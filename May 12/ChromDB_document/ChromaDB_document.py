import chromadb

# To create a chromaDB instance
client = chromadb.Client()

# Create a new collection
collection = client.create_collection("example_collection")

# Sample document
document = {
    "id": "1", 
    "content": "This is a sample document", 
    "metadata": {"author": "Santhra", "category": "example"}
}

# Add document to the collection
collection.add(
    documents=[document["content"]],
    metadatas=[document["metadata"]],
    ids=[document["id"]],
)

print("Document added successfully!")
