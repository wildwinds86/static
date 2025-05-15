from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "Paragraph Text"
	HEADING = "Heading Text"
	CODE = "Code Text"
	QUOTE = "Quote Text"
	UNORDERED_LIST = "Unordered List"
	ORDERED_LIST = "Ordered List"


def markdown_to_blocks(markdown):
	blocks = markdown.strip().split("\n\n")

	for b in blocks:
		if b == "":
			blocks.remove(b)

	return blocks