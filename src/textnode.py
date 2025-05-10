from enum import Enum

class TextType(Enum):
    NORMAL = "Normal Text"
    BOLD = "Bold Text"
    ITALIC = "Italic Text"
    CODE = "Code Text"
    LINK = "Link"
    IMAGE = "Image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return self.text == text_node.text and self.text_type.value == text_node.text_type.value and self.url == text_node.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
