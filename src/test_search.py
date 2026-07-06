from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading vector database...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "../vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Vector database loaded successfully!")

# Test queries
queries = [
    "What is the annual leave policy?",
    "How do employees request VPN access?",
    "What is the expense reimbursement process?",
    "What is the travel policy?",
    "How does the deployment process work?"
]

for query in queries:
    print("\n" + "="*60)
    print("QUERY:", query)
    print("="*60)

    docs = db.similarity_search(query, k=3)

    for i, doc in enumerate(docs):
        print(f"\nResult {i+1}")
        print("Source:", doc.metadata["source"])
        print("\nContent Preview:")
        print(doc.page_content[:300])
        print("-"*50)