
import json

def py_to_ipynb(py_path, ipynb_path):
    """
    Converts a Python script (.py) to a Jupyter Notebook (.ipynb).
    Each separate block of code (separated by two newlines) is treated as a separate cell.
    """
    # Read the Python script
    with open(py_path, 'r', encoding='utf-8') as f:
        script = f.read()
    
    # Split script into code blocks (using two newlines as separator for cells)
    code_cells = [cell.strip() for cell in script.split('\n\n') if cell.strip()]
    
    # Create notebook structure
    notebook = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    # Add code cells to the notebook
    for code in code_cells:
        cell = {
            "cell_type": "code",
            "metadata": {},
            "source": [line + "\n" for line in code.split('\n')],
            "outputs": [],
            "execution_count": None
        }
        notebook["cells"].append(cell)
    
    # Write to the .ipynb file
    with open(ipynb_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=4)
    
    print(f"Conversion complete: {ipynb_path}")

py_path = "script.py" 
ipynb_path = "notebook.ipynb"
py_to_ipynb(py_path, ipynb_path)
