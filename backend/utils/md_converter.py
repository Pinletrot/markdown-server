import codecs
import os
import sys

import markdown as md
from mdx_gfm import GithubFlavoredMarkdownExtension as gfme

from .md_templates import HTML_FOOTER, HTML_HEADER

markdown_extensions = [gfme(), 'mdx_math']
html_extension = '.html'
ms_encoding = 'utf-8'


class MarkdownConverter(object):
    def __init__(self, temp_dir, note_dir):
        self.html_header = HTML_HEADER
        self.html_footer = HTML_FOOTER

        self.temp_dir = temp_dir
        self.note_dir = note_dir

    def convert(self, src, dst=""):
        code = md.markdown(self.read_md(src), extensions=markdown_extensions)

        return self.write_html(code, src, dst)

    def read_md(self, file_name):
        with codecs.open(
                os.path.join(self.note_dir, file_name),
                encoding=ms_encoding,
                mode='r') as md_file:
            md = md_file.read()

        return md

    def write_html(self, body, file_name, dst):
        html_path = os.path.join(self.temp_dir, file_name + html_extension)

        if dst != "":
            html_path = dst
        try:
            os.makedirs('/'.join(html_path.replace('\\', '/').split('/')[:-1]))
        except OSError as exc:
            pass

        with codecs.open(html_path, encoding=ms_encoding, mode='w') as f:
            f.write(self.html_header + body + self.html_footer)

        return html_path
