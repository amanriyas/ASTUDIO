from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import os 
from sentence_transformers import SentenceTransformer


DATA_PATH = r"data"
CHROMA_PATH = r"chroma"

chroma_client = chromadb.PersistentClient(path = CHROMA_PATH)

collection = chroma_client.get_or_create_collection("assessment_colelction")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []

metadata = []

for filename in os.listdir(DATA_PATH):
    if filename.endswith(".txt"):
        file_path = os.path.join(DATA_PATH, filename)
        loader = TextLoader(file_path)
        raw_documents = loader.load()
        documents.extend(raw_documents)
        metadata.extend([{"source": filename}] * len(raw_documents))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)   



chunks = text_splitter.split_documents(documents)

chunk_texts = [chunk.page_content for chunk in chunks]
chunk_metadata = [chunk.metadata for chunk in chunks]
chunk_ids = [f"ID{i}" for i in range(len(chunks))]
chunk_embeddings = embedding_model.encode(chunk_texts).tolist()  


collection.upsert(
    documents=chunk_texts,
    metadatas=chunk_metadata,
    ids=chunk_ids,
    embeddings=chunk_embeddings  # Now storing vectors
)

query = "What is your return policy?"

query_embedding = embedding_model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3  # Retrieve top 3 most relevant chunks
)

print(results)