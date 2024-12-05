def custom_entity_filter(doc):

    seen_entities:set = set()
    new_entities:list = []

    for ent in doc.ents:
        if ent.text.lower() not in seen_entities:
            seen_entities.add(ent.text.lower())
            new_entities.append(ent)
    

    doc.ents = new_entities
    return doc

