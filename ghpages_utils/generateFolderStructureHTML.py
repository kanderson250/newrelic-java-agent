import os
import argparse


def generate_folder_structure(path):
    html = ""
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            html += f'<div class="folder">'
            html += f'<div class="folder-name">{item}</div>'
            html += generate_folder_structure(item_path)  # Recursively generate subfolders and files
            html += f'</div>'
        elif item.endswith('.html'):
            html += f'<div class="file"><a href="{item_path}">{item}</a></div>'
    return html

def writeHTMLFileStructure(rootPath, destinationPath):

    # Generate the folder-by-folder dropdown HTML structure
    html_structure = generate_folder_structure(rootPath)

    # Create the final HTML document with the generated structure
    html_document = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>File Structure</title>
    <style>
        .folder {{
        padding-left: 20px;
        }}
        .folder-name {{
        cursor: pointer;
        }}
        .file {{
        padding-left: 40px;
        }}
    </style>
    </head>
    <body>
    <h1>File Structure</h1>

    {html_structure}

    </body>
    </html>
    '''

    # Save the HTML document to a file
    with open(destinationPath, 'w') as file:
        file.write(html_document)


if __name__ == '__main__':
    # Create an argument parser object
    parser = argparse.ArgumentParser(description='Description of your script')

    # Add command-line arguments
    parser.add_argument('arg1', help='The root path of a folder to index.')
    parser.add_argument('arg2', help='The destination path to write to, terminating in an html file.')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the argument values
    arg1_value = args.arg1
    arg2_value = args.arg2

    # Call the main function with the argument values
    writeHTMLFileStructure(arg1_value, arg2_value)
