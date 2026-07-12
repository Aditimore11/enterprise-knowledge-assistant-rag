from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Load Embedding Model
# -----------------------------
print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Load FAISS Database
# -----------------------------
print("Loading vector database...")

db = FAISS.load_local(
    "../vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20,
        "lambda_mult": 0.7
    }
)

# -----------------------------
# Load LLM
# -----------------------------
print("Loading LLM...")

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# -----------------------------
# Prompt Template
# -----------------------------
template = """
You are TechNova Solutions' Enterprise AI Assistant.

Use ONLY the retrieved enterprise documents to answer.

Rules:
1. Do not use outside knowledge.
2. Combine information from multiple retrieved documents when appropriate.
3. If the answer is only partially available, say what is available.
4. If the answer is completely absent, reply:
"I couldn't find that information in the enterprise knowledge base."

Context:
{context}

Question:
{question}

Provide a clear, structured answer.
"""

prompt = ChatPromptTemplate.from_template(template)

print("RAG Pipeline Ready!")


def ask_question(question):

    results = db.similarity_search_with_score(question, k=5)

    context = ""
    retrieved_docs = []

    print("\nRetrieved Documents:")
    print("=" * 70)

    for doc, score in results:

        retrieved_docs.append(doc)

        print(f"\nScore : {score:.4f}")
        print("Source:", doc.metadata["source"])
        print(doc.page_content[:200])
        print("-" * 70)

        context += doc.page_content + "\n\n"

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    return response.content, retrieved_docs


while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer, docs = ask_question(question)

    print("\nAnswer:\n")
    print(answer)

    print("\nSources:")

    seen = set()

    for doc in docs:

        source = doc.metadata["source"]

        if source not in seen:
            seen.add(source)
            print("-", source)