import spacy
from spacy.util import minibatch, compounding
from pathlib import Path
import random 

def train_ner_model(model_name:str, train_data:list[set], n_iter=20):
    # Load the existing model or initialize a blank one
    model_path = Path(f"./{model_name}")
    if model_path.exists():
        nlp = spacy.load(model_path)
    else:
        print(f"Model '{model_name}' not found. Run the creation script first.")
        return

    # Get the NER pipeline
    ner = nlp.get_pipe("ner")
    
    # Add labels if they're new
    for _, annotations in train_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # Disable other pipelines during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.resume_training() if model_path.exists() else nlp.begin_training()
        for itn in range(n_iter):
            losses = {}
            # Shuffle training data
            random.shuffle(train_data)
            batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, drop=0.5, losses=losses)
            print(f"Iteration {itn+1}, Losses: {losses}")

    # Save the trained model
    nlp.to_disk(model_path)
    print(f"Model '{model_name}' trained and saved at {model_path}.")

# Example dataset
train_data = [
    ('delete the file data.csv', {'entities': [(16, 24, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('rename the report.docx as summary.docx', {'entities': [(26, 38, 'New_Name'), (11, 22, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('clear the file temp_log.txt', {'entities': [(15, 27, 'FIle_FolderName'), (0, 5, 'Action')]}),
    ('copy the file notes.xls to documents folder', {'entities': [(27, 36, 'Destination'), (14, 23, 'FIle_FolderName'), (0, 4, 'Action')]}),
    ('move the image.png to images folder', {'entities': [(22, 28, 'Destination'), (9, 18, 'FIle_FolderName'), (0, 4, 'Action')]}),
    ('create the file new_project.ipynb', {'entities': [(16, 33, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('show content of log.txt', {'entities': [(16, 23, 'FIle_FolderName'), (0, 12, 'Action')]}),
    ('create the folder archives', {'entities': [(18, 26, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('delete the folder old_data', {'entities': [(18, 26, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('list the files in folder documents', {'entities': [(25, 34, 'FIle_FolderName'), (0, 14, 'Action')]})
]

# Train the model
train_ner_model("MeineAI", train_data)
