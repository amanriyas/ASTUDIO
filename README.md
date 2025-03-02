# ASTUDIO
ASTUDIO Practical Assessment

# Customer Support AI Agent

A basic AI-powered customer support agent that leverages RAG (Retrieval Augmented Generation) to answer common e-commerce questions. The agent retrieves information from a knowledge base containing product information and company policies to provide accurate responses to customer queries.

## Overview

This application consists of two main components:
1. A data ingestion script that processes text files and stores them in a vector database
2. A command-line interface for interacting with the agent

The system uses:
- ChromaDB for vector storage
- Sentence Transformers for embedding generation
- Llama3 8B model via Groq API for generating responses

## Features

- Answers questions about products (descriptions, prices, features, etc.)
- Provides information about company policies (shipping, returns, etc.)
- Simple command-line interface
- Maintains context through RAG implementation

## Requirements

- Python 3.8+
- Groq API key (for accessing Llama3 model)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/customer-support-ai.git
cd ASTUDIO
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
On Windows: venv\Scripts\activate
On Mac/Linux: venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

5. Create a folder named `data` in the project root and add your product and policy text files. For this assessment I ahve added my own custom txt file swith 5 products and a txt file for company policies.

## Usage

1. First, run the data ingestion script to create the vector database so that the data is chunked, vectorized and stored in the database for RAG retrieval:
```bash
python vector_store.py
```

2. Then, run the chat interface to interact with the agent:
```bash
python ask.py
```

3. Enter your questions at the prompt. Type 'Q' to exit the application.

## Example Conversations

### Example 1: Product Information Query
```
Welcome ASTUDIO Customer Support!
What queries do you have? (Enter 'Q' to quit)
How much does the UltraPhone X cost?

---------------------

The UltraPhone X costs $799. It's available in three colors: Black, Silver, and Blue. The phone features a 6.5" OLED display, 128GB storage, and a 12MP camera. It's currently in stock and ready to ship.

---------------------
```

### Example 2: Shipping Policy Query
```
Welcome ASTUDIO Customer Support!
What queries do you have? (Enter 'Q' to quit)
What are your shipping options?

---------------------

We offer two shipping options:
1. Standard shipping (3-5 business days) for $4.99
2. Express shipping (1-2 business days) for $12.99

Good news! Orders over $50 qualify for free standard shipping.

---------------------
```

### Example 3: Return Policy Query
```
Welcome ASTUDIO Customer Support!
What queries do you have? (Enter 'Q' to quit)
Can I return a product if I don't like it?

---------------------

Yes, you can return a product if you're not satisfied with it. Our return policy allows returns within 30 days of purchase for a full refund. The product must be in its original condition with all packaging. Please note that shipping costs are non-refundable. Contact our customer service team to initiate a return.

---------------------
```


## How It Works

1. **Data Ingestion (ingest.py)**:
   - Loads text files from the `data` directory
   - Splits documents into chunks
   - Generates embeddings using Sentence Transformers
   - Stores chunks and embeddings in ChromaDB

2. **Chat Interface (chat.py)**:
   - Takes user queries via command line
   - Converts queries to embeddings
   - Retrieves relevant information from ChromaDB
   - Sends the query and retrieved context to Llama3 via Groq API
   - Displays the generated response

