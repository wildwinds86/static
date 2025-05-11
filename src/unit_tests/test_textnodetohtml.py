import unittest
from textnode import *

class TestTextNodeToHTML(unittest.TestCase):
    def test_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("this is some bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is some bold text")

    def test_link(self):
        node = TextNode("this is link text", TextType.LINK, "https:\\www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is link text")
        self.assertEqual(html_node.props["href"], "https:\\www.google.com")

        

if __name__ == "__main__":
    unittest.main()