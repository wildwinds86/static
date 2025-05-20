import os
import shutil
from inline_markdown import *
from htmlnode import *
from markdown_blocks import *
from textnode import *

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


#print(os.path.dirname(r"../public/index.html"))
generate_page(r"../content/index.md", r"../template.html", "../public/index.html")