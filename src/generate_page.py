import os
from inline_markdown import *
from markdown_blocks import *


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")

    f = open(from_path, "r")
    content_md = f.read()
    f.close()

    f = open(template_path, "r")
    template_html = f.read()
    f.close()

    html_str = markdown_to_html_node(content_md).to_html()
    title = extract_title(content_md)

    html_page = template_html.replace(r"{{ Title }}", title)
    html_page = html_page.replace(r"{{ Content }}", html_str)

    if os.path.exists(dest_path):
        raise FileExistsError(f"{dest_path} already exists")

    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))

    f = open(dest_path, "x")
    f.write(html_page)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        print(f"Creating directory {dest_dir_path}")

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        #print(f" * {from_path} -> {dest_path}")

        if os.path.isfile(from_path):
            html_file_path = os.path.splitext(dest_path)[0] + ".html"
            print(f"Generating html page from {from_path} to {html_file_path}")
            generate_page(from_path, template_path, html_file_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
