import logging
import os

from bottle import route

from utils import remark
from utils.env import slide_dir


@route('/slides')
def slides_home():
    html = ''
    for folder, _, fs in os.walk(slide_dir, followlinks=True):
        folder = folder[len(slide_dir) + 1:]
        for f in fs:
            if 'md' in f:
                if folder == '':
                    path = 'slides/{}'.format(f)
                else:
                    path = 'slides/{}/{}'.format(folder, f)
                html += '<a href={}>{}</a><br>\n'.format(path, f)

    return html


@route('/slides/<resource:re:.*\.md>')
def slides_page(resource):
    md_fn = os.path.join(slide_dir, resource)

    logging.debug('/slides: ' + md_fn)

    return remark.get_html(md_fn)


dummy = 'slides'

__all__ = ['slides_home', 'slides_page', 'dummy']
