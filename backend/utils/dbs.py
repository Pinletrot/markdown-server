import logging
from collections import namedtuple
from typing import Dict, List

from tinydb import Query, TinyDB


class PaperDB:

    def __init__(self, db_file_path):
        self._db = TinyDB(db_file_path)

    @property
    def n_papers(self):
        q = Query()
        docs = self._db.search(q.type == 'paper_item')
        return len(docs)

    def contains(self, title, url):
        q = Query()
        docs = self._db.search((q.type == 'paper_item') & (q.title == title) &
                               (q.url == url))
        return len(docs) != 0

    def add_paper(self, post_body):
        try:
            title = post_body['title']
            url = post_body['url']
        except KeyError:
            logging.debug('key error:' + str(post_body))
            return False

        if self.contains(title, url):
            logging.debug('duplicated')
            return

        pdf_url = post_body.get('pdf_url', '')
        self._db.insert({
            'type': 'paper_item',
            'title': title,
            'url': url,
            'authors': post_body['authors'],
            'pdf_url': pdf_url,
            'uid': self.n_papers + 1,
            'tags': []
        })

    def get_all_papers(self) -> List[Dict]:
        q = Query()
        docs = self._db.search(q.type == 'paper_item')
        return [{
            k: doc[k]
            for k in ['title', 'tags', 'url', 'pdf_url', 'authors']
        }
                for doc in docs]


def get_db(db_file_path) -> PaperDB:
    return PaperDB(db_file_path)
