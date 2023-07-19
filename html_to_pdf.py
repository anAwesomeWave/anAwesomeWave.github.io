import pdfkit

# with open('index.html', 'rb') as f:
html = './docs/index.html'
base_css = './docs/css/'
css = [
    base_css + 'bootstrap.min.css',
    base_css + 'style.css',
    # base_css + 'dark.css',
]
pdfkit.from_file(
    html,
    'test.pdf',
    options={
        "enable-local-file-access": "",
        "page-size": "A4",
        "page-width": "1920",
        "page-height": "1080",
        "margin-left": '0',
        "margin-right": '0',
        "margin-top": '0',
        "margin-bottom": '0',
        "disable-smart-shrinking": "",
    },
    css=css
)
