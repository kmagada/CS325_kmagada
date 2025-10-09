import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from typing import List

# Load .env file for the api key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embeddings_from_json(file_path: str, model="text-embedding-3-small"):
    """
    Reads a JSON file containing a list of strings,
    generates embeddings, and returns the vector list.
    """
    # Load JSON content
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ensure it's a list of strings
    if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
        raise ValueError("JSON file must contain a list of strings")

    # Get embeddings in one request (faster than looping)
    response = client.embeddings.create(
        input=data,
        model=model
    )

    # Vectors
    embeddings = [item.embedding for item in response.data]
    return embeddings


def main(file_path: str):
    embeddings = get_embeddings_from_json(file_path)
    print(f"Loaded {len(embeddings)} embeddings.")
    print("First embedding example:", embeddings[0][:10])  # print only first 10 values for preview


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
