import spacy
from pathlib import Path

def test_ner_model(model_name, text):
    # Load the trained model
    model_path = Path(f"./{model_name}")
    if model_path.exists():
        nlp = spacy.load(model_path)
    else:
        print(f"Model '{model_name}' not found. Train the model first.")
        return

    # Process the input text
    doc = nlp(text)

    # Display the entities found in the text
    print(f"Input Text: {text}")
    print("Entities Detected:")
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")
    
# Test the model with example input
test_input = "rename the report.docx as summary.docx"
test_ner_model("MeineAI", test_input)
