import spacy
from spacy import displacy
from spacy import Language
from spacy.tokens import Doc,Span

@Language.component('rename')
def Rename(doc: Doc):
    for ent in doc.sents:
        print(ent.text)
    return doc





nlp2 = spacy.load('output/model-best')
nlp2.add_pipe("rename",after='ner')


with open('dataset/raw/rename.txt') as file:
    l = file.readlines()


for command in l:
    command = command.replace('\n','')
    doc = nlp2(command)
    print([(ent.label_,ent.text) for ent in doc.sents])