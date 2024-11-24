import spacy
from spacy.training.example import Example
from spacy.util import minibatch, compounding
import random
from pathlib import Path

def train_ner_model(model_name, train_data, n_iter=20):
    # Load the existing model or initialize a blank one
    model_path = Path(f"./{model_name}")
    if model_path.exists():
        nlp = spacy.load(model_path)
    else:
        nlp = spacy.blank("en")  # Start with a blank English model
        nlp.add_pipe("ner")  # Add a new NER pipeline
    
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
    ('delete the file data.csv', {'entities': [(16, 24, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('rename the report.docx as summary.docx', {'entities': [(26, 38, 'New_Name'), (11, 22, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('clear the file temp_log.txt', {'entities': [(15, 27, 'FIle_FolderName'), (0, 5, 'Action')]}),
    ('copy the file notes.xls to documents folder', {'entities': [(27, 36, 'Destination'), (14, 23, 'FIle_FolderName'), (0, 4, 'Action')]}),
    ('move the image.png to images folder', {'entities': [(22, 28, 'Destination'), (9, 18, 'FIle_FolderName'), (0, 4, 'Action')]}),
    ('create the file new_project.ipynb', {'entities': [(16, 33, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('show content of log.txt', {'entities': [(16, 23, 'FIle_FolderName'), (0, 12, 'Action')]}),
    ('create the folder archives', {'entities': [(18, 26, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('delete the folder old_data', {'entities': [(18, 26, 'FIle_FolderName'), (0, 6, 'Action')]}),
    ('list the files in folder documents', {'entities': [(25, 34, 'FIle_FolderName'), (0, 14, 'Action')]}),
]

# Train the model
train_ner_model("summaMeineAI", train_data)
