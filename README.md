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

## Getting a Groq API Key
To use this application, you'll need a Groq API key to access the Llama3 model. Follow these steps to obtain one:

1. Create a Groq Account:

- Visit Groq's website and sign up for an account
- Complete the registration process with your email and password


2. Access the API Key:

- After registration and login, navigate to the API section of your account dashboard
- Look for "API Keys" or similar section
- Click on "Create API Key" or "Generate New Key"
- Give your key a name (e.g., "Customer Support AI")


3. Copy Your API Key:

- Once generated, copy the API key to your clipboard
- Important: Store this key securely as it may only be displayed once

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

5. Create a folder named `data` in the project root and add your product and policy text files. For this assessment I havve added my own custom txt file swith 5 products and a txt file for company policies. They are as follows:

policy.txt
```
Company Policy
Our company is committed to providing high-quality products and exceptional customer service. We prioritize customer satisfaction, transparency, and ethical business practices. Our policies are designed to ensure a smooth shopping experience while maintaining fairness for both customers and the company.

- Customer Support: Our team is available Monday to Friday from 9 AM to 6 PM to assist with any inquiries.
- Privacy Policy: Customer data is securely stored and never shared with third parties without consent.
- Warranty: All electronic products come with a one-year limited warranty covering manufacturing defects.
- Shipping: Orders are processed within 24-48 hours. Shipping times may vary based on location.

Return Policy
We strive to ensure our customers are satisfied with their purchases. If you are not completely satisfied, you may return the product under the following conditions:

- Eligibility: Products must be returned within 30 days of purchase.
- Condition: Items must be in their original packaging, unused, and in resalable condition.
- Non-Returnable Items: Digital goods, gift cards, and personalized items are non-refundable.
- Refund Process: Refunds will be processed within 7-10 business days after the returned product is received and inspected.
- Return Shipping: Customers are responsible for return shipping costs unless the product is defective or incorrect.

For any return or refund requests, please contact our support team with your order details.
```

products.txt
```
Product: UltraPhone X
Price: $799
Features: 6.5" OLED display, 128GB storage, 12MP camera
Colors: Black, Silver, Blue
Availability: In stock
Shipping Policy:
Standard shipping (3-5 business days): $4.99
Express shipping (1-2 business days): $12.99
Free standard shipping on orders over $50

Product: SmartTab 10
Price: $499
Features: 10" LCD display, 256GB storage, 8MP camera
Colors: Gray, White, Gold
Availability: In stock
Shipping Policy:
Standard shipping (3-5 business days): $4.99
Express shipping (1-2 business days): $12.99
Free standard shipping on orders over $50

Product: NoiseFit Pro
Price: $199
Features: 1.8" AMOLED display, Heart rate monitor, GPS tracking
Colors: Black, Red, Blue
Availability: In stock
Shipping Policy:
Standard shipping (3-5 business days): $4.99
Express shipping (1-2 business days): $12.99
Free standard shipping on orders over $50

Product: SonicBuds 2
Price: $149
Features: Active noise cancellation, 24-hour battery life, Wireless charging
Colors: White, Black, Green
Availability: In stock
Shipping Policy:
Standard shipping (3-5 business days): $4.99
Express shipping (1-2 business days): $12.99
Free standard shipping on orders over $50

Product: PowerBank 20K
Price: $59
Features: 20,000mAh capacity, Fast charging, Dual USB-C ports
Colors: Black, Blue
Availability: In stock
Shipping Policy:
Standard shipping (3-5 business days): $4.99
Express shipping (1-2 business days): $12.99
Free standard shipping on orders over $50
```

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
How much does the UltraPhone X cost and what are it's features?

---------------------

The UltraPhone X is priced at $799. As for its features, it comes with a 6.5" OLED display, 128GB of storage, and a 12MP camera.

---------------------
```

### Example 2: Shipping Policy Query
```
What queries do you have? (Enter 'Q' to quit)
What are your shipping options?

---------------------

We offer two shipping options for your convenience. Our Express Shipping option takes 1-2 business days and costs $12.99. Additionally, we offer Free Standard Shipping on all orders over $50.

---------------------
```

### Example 3: Return Policy Query
```
What are your return policies?

---------------------

Our return policy is designed to provide our customers with a hassle-free experience. We accept returns within 30 days of delivery for all products.

To initiate a return, please contact our customer support team and provide us with your order number, the reason for the return, and whether you would like a refund, exchange, or store credit.

The item must be in its original condition, with all original tags and packaging intact. We also require that the item is in a resellable condition.

Once we receive the returned item, we will process your refund or exchange within 5-7 business days. Refunds will be issued in the original form of payment.

Please note that some products may have a restocking fee, which will be deducted from your refund. This will be clearly stated on the product page and in your order confirmation email.

If you have any further questions or concerns about our return policy, please don't hesitate to reach out to us. We're here to help!

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

