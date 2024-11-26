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

]

# Train the model
train_ner_model("summaMeineAI", train_data)
