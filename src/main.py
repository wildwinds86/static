import os
import shutil
from generate_page import generate_pages_recursive
from copystatic import copy_files_recursive
from sys import argv

if len(argv) > 1:
    basepath = argv[1]
else:
    basepath = "/"

dir_path_static = r"../static"
dir_path_docs = r"../docs"
dir_path_content = r"../content"
file_path_template = r"../template.html"


def main():
    if os.path.exists(dir_path_docs):
        print("Deleting public directory...")
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_pages_recursive(dir_path_content, file_path_template, dir_path_docs, basepath)

main()
