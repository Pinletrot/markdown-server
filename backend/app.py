import logging
import os

from bottle import route, run, static_file, template
from env import *
from notes_api import notes_home, notes_page
from paper_api import add_paper


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', type=int, default=5901)
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--live_reload', action='store_true')

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG if args.debug else logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    run(host=args.host,
        port=args.port,
        debug=args.debug,
        reloader=args.live_reload)


if __name__ == '__main__':
    main()
