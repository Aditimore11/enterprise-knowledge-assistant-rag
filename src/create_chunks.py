from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Loading enterprise documents...")

loader = DirectoryLoader(
    "../dataset",
    glob="**/*.md",
    loader_cls=TextLoader,
    show_progress=True
)

documents = loader.load()

print(f"\nTotal Documents: {len(documents)}")

print("\nCreating chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]
)

chunks = splitter.split_documents(documents)

print("\n==============================")
print("CHUNKING COMPLETED")
print("==============================")

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:")
print("-"*50)
print(chunks[0].page_content[:500])

print("\nChunk Metadata:")
print(chunks[0].metadata)