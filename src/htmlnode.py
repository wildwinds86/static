class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props: 
            return ""

        properties = " "
        for p in self.props.items():
            properties += f"{p[0]}='{p[1]}' "
        return properties.rstrip()
    
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if not self.value or self.value == "": raise ValueError("Value is a required parameter!")

        if not self.tag:
            return str(self.value)
        
        properties = ""
        if self.props: properties = self.props_to_html()

        return f"<{self.tag}{properties}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag: raise ValueError("Tag is a required parameter!")
        if self.children is None: 
            raise ValueError("Children can not be None for a ParentNode")

        properties = ""
        if self.props:
            properties = self.props_to_html()
        
        html_string = f"<{self.tag}{properties}>"
        for c in self.children:
            html_string += f"{c.to_html()}"

        return f"{html_string}</{self.tag}>"