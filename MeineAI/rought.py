import spacy
from spacy import displacy
from spacy import Language
from spacy.tokens import Doc,Span



nlp2 = spacy.load('MeineAI/output_dir/model-best')


with open('/home/balaji/MeineAI/MeineAI/dataset/raw/all.txt') as file:
    l = file.readlines()


for i,command in enumerate(l,start=0):
    if (i == 15):
        break
    command = command.replace('\n','')
    doc = nlp2(command)
    print([(ent.label_,ent.text) for ent in doc.ents])
    