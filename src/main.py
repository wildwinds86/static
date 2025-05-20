import os
import shutil
from generate_page import generate_page

from copystatic import copy_files_recursive


dir_path_static = r"../static"
dir_path_public = r"../public"
dir_path_content = r"../content"
file_path_template = r"../template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_page(dir_path_static, file_path_template, dir_path_public)
main()
