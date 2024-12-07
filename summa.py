import spacy

nlp = spacy.load('./LGmoder/model-best')


# with open('./MeineAI/dataset/raw/all.txt') as file:
#     l = file.readlines()


# for i,j in enumerate(l):
#     if (i == 50):
#         break
#     j=j.replace('\n','')
#     doc = nlp(j)
#     print([(ent.text,ent.label_) for ent in doc.ents])


# while True:
#     cmd = input("enter >>> ")
#     doc = nlp(cmd)
#     print([(ent.text,ent.label_) for ent in doc.ents])