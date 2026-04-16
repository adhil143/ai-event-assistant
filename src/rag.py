import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("events")

def store_event(name, notes):
    collection.add(
        documents=[notes],
        ids=[name]
    )

def get_memory(name):
    try:
        result = collection.get(ids=[name])
        return result['documents'][0]
    except:
        return ""