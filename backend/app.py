import logging

from bottle import run, route

import notes_api
import papers_api
import slides_api


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


@route('/')
def homepage():
    dummies = [notes_api.dummy, papers_api.dummy, slides_api.dummy]

    html = ''
    for dummy in dummies:
        html += f'<p><a href="/{dummy}">{dummy}</a><p>'

    return html


if __name__ == '__main__':
    main()
