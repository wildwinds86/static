import os
import shutil
from generate_page import generate_page, generate_pages_recursive
from copystatic import copy_files_recursive


dir_path_static = r"../static"
dir_path_public = r"../public"
dir_path_content = r"../content"
file_path_template = r"../template.html"


def main():
    if os.path.exists(dir_path_public):
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    #generate_page(dir_path_content + "/index.md", file_path_template, dir_path_public + "/index.html")
    generate_pages_recursive(dir_path_content, file_path_template, dir_path_public)

main()
