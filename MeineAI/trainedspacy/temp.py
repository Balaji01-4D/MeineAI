

import spacy
from spacy.tokens import DocBin
# List of file paths to your .spacy files
spacy_files = [ "/home/balaji/MeineAI/MeineAI/trainedspacy/allnotseen.spacy", "/home/balaji/MeineAI/MeineAI/trainedspacy/final.spacy"]


# Create a new DocBin object to store combined data
merged_doc_bin = DocBin()

nlp = spacy.blank('en')
# Iterate through each .spacy file and add its contents to the merged DocBin
for file_path in spacy_files:
    with open(file_path, "rb") as f:
        doc_bin = DocBin().from_bytes(f.read())
        for doc in doc_bin.get_docs(nlp.vocab):
            merged_doc_bin.add(doc)

merged_doc_bin.to_disk('finalpro.spacy')

print("Merging complete. The merged data is saved in 'merged_file.spacy'.")
