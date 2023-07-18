import pdfkit

# with open('index.html', 'rb') as f:
pdfkit.from_file(
    'index.html',
    'test.pdf',
    options={"enable-local-file-access": ""},
    css=['style.css']
)
