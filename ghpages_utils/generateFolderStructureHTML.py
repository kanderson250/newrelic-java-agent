import os
import argparse

js_string = '''
    document.addEventListener('DOMContentLoaded', function() {
    var folders = document.getElementsByClassName('folder-name');

    for (var i = 0; i < folders.length; i++) {
        folders[i].addEventListener('click', function(e) {
        e.stopPropagation();
        this.parentNode.classList.toggle('open');
        });
    }
    });
'''



def generate_folder_structure(path, rootPath):
    html = "<ul>"
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            html += f'<li ><span class="folder-name">{item}</span>'
            html += f'<ul>'
            html += generate_folder_structure(item_path, rootPath)  # Recursively generate subfolders and files
            html += f'</ul>'
            html += f'</li>'
        elif item.endswith('.html'):
            relativePath = os.path.relpath(item_path, rootPath)
            html += f'<li class="file"><a href="{relativePath}">{item}</a></li>'
    html += f'</ul>'
    return html

def writeHTMLFileStructure(rootPath):

    dirName = os.path.dirname(rootPath)
    # Generate the folder-by-folder dropdown HTML structure
    html_structure = generate_folder_structure(rootPath, rootPath)

    # Create the final HTML document with the generated structure
    html_document = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <title>{dirName}</title>
    <style>
        li > ul{{
        display: none;
        }}
        li.open > ul {{
        display: block;
        }}
    </style>
    </head>
    <body>
    <h1>{dirName}</h1>

    {html_structure}

    <script src='collapser.js'></script>
    </body>
    </html>
    '''

    indexFilePath = os.path.join(rootPath, 'index.html')
    jsFilePath = os.path.join(rootPath, "collapser.js")

    # Save the HTML document to a file
    with open(indexFilePath, 'w') as file:
        file.write(html_document)
    
    with open(jsFilePath, 'w') as file:
        file.write(js_string)
        print(jsFilePath)


if __name__ == '__main__':
    # Create an argument parser object
    parser = argparse.ArgumentParser(description='Generate the complete subfolder structure starting from a given directory, and terminating with .html files.')

    # Add command-line arguments
    parser.add_argument('arg1', help='The root path of a folder to index.')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the argument values
    rootPath = args.arg1

    # Call the main function with the argument values
    writeHTMLFileStructure(rootPath)

