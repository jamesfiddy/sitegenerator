import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node_italics = TextNode("This is an text node", TextType.ITALIC)
        self.assertNotEqual(node_italics, node)

        node_url = TextNode("This is a url", TextType.LINK, "http://www.google.com")
        node_url2 = TextNode("This is a url", TextType.LINK)
        self.assertNotEqual(node_url, node_url2)

        node_image = TextNode("This is an image", TextType.IMAGE)
        self.assertNotEqual(node, node_image)

if __name__ == "__main__":
    unittest.main()