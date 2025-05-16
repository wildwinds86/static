from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "Paragraph Text"
	HEADING = "Heading Text"
	CODE = "Code Text"
	QUOTE = "Quote Text"
	UNORDERED_LIST = "Unordered List"
	ORDERED_LIST = "Ordered List"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks