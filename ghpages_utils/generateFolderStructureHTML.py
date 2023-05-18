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

def generate_folder_structure(path):
    html = ""
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            html += f'<ul>'
            html += f'<li ><span class="folder-name">{item}</span>'
            html += generate_folder_structure(item_path)  # Recursively generate subfolders and files
            html += f'</li>'
            html += f'</ul>'
        elif item.endswith('.html'):
            html += f'<li class="file"><a href="{item_path}">{item}</a></li>'
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
        .file {{
        margin-left: 5%
        }}
        li > ul{{
        display: none;
        }}
        li.open > ul {{
        display: block;
        }}
    </style>
    </head>
    <body>
    <h1>File Structure</h1>

    {html_structure}

    <script src='myJavascript.js'></script>
    </body>
    </html>
    '''

    parDir = os.path.dirname(destinationPath)
    jsFilePath = os.path.join(parDir, "myJavascript.js")

    # Save the HTML document to a file
    with open(destinationPath, 'w') as file:
        file.write(html_document)
    
    with open(jsFilePath, 'w') as file:
        file.write(js_string)
        print(jsFilePath)


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
