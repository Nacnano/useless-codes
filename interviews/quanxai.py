# Given a list of documents
# Each document has an id and content
# Task: Search for a word and return the list of document ids that contain that word 
# Hard version: Search for a phrase and return the list of document ids that contain that phrase

documents = [
    {"id": 1, "content": "This is about machine learning. Mostly implement with Python"},
    {"id": 2, "content": "Python programming tutorial"},
    {"id": 3, "content": "Machine learning with Python"}
]

hasInDocument = dict()

for document in documents:
    documentId = document["id"]
    content = document["content"]
    words = content.split(" ")
    
    for word in words:
        if word not in hasInDocument:
            hasInDocument[word] = set()
        hasInDocument[word].add(documentId)
        
print(hasInDocument["machine"])
    
    
