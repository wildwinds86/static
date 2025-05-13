import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("<p>", "Small paragraph", None, {'href': 'not a link', 'target': '_blank', 'src': 'not a sauce'})
        print(node.props_to_html())

    def test_repr(self):
        node = HTMLNode("<p>", "Small paragraph", None, {'href': 'not a link', 'target': '_blank'})
        print(node)

    def test_child_node(self):
        child_node = HTMLNode("<p>", "Small paragraph", None, {'href': '"not a link"', 'target': '_blank'})
        parent_node = HTMLNode("<html>", "HTML root", child_node, {'href': '"not a link"', 'target': '_blank'})
        #print(parent_node)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a","This Link", {"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<a href='www.google.com' target='_blank'>This Link</a>")

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "This Image", {"src": "/img.gif"})
        self.assertEqual(node.to_html(), "<img src='/img.gif'>This Image</img>")

    def test_no_tag(self):
        node = LeafNode(None, "This Image", {"src": "/img.gif"})
        self.assertEqual(node.to_html(), "This Image")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


if __name__ == "__main__":
    unittest.main()