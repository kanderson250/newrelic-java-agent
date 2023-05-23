import os
import argparse
from bs4 import BeautifulSoup

def getFailures(root_path):
    failCount = 0
    failingTests = ""
    passingTests = ""

    #check results for each test suite
    for folder in os.listdir(root_path):
        summary_path = os.path.join(root_path, folder, 'build', 'reports', 'tests', 'test', 'index.html')
        if os.path.exists(summary_path):
            relative_path = os.path.relpath(summary_path, root_path)
            test_item = f"<li><a href='{relative_path}'>{relative_path}</a></li>"
            with open(summary_path, 'r') as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                failures = soup.find(id='failures')
                if failures and '0' not in failures.get_text().strip():
                    failCount += 1
                    failingTests += test_item
                else:
                    passingTests += test_item

    html_string = f'''
      <!DOCTYPE html>
      <html>
      <head>
      <title>Unit Test Results</title>
      <style>
        #failing li {{
            color: red
        }}
        #passing li {{
            color: green
        }}
      </style>
      </head>
      <body>
      <h1>Unit Test Results</h1>
      <div id = 'failing'><h2>Failing Test Suites</h2>
          <ul> {failingTests} </ul>
      </div>
      <div id='passing'> <h2>Passing Test Suites</h2>
          <ul> {passingTests} </ul>
      </div>
      </body>
      </html>
      '''
    index_path = os.path.join(root_path, 'index.html')
    with open(index_path, 'w') as index_file:
        index_file.write(html_string)
    print(f'Test reports published to {root_path} with {failCount} failing suites.')

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
    getFailures(arg1_value)