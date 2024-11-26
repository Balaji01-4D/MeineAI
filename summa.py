import time
import typer as tp
a = time.time()
import spacy
nlp = spacy.load('summaMeineAI')
print(f"{a - time.time():.2f}")
while True:
    command = input("enter the commad>> ")
    doc = nlp(command)
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")