import chromadb
import os
import requests
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHROMA_PATH = r"chroma"

#Initialize the chroma client, collections and the embedding model

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="assessment_colelction")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")



print("Welcome ASTUDIO Customer Support!")

while True:
    user_query = input("What queries do you have? (Enter 'Q' to quit)\n")
    if user_query.strip().upper() == 'Q':
        print("Thank you for using ASTUDIO Customer Support!")
        break


# Vectoirze the user query and retrieve the most similar document from the collection
    query_embedding = embedding_model.encode([user_query]).tolist()

# Query the chromadb to perform a similairy search to retrive the most relevant answers
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )

    retrieved_docs = results["documents"][0] if results["documents"] else ["I don't know"]
    retrieved_text = "\n".join(retrieved_docs)

#Define a prompt template for the agent so that it's answers are scoped with respect to the information that it retrives from the chroma
    
    system_prompt = f"""
    You are a customer support agent who will answer queries regarding our current products as well as queries regarding our policies. You answer questions about our products and services.
    Maintain a friendly and professional tone. When asked about a product give it all the information without requesting and additional prompt frpm the user.
    But you only answer based on knowledge I'm providing you. You don't use your internal 
    knowledge and you don't make things up.
    If you don't know the answer, just say: I don't know
    --------------------
    The data:
    {retrieved_text}
    """

    # Call Groq API (Llama 3)
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

# Define the payload as weel as the parameters for the model to optimise response quality
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

# Print the response from the model 
    if response.status_code == 200:
        result = response.json()
        print("\n---------------------\n")
        print(result['choices'][0]['message']['content'])
        print("\n---------------------\n")
    else:
        print("Error:", response.text)