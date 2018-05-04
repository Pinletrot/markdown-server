import logging
import os

from bottle import route

from utils import notes_get_html
from utils.env import note_dir


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


@route('/notes/<fn:re:.*\.md>')
def notes_page(fn):
    if fn == 'favicon.ico':
        return ''

    md_fn = os.path.join(note_dir, fn)

    logging.debug('/slides: ' + md_fn)

    return notes_get_html(md_fn)


dummy = 'notes'

__all__ = ['notes_home', 'notes_page', 'dummy']
