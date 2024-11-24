import spacy
from spacy.util import minibatch, compounding
from pathlib import Path

def create_ner_model(model_name, labels):
    # Create a blank spaCy model
    nlp = spacy.blank("en")
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")
    
    # Add labels to the NER component
    for label in labels:
        ner.add_label(label)
    
    # Save the blank model
    model_path = Path(f"./{model_name}")
    if not model_path.exists():
        model_path.mkdir()
    nlp.to_disk(model_path)
    print(f"Model '{model_name}' created and saved at {model_path}.")

# Define the labels from your dataset
labels = ["FIle_FolderName", "Action", "New_Name", "Destination","Etc"]

# Create the model
create_ner_model("summaMeineAI", labels)
