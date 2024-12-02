import re
from spacy.language import Language
import spacy
nlp = spacy.load('./MEINEAIBETA')
@Language.component("file_recognizer")
def file_recognizer(doc):
    pattern = r"(\b\S+\.pdf\b|\b\S+\.log\b|(?:/[\w-]+)+\.\w+)"
    matches = re.finditer(pattern, doc.text)
    spans = [doc.char_span(m.start(), m.end(), label="FILE") for m in matches]
    doc.ents = list(doc.ents) + [span for span in spans if span is not None]
    return doc

# Add the component to the pipeline
# nlp.add_pipe("file_recognizer", before="ner")
def CMDMapper(labels: list[str],text: list[str]) -> dict[str]:
    cdict = {}
    Backup = {'ACTION':'ACTION2','FILE':'NEWNAME','FOLDER':'DESTINATION'}
    for label,val in zip(labels,text):
        if (cdict.__contains__(label)):
            cdict[Backup[label]] = val
        else :
            cdict[label] = val
    return cdict

# Test the custom component
while True:
    command = input(">>> ")
    text = []
    labels = []
    doc = nlp(command)
    for ent in doc.ents:
        text.append(ent.text)
        labels.append(ent.label_)

    print(CMDMapper(labels,text))

