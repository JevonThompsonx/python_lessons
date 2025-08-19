"""
Day 10 c version w/ beautiful soup 
"""

from bs4 import BeautifulSoup
HTML_DOC = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test HTML</title>
</head>
<body>
    <h1>This is a Heading</h1>
    <p class="description">This is a paragraph with a <a href="http://example.com/link1">link</a>.</p>
    <p class="description">This is another paragraph with a <a href="http://example.com/link2">second link</a>.</p>
    <div id="footer">This is the footer.</div>
</body>
</html>
"""


# Create a BeautifulSoup object
soup = BeautifulSoup(HTML_DOC, 'html.parser')

# Extract and print the title
print("Title:", soup.title)

# Extract and print the heading
print("Heading:", soup.h1)

# Extract and print the paragraph
print("Paragraph:", soup.p)
