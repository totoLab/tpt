import sys
import pypandoc

def todo():
    return print_return_error("Not yet implemented.")

def print_return_error(err):
    print(err)
    return err

def from_docx(filepath):
    output = pypandoc.convert_file(filepath, 'plain')
    if output is None or output == "":
        print("ERR: empty output.")
        return "Empty file."
    return output

def from_doc(filepath):
    return from_docx(filepath)

def from_pdf(filepath):
    return todo()

def from_plain_text(filepath):
    with open(filepath, "r") as f:
        output = f.read()
    
    if output is None or output == "":
        return print_return_error(f"Error gathering text from {filepath}.")

    return output

def get_content(filepath):
    print(filepath)
    parts = filepath.split(".")
    ext = parts[len(parts) - 1]

    if ext == "txt":
        return from_plain_text(filepath)
    elif ext == "pdf":
        return from_pdf(filepath)
    elif ext == "docx":
        return from_docx(filepath)
    elif ext == "doc":
        return from_doc(filepath)
    else:
        return print_return_error(f"Extension {ext} is not yet supported.")
        