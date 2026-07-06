from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from langchain_huggingface import (
    HuggingFaceEmbeddings,
)

from langchain_community.vectorstores import (
    FAISS,
)

print("Loading enterprise documents...")

loader = DirectoryLoader(
    "../dataset",
    glob="**/*.md",
    loader_cls=TextLoader,
    show_progress=True,
)

documents = loader.load()

print(f"Total Documents: {len(documents)}")

print("\nCreating chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks: {len(chunks)}")

print("\nLoading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating FAISS vector database...")

vectorstore = FAISS.from_documents(
    chunks,
    embeddings,
)

print("\nSaving vector database...")

vectorstore.save_local(
    "../vectorstore"
)

print("\n================================")
print("FAISS DATABASE CREATED")
print("================================")
print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")
print("Location: ../vectorstore")