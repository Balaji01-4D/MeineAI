import time
from rich.console import Console
from spacy import load
from spacy.language import Language
import spacy
from spacy.tokens import Span,Doc

start_time = time.time()
console = Console()



@Language.component('personremove')
def custom_entity_filter(doc:Doc):

    seen_entities:set = set()
    new_entities:list = []

    for ent in doc.ents:
        if ent.text.lower() not in seen_entities:
            seen_entities.add(ent.text.lower())
            new_entities.append(ent)
    

    doc.ents = new_entities
    return doc
# Use a spinner by specifying its name as a string
with console.status("[bold cyan]Loading...", spinner="dots",):

    nlp = load('en_core_web_sm')  # Load the model




nlp.add_pipe('personremove',first=True)
print(f"Model loaded in {time.time() - start_time:.2f} seconds")


# command = 'delete the file.txt /java/projects/'
command = 'john enjoys playing basketball in berlin in June'
doc = nlp(command)

for ent in doc.ents:
    print(f"{doc.spans} {ent.text} ({ent.label_})")

doc = Doc(nlp.vocab)
