import json
import os
import logging
import requests

from bottle import Response, get, post, request, response, route, static_file
from env import data_dir, root_path
from utils import get_db

_db = get_db(os.path.join(data_dir, 'papers.db'))

papers_static_path = os.path.join(root_path, 'frontend/papers-dev/dist')


@post('/papers/add')
def add_paper():
    body = request.body.read()
    body = json.loads(body)
    if _db.add_paper(body):
        body = 'ok'
        code = 200
    else:
        body = 'failed'
        code = 400
    resp = Response(body, status=code)
    return resp


@get('/papers/get_all')
def get_all_paper():
    papers = _db.get_all_papers()
    resp = {'papers': papers}
    response.content_type = 'application/json'
    return json.dumps(resp)


@route('/papers')
def papers_home():
    logging.debug(os.path.join(papers_static_path, 'index.html'))

    return static_file('index.html', root=papers_static_path)


@route('/papers/<filename>')
def papers_file(filename):
    return static_file(filename, root=papers_static_path)


@get('/papers/fetch')
def papers_fetch_remote_url():

    data = request.query.decode()
    try:
        url = request.query['url']
        r = requests.get(url)
        resp = Response(body=r.text, status=r.status_code)
        return resp
    except Exception:
        return Response(body='', status=400)
