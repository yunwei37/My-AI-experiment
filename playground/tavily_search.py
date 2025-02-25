import os
import sys
import json
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables from .env file
load_dotenv()

def tavily_search(query):
    # Instantiating your TavilyClient
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Executing a search query
    response = tavily_client.search(query, 
                                    include_images=True, 
                                    include_answer=True, 
                                    search_depth="advanced", 
                                    include_image_descriptions=True)
    return response

def main():
    if len(sys.argv) != 3:
        print("Usage: python tavily_search.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f:
            query = f.read().strip()

        response = tavily_search(query)

        with open(output_file, 'w') as f:
            json.dump(response, f, indent=2)

        print(f"Search results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
