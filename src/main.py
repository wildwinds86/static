import os
import shutil

from copystatic import copy_files_recursive


dir_path_static = "/home/david/PycharmProjects/static/static"
dir_path_public = "/home/david/PycharmProjects/static/public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()
