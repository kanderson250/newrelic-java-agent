import os
import argparse

def generate_folder_structure(path):
    html = ""
    html += f'<ul>'
    for item in os.listdir(path):
        html += f'<li class="file"><a href="{item}">{item}</a></li>'
    html += f'</ul>'
    return html

def writeHTMLIndexFileStructure(rootPath):

    # Generate the folder-by-folder dropdown HTML structure
    html_structure = generate_folder_structure(rootPath)
    dirName = os.path.basename(rootPath)

    # Create the final HTML document with the generated structure
    html_document = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>{dirName}</title>
    </head>
    <body>
    <h1>{dirName}</h1>

    {html_structure}
    </body>
    </html>
    '''

    indexPath = os.path.join(rootPath, 'index.html')
    # Save the HTML document to a file
    with open(indexPath, 'w') as file:
        file.write(html_document)


if __name__ == '__main__':
    # Create an argument parser object
    parser = argparse.ArgumentParser(description='Description of your script')

    # Add command-line arguments
    parser.add_argument('arg1', help='The root path of a folder to index.')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the argument values
    arg1_value = args.arg1

    # Call the main function with the argument values
    writeHTMLIndexFileStructure(arg1_value)
