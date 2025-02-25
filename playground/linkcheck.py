import re
import requests
from typing import List, Tuple
import sys

def check_markdown_links(markdown_text: str, timeout: int = 5) -> List[Tuple[str, str]]:
    """
    Extracts all Markdown links from the given text and checks their validity.

    Parameters:
        markdown_text (str): The Markdown content as a string.
        timeout (int): The timeout for HTTP requests in seconds. Default is 5 seconds.

    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple contains the URL and its status.
                               Status is 'OK' for successful requests or the error message for failures.
    """
    # Regular expression to find Markdown links: [text](URL)
    link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\s)]+)\)')
    links = link_pattern.findall(markdown_text)

    results = []

    for text, url in links:
        print(f"Checking link: {url}")
        try:
            response = requests.head(url, allow_redirects=True, timeout=timeout)
            if response.status_code == 200:
                status = 'OK'
            else:
                status = f'Error {response.status_code}'
        except requests.exceptions.RequestException as e:
            status = f'Failed: {e}'
        
        results.append((url, status))
    
    return results


def main():
    if len(sys.argv) < 2:
        print("Please provide the Markdown file as an argument.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as file:
            markdown_text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    results = check_markdown_links(markdown_text)

    for url, status in results:
        print(f"{url}: {status}")


if __name__ == "__main__":
    main()
