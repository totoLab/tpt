#!/usr/bin/env python3

import to_plain_text as tpt
from flask import Flask, render_template, g 
import sys, os
from os.path import isfile, join

program_directory = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(program_directory, "templates")
app = Flask(__name__, template_folder=template_dir)

def get_filenames_from_root(file_root):
    filenames = []
    for root, dirs, files in os.walk(file_root):
        for filename in files:
            filepath = os.path.join(root, filename)
            if isfile(filepath):
                relative_path = os.path.relpath(filepath, file_root)
                filenames.append(relative_path)
    return filenames

@app.before_request
def before_request():
    g.file_directory = os.path.abspath(file_directory)
    g.filenames = get_filenames_from_root(g.file_directory)

@app.route('/')
def index():
    return render_template('index.html', filenames=g.filenames)

@app.route('/file/<path:filename>')
def display_content(filename):
    filepath = os.path.join(g.file_directory, filename)  # Create the full path using the directory and filename
    print(f"Trying to display content of {filepath}")
    content = tpt.get_content(filepath)
    return render_template('content.html', title=filename, filenames=g.filenames, content=content)

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        relative_root = args[1]

        file_directory = os.path.abspath(relative_root)
        app.run(port=8081)
    else:
        print("Can't start the server, no relative root for indexing specified.")
