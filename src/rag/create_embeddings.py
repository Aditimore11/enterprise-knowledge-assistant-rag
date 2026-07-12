from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Model loaded successfully!")

query = "What is the annual leave policy?"

embedding = model.encode(query)

print("\n================================")
print("EMBEDDING CREATED")
print("================================")

print(f"Embedding Dimensions: {len(embedding)}")

print("\nFirst 10 values:")
print(embedding[:10])