import os
from dotenv import load_dotenv
import chromadb
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import Chroma
import json
from guidelines import fdata
import requests
from sentence_transformers import SentenceTransformer

os.environ["OPENAI_API_KEY"]="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"
os.environ["OPENROUTER_API_KEY"]="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"



def get_openrouter_embedding(text, model_name="huggingface/all-mpnet-base-v2"):
    """
    Gets an embedding for the given text using an embedding model via OpenRouter.

    Args:
        text (str): The text to embed.
        model_name (str): The name of the embedding model on OpenRouter.
            Defaults to "huggingface/all-mpnet-base-v2".  You can change this.

    Returns:
        list: The embedding for the text, or None on error.
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        return None

    url = "https://openrouter.ai/api/v1/embeddings"
    #url = "https://openrouter.ai/api/v1"
    headers = {
        "Authorization": f"Bearer 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",
        "Content-Type": "application/json",
    }
    data = {
        "model": model_name,
        "input": [text],
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise for bad status codes
        result = response.json()
        # **Important:** The following line assumes the OpenRouter response
        # has the embedding in this structure.  This may vary by model!
        # Double-check the OpenRouter API documentation for the model you use.
        return result["data"][0]["embedding"]
    except requests.exceptions.RequestException as e:
        print(f"Error getting embedding from OpenRouter: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response from OpenRouter: {e}")
        return None
    except KeyError as e:
        print(
            f"Error accessing embedding in response: {e}.  Check the response format from OpenRouter for the model: {model_name}"
        )
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def load_financial_data(persist_directory="financial_vector_db", include_examples=True):
    """
    Loads financial request type and sub-request type data into a Chroma vector store.
    If the database already exists, it loads from the persisted directory.
    If not, it creates the data and persists it.  Now includes example emails.

    Args:
        persist_directory (str): The directory to persist the Chroma database.
        include_examples (bool): Whether to include example emails in the vector store.
            Defaults to True.

    Returns:
        Chroma: A Chroma vector store containing the financial data.
    """
    # 1. Define financial request types and sub-request types.
    #    -  This is your knowledge base.  In a real application, this would
    #       likely come from a database or configuration files.
    financial_data = fdata

    # 2.  Create embeddings using OpenAI.
    embeddings = OpenAIEmbeddings()

    # 3.  Use Chroma to store the embeddings.
    #     -  We use the request types, sub-types, and now example emails as the text to embed.
    #     -  We store the full data structure in the metadata, so we can
    #        retrieve it later.
    persist_directory = persist_directory
    # client = chromadb.Client(
    #     settings=chromadb.config.Settings(
    #         chroma_db_impl="duckdb+filesystem",
    #         persist_directory=persist_directory,
    #     )
    # )
    client = chromadb.PersistentClient(path=persist_directory)

    collection_name = "financial_requests"
    try:
        collection = client.get_collection(name=collection_name)
    except:  # Collection does not exist
        collection = client.create_collection(name=collection_name)

    if collection.count() == 0:
        texts = []
        metadatas = []
        ids = []
        for item in financial_data:
            request_type = item["request_type"]
            request_definition = item["definition"]

            # Add request type and definition.
            texts.append(f"Request Type: {request_type}. Definition: {request_definition}")
            metadatas.append({"type": "request_type", "request_type": request_type})
            ids.append(f"reqtype-{request_type}")

            for sub_type_data in item["sub_types"]:
                sub_type_name = sub_type_data["name"]
                sub_type_definition = sub_type_data["definition"]
                texts.append(f"Sub-Request Type: {sub_type_name}. Definition: {sub_type_definition}")
                metadatas.append(
                    {
                        "type": "sub_type",
                        "request_type": request_type,
                        "sub_type": sub_type_name,
                    }
                )
                ids.append(f"subtype-{request_type}-{sub_type_name}")

            for example in item.get("examples", []):  # Use .get() to handle missing "examples"
                example_text = f"Example: {example['email']}.  Justification: {example.get('justification', 'N/A')}"  # handle missing justification
                texts.append(example_text)
                metadatas.append(
                    {
                        "type": "example",
                        "request_type": request_type,
                        "sub_type": example["sub_type"],
                    }
                )
                ids.append(f"example-{request_type}-{example['sub_type']}")

            # Add attributes for the request type
            attributes_text = f"Attributes for {request_type}: {', '.join(item['attributes'])}"
            texts.append(attributes_text)
            metadatas.append({"type": "attributes", "request_type": request_type})
            ids.append(f"attributes-{request_type}")

        collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids,
        )
        print(f"Vector database created and persisted to {persist_directory}")
    else:
        print(f"Vector database loaded from {persist_directory}")
    return client, collection


def analyze_email(email_content, client, collection, llm):
    """
    Analyzes an email to determine the financial request type, sub-request type,
    and extract relevant attributes using a vector store and LLM.

    Args:
        email_content (str): The text of the email to analyze.
        client (chromadb.Client): The Chroma client.
        collection (chromadb.Collection): The Chroma collection containing financial data.
        llm (ChatOpenAI): An instance of the ChatOpenAI language model.

    Returns:
        dict: A dictionary containing the identified request type, sub-request type,
              and extracted attributes, or None if no match is found.
    """
    # 1.  Embed the email content.
    # embeddings = OpenAIEmbeddings()  # Use the same embeddings model as for the vector store
    # query_embedding = embeddings.embed_query(email_content)

    #query_embedding = get_openrouter_embedding(email_content)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(email_content)

    #print(query_embedding)

    # 2.  Query the vector store to find the most relevant financial request types.
    #     -  We're looking for the closest match to the email's meaning.
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5,  # Get more results to improve context for LLM
    )

    # 3.  Print the results from vectorstore
    print("Vector store query results:")
    print(results)

    # 4.  Use an LLM to analyze the email and extract information.
    #     -  We'll use a prompt that instructs the LLM to:
    #         -  Determine the request type and sub-type.
    #         -  Extract key attributes from the email.
    #         -  Use the context from the vector store results to help.
    best_result_index = 0  # Default, but we might adjust based on LLM
    if not results or not results['ids'] or len(results['ids']) == 0:
        print("No matching financial request type found.")
        return None

    # Get the metadata of all results to provide context to the LLM
    context_data = results['metadatas']

    prompt = PromptTemplate(
        input_variables=["email_content", "context_data"],
        template="""
        You are a financial analyst.
        Analyze the following email to determine the type of financial request and extract relevant information.

        Email Content:
        {email_content}

        Here is context data from a vector database about possible financial request types, sub-types, and attributes:
        {context_data}

        Identify the most likely request type and sub-request type that the email is about.
        Extract the values of the relevant attributes from the email.  Explain your reasoning for the identified request type and sub-request type.

        Return the results as a JSON object with the following keys:
        - request_type: The financial request type.
        - sub_request_type: The sub-request type.
        - justification: Explanation for the sub_request_type.
        - attributes: A dictionary of the extracted attributes and their values.  
                      If an attribute value is not found, use "N/A".

        If you cannot determine the request type or sub-request type, or if no attributes
        are found, return None.
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    # Invoke the chain with the email content and the context data.
    try:
        output = chain.run({
            "email_content": email_content,
            "context_data": context_data,
        })

        # Parse the output as JSON.
        try:
            json_output = json.loads(output)
            return json_output
        except json.JSONDecodeError:
            print(f"LLM output was not valid JSON: {output}")
            return None

    except Exception as e:
        print(f"Error during LLM processing: {e}")
        return None


def runner(email_content):
    """
    Main function to orchestrate the email analysis process.
    """
    load_dotenv()  # Load environment variables from .env

    # 1. Initialize LLM
    llm = ChatOpenAI(
        model_name="openai/gpt-3.5-turbo",  # Choose your desired model from OpenRouter
        openai_api_key="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",  # Pass the API key
        base_url="https://openrouter.ai/api/v1",
    )

    # 2. Load or create the vector store.  Include examples.
    client, collection = load_financial_data(include_examples=True)

    # 3. Example email content to analyze.
    email_content = email_content
    # 4. Analyze the email.
    analysis_result = analyze_email(email_content, client, collection, llm)

    # 5. Print the results.
    if analysis_result:
        print("\nEmail Analysis Result:")
        print(json.dumps(analysis_result, indent=4))
        return json.dumps(analysis_result, indent=4)
    else:
        print("\nFailed to analyze email.")
        return "\nFailed to analyze email."



if __name__ == "__main__":
    email_content = """
    Subject: Urgent Funds Transfer Request

    Dear Sir/Madam,

    Please initiate a transfer of $10,000 from my checking account, account number 1234567890,
    to savings account 9876543210.  I need this transfer completed by the end of business
    on March 15, 2025.  The reference number for this transaction is FT-98765.

    Sincerely,
    John Smith
    """
    print(runner(email_content))
