import os

from bottle import route, static_file

from env import markdown_dir, html_dir, root_path
from md_converter import MarkdownConverter


@route('/notes')
def notes_home():
    html = ''
    for folder, _, fs in os.walk(markdown_dir, followlinks=True):
        folder = folder[len(markdown_dir) + 1:]
        for f in fs:
            if 'md' in f:
                html += f'<a href={folder}/{f}>{f}</a><br>\n'

    return html


@route('/notes/<resource:re:.*\.md>')
def notes_page(resource):
    if resource == 'favicon.ico':
        return ''

    converter = MarkdownConverter()
    html_file_name = converter.convert(resource)
    path = os.path.join(html_dir, html_file_name)
    path = path[len(root_path):]
    if path[0] in ['/', '\\']:
        path = path[1:]

    return static_file(path, root=root_path)
