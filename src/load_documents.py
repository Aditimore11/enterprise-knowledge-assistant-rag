from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

print("Loading enterprise documents...")

loader = DirectoryLoader(
    path="../dataset",
    glob="**/*.md",
    loader_cls=TextLoader,
    show_progress=True
)

documents = loader.load()

print("\n===================================")
print("ENTERPRISE DATASET LOADED")
print("===================================")

print(f"Total Documents: {len(documents)}")

print("\nFirst 5 documents:")

for i, doc in enumerate(documents[:5]):
    print("\n--------------------")
    print(f"Document {i+1}")
    print(doc.metadata["source"])