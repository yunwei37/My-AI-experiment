import os
import json
import openai
import argparse
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
model_name = os.getenv('OPENAI_MODEL_NAME')
if not model_name:
    model_name = "gpt-4o"
temperature = os.getenv('OPENAI_TEMPERATURE')
if not temperature:
    temperature = 0.7
client = OpenAI()

def read_file(file_path):
    """Read the content of the input file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Write the content to the output file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def ai_generate_content(content, schema):
    """Send the prompt and content to OpenAI's API and get the structured content."""

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that generates structured output based on the following JSON schema: {json.dumps(schema)}"},
            {"role": "user", "content": content}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "response",
                "schema": schema,
                "strict": True
            }
        }
    )

    return json.loads(completion.choices[0].message.content)

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Generate a structured version of a text file using OpenAI's GPT-4."
    )
    parser.add_argument('input_file', help='Path to the input .txt file')
    parser.add_argument('output_file', help='Path to save the structured output file')
    parser.add_argument('schema_file', help='Path to the JSON schema file')

    args = parser.parse_args()

    try:
        # Read input file
        input_content = read_file(args.input_file)

        # Read schema file
        schema = json.loads(read_file(args.schema_file))

        # Generate structured content
        structured_content = ai_generate_content(input_content, schema)

        # Write to output file
        write_file(args.output_file, json.dumps(structured_content, indent=2))

        print(f"Successfully processed '{args.input_file}' and saved structured output to '{args.output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
