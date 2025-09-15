import chromadb
import os

# Point to your ChromaDB folder
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma", "war_health_chroma_db")

print(f"Loading ChromaDB from: {CHROMA_PATH}")

# Initialize client
client = chromadb.PersistentClient(path=CHROMA_PATH)

# List collections
print("\n Collections in DB:")
collections = client.list_collections()
for col in collections:
    print(f" - {col.name} (ID: {col.id})")

# Try to get your collection
try:
    collection = client.get_collection(name="war_health_embeddings")
    count = collection.count()
    print(f"\n Success! Collection 'war_health_embeddings' loaded.")
    print(f"Total items: {count}")
except Exception as e:
    print(f"\n Error loading collection: {e}")
    print("\n Let's try to get collection by ID instead...")

    # If name fails, try by ID (use the folder name)
    if collections:
        first_collection = collections[0]
        collection = client.get_collection(name=first_collection.name)
        count = collection.count()
        print(f"Loaded collection '{first_collection.name}' by ID.")
        print(f"Total items: {count}")
    else:
        print("No collections found. DB may be empty or corrupted.")