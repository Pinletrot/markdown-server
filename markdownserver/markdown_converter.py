import codecs
import os
import sys

import markdown as md
from env import css_path, ms_encoding, markdown_dir, html_dir, html_extension
from mdx_gfm import GithubFlavoredMarkdownExtension as gfme

HTML_HEADER = '''
<html>
<head>
<style type='text/css'>
<!--
''' + codecs.open(css_path, encoding=ms_encoding, mode='r').read() + \
'''
//-->
</style>
<script
    type="text/javascript"
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js">
</script>
</head>
<body>
<div class='markdown-body'>
'''
HTML_FOOTER = '''
</div>
</body>
</html>
'''


class MarkdownConverter(object):
    def __init__(self):
        self.html_header = HTML_HEADER
        self.html_footer = HTML_FOOTER

    def convert(self, src, dst=""):
        code = md.markdown(self.read_md(src), extensions=[gfme()])

        return self.write_html(code, src, dst)

    def read_md(self, file_name):
        md_file = codecs.open(
            os.path.join(markdown_dir, file_name),
            encoding=ms_encoding,
            mode='r')

        return md_file.read()

    def write_html(self, body, file_name, dst):
        html_path = os.path.join(html_dir, file_name + html_extension)

        if dst != "":
            html_path = dst
        try:
            os.makedirs('/'.join(html_path.replace('\\', '/').split('/')[:-1]))
        except OSError as exc:
            pass

        html_file = codecs.open(html_path, encoding=ms_encoding, mode='w')
        html_file.write(self.html_header + body + self.html_footer)

        return html_path


if __name__ == '__main__':
    converter = MarkdownConverter()
    print(converter.convert('notes/quick.md'))
