import os

from bottle import route, static_file

from utils import MarkdownConverter
from utils.env import note_dir, root_path, data_dir

converter = MarkdownConverter(data_dir, note_dir)


@route('/notes')
def notes_home():
    html = ''
    for folder, _, fs in os.walk(note_dir, followlinks=True):
        folder = folder[len(note_dir) + 1:]
        for f in fs:
            if 'md' in f:
                if folder == '':
                    path = 'notes/{}'.format(f)
                else:
                    path = 'notes/{}/{}'.format(folder, f)
                html += '<a href={}>{}</a><br>\n'.format(path, f)

    return html


@route('/notes/<resource:re:.*\.md>')
def notes_page(resource):
    if resource == 'favicon.ico':
        return ''

    html_file_name = converter.convert(resource)
    path = os.path.join(data_dir, html_file_name)
    path = path[len(root_path):]
    if path[0] in ['/', '\\']:
        path = path[1:]

    return static_file(path, root=root_path)


dummy = 'notes'

__all__ = ['notes_home', 'notes_page', 'dummy']
