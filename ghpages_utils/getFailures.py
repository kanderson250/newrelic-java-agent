import os
import argparse
from bs4 import BeautifulSoup

def generate_index_file(root_path):
    index_path = os.path.join(root_path, 'index.html')

    with open(index_path, 'w') as index_file:
        index_file.write("<html><body><h1>Test Reports</h1><ul>")

        for root, _, files in os.walk(root_path):
            for filename in files:
                if filename.endswith('.html'):
                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, root_path)

                    with open(file_path, 'r') as html_file:
                        soup = BeautifulSoup(html_file, 'html.parser')
                        failures = soup.find(id='failures')

                        if failures and '0' not in failures.get_text().strip():
                            index_file.write(f"<li><a href='{relative_path}'>{relative_path}</a></li>")

        index_file.write("</ul></body></html>")

# Usage example

if __name__ == '__main__':
    # Create an argument parser object
    parser = argparse.ArgumentParser(description='Description of your script')

    # Add command-line arguments
    parser.add_argument('arg1', help='The root path of a folder to get all html files containing failure messages')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the argument values
    arg1_value = args.arg1

    # Call the main function with the argument values
    generate_index_file(arg1_value)