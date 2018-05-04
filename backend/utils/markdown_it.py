import codecs
import os

import pystache

from utils.env import template_dir

_template_fn = os.path.join(template_dir, 'notes.html')


def notes_get_html(note_fn):
    with codecs.open(_template_fn) as f:
        template_text = f.read()

    with open(note_fn, 'r') as f:
        text = f.read()

    return pystache.render(template_text, {
        'text': text.lstrip(),
        'title': note_fn.rsplit('/', 1)[1]
    })
