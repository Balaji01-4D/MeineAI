import spacy
from spacy.training.example import Example
from spacy.util import minibatch, compounding
import random
from pathlib import Path

def train_ner_model(model_name, train_data, n_iter=30):
    # Load the existing model or initialize a blank one
    model_path = Path(f"./{model_name}")
    if model_path.exists():
        nlp = spacy.load(model_path)
    else:
        nlp = spacy.load("en_core_web_lg")  # Start with a blank English model
        # nlp.add_pipe("ner")  # Add a new NER pipeline
    
    ner = nlp.get_pipe("ner")

    # Add labels from the training data
    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # Convert training data to Example objects
    examples = []
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        examples.append(Example.from_dict(doc, annotations))

    # Disable other pipelines during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        if not model_path.exists():
            optimizer = nlp.begin_training()
        else:
            optimizer = nlp.resume_training()

        for itn in range(n_iter):
            losses = {}
            random.shuffle(examples)  # Shuffle the training examples
            batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))

            for batch in batches:
                nlp.update(batch, drop=0.5, losses=losses)

            print(f"Iteration {itn + 1}, Losses: {losses}")

    # Save the trained model
    nlp.to_disk(model_path)
    print(f"Model '{model_name}' trained and saved at {model_path}.")

# Example dataset
train_data = [
('clear the file home/docs/user/system.log', {'entities': [(15, 40, 'File_FolderName'), (0, 5, 'Action')]}), ('copy the file home/docs/invoice.pdf to home/finance/invoice.pdf', {'entities': [(36, 63, 'Destination'), (14, 35, 'File_FolderName'), (0, 4, 'Action')]}), ('move the home/docs/draft.pptx to home/docs/presentations/', {'entities': [(30, 57, 'Destination'), (9, 29, 'File_FolderName'), (0, 4, 'Action')]}), ('create the file home/logs/debug_info.log', {'entities': [(16, 40, 'File_FolderName'), (0, 6, 'Action')]}), ('show content of home/scripts/module.py', {'entities': [(16, 38, 'File_FolderName'), (0, 12, 'Action')]}), ('create the folder home/logs/system_logs', {'entities': [(18, 39, 'File_FolderName'), (0, 6, 'Action')]}), ('delete the folder home/files/unused_files', {'entities': [(18, 41, 'File_FolderName'), (0, 6, 'Action')]}), ('list the files in folder home/data/datasets', {'entities': [(25, 43, 'File_FolderName'), (0, 14, 'Action')]}), ('move the home/logs/logs to home/reports/reports_folder', {'entities': [(24, 54, 'Destination'), (9, 23, 'File_FolderName'), (0, 4, 'Action')]}), ('copy the folder home/archives/archive_data to home/storage/storage_units', {'entities': [(43, 72, 'Destination'), (16, 42, 'File_FolderName'), (0, 4, 'Action')]}), ('change directory to /home/user/Downloads', {'entities': [(20, 40, 'Path'), (0, 16, 'Action')]}), ('cd to /home/user/Archives/2025', {'entities': [(6, 30, 'Path'), (0, 2, 'Action')]}), ('delete the file home/reports/test_results.xlsx', {'entities': [(16, 46, 'File_FolderName'), (0, 6, 'Action')]}), ('rename the home/docs/todo.md as home/docs/tasks.md', {'entities': [(32, 50, 'NewName'), (11, 28, 'File_FolderName'), (0, 6, 'Action')]}), ('clear the file home/temp/session.log', {'entities': [(15, 36, 'File_FolderName'), (0, 5, 'Action')]}), ('copy the file home/server/server_config.txt to home/server/server_folder', {'entities': [(44, 72, 'Destination'), (14, 43, 'File_FolderName'), (0, 4, 'Action')]}), ('move the home/images/diagram.png to home/drawings/diagram.png', {'entities': [(33, 61, 'Destination'), (9, 32, 'File_FolderName'), (0, 4, 'Action')]}), ('create the file home/docs/roadmap.txt', {'entities': [(16, 37, 'File_FolderName'), (0, 6, 'Action')]}), ('show content of home/config/debug.yaml', {'entities': [(16, 38, 'File_FolderName'), (0, 12, 'Action')]}), ('create the folder home/application/application_files', {'entities': [(18, 52, 'File_FolderName'), (0, 6, 'Action')]}), ('delete the folder home/system/deprecated_modules', {'entities': [(18, 48, 'File_FolderName'), (0, 6, 'Action')]}), ('list the files in folder home/api/api_docs', {'entities': [(25, 42, 'File_FolderName'), (0, 14, 'Action')]}), ('move the home/source/source_code to home/version/version_control', {'entities': [(33, 64, 'Destination'), (9, 32, 'File_FolderName'), (0, 4, 'Action')]}), ('copy the folder home/docs/documents to home/drive/personal_drive', {'entities': [(36, 64, 'Destination'), (16, 35, 'File_FolderName'), (0, 4, 'Action')]}), ('change directory to /home/system/System', {'entities': [(20, 39, 'Path'), (0, 16, 'Action')]}), ('cd to /home/images/family_photos', {'entities': [(6, 32, 'Path'), (0, 2, 'Action')]}), ('delete the file home/code/code_snippets.java', {'entities': [(16, 44, 'File_FolderName'), (0, 6, 'Action')]}), ('rename the home/db/backup.sql as home/db/database.sql', {'entities': [(33, 53, 'NewName'), (11, 29, 'File_FolderName'), (0, 6, 'Action')]}), ('clear the file home/logs/api_requests.log', {'entities': [(15, 41, 'File_FolderName'), (0, 5, 'Action')]}), ('copy the file home/images/profile.jpg to home/pictures/profile_pictures', {'entities': [(38, 71, 'Destination'), (9, 37, 'File_FolderName'), (0, 4, 'Action')]}), ('move the home/docs/annual_meeting.pdf to home/docs/documents/annual_meeting.pdf', {'entities': [(38, 79, 'Destination'), (9, 37, 'File_FolderName'), (0, 4, 'Action')]}), ('create the file home/logs/new_log.txt', {'entities': [(16, 37, 'File_FolderName'), (0, 6, 'Action')]}), ('show content of home/templates/template.html', {'entities': [(16, 44, 'File_FolderName'), (0, 12, 'Action')]}), ('create the folder home/compressed/compressed_files', {'entities': [(18, 50, 'File_FolderName'), (0, 6, 'Action')]}), ('delete the folder home/temp/temporary_files', {'entities': [(18, 43, 'File_FolderName'), (0, 6, 'Action')]}), ('compress the folder home/data/dataset', {'entities': [(20, 37, 'File_FolderName'), (0, 8, 'Action')]}), ('compress the folder home/docs/reports', {'entities': [(20, 37, 'File_FolderName'), (0, 8, 'Action')]}), ('extract the folder home/data/datasets', {'entities': [(19, 37, 'File_FolderName'), (0, 7, 'Action')]}), ('extract the folder home/cloud/cloud_storage', {'entities': [(19, 43, 'File_FolderName'), (0, 7, 'Action')]}), ('search the file home/scripts/yahoo.py', {'entities': [(16, 37, 'File_FolderName'), (0, 6, 'Action')]}), ('show the disk usage', {'entities': [(0, 19, 'Action')]}), ('show the details of home/docs/report.pdf', {'entities': [(20, 40, 'File_FolderName'), (0, 16, 'Action')]}), ('compress the file home/scripts/reports.py', {'entities': [(18, 41, 'File_FolderName'), (0, 8, 'Action')]}), ('compress the file home/data/datasets.py', {'entities': [(18, 39, 'File_FolderName'), (0, 8, 'Action')]}), ('extract the folder home/cloud/cloud_storage', {'entities': [(19, 43, 'File_FolderName'), (0, 7, 'Action')]}), ('extract file.py new.py calc.html index.css from folder home/cloud/cloud_storage.zip', {'entities': [(55, 83, 'File_FolderName'), (8, 42, 'File_List'), (0, 7, 'Action')]}), ('search the text submission_reports in files', {'entities': [(38, 43, 'File_FolderName'), (16, 34, 'Text'), (0, 6, 'Action')]}), ('extract month.csv, months.xlsx, year.csv from folder home/finance/accountance.zip', {'entities': [(53, 81, 'File_FolderName'), (8, 40, 'File_List'), (0, 7, 'Action')]})
]

# Train the model
train_ner_model("pretrainedsm", train_data)
