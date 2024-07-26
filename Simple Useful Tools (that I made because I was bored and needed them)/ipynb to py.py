
# A simple regex based .ipynb to .py converter #

import re
import json

def ipynb_to_py(ipynb_path, py_path):
    # Reading the .ipynb file
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Initializing a list to hold the code lines
    code_lines = []

    # Regex pattern to match code cells
    code_cell_pattern = re.compile(r'\"cell_type\": \"code\".*?\"source\": \[(.*?)\]', re.DOTALL)

    # Iterating over all cells
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Extract the code lines
            source = ''.join(cell['source'])
            code_lines.append(source + '\n\n')

    # Write the extracted code to a .py file
    with open(py_path, 'w', encoding='utf-8') as f:
        f.writelines(code_lines)

# Usage
ipynb_path = 'path/to/your/notebook.ipynb'
py_path = 'path/to/output/script.py'
ipynb_to_py(ipynb_path, py_path)
