from bottle import route, run, template, static_file
from md_converter import MarkdownConverter
from env import *
import os

converter = MarkdownConverter()


@route('/')
def homepage():
    html = ''
    for folder, _, fs in os.walk(markdown_dir, followlinks=True):
        folder = folder[len(markdown_dir) + 1:]
        for f in fs:
            if 'md' in f:
                html += f'<a href={folder}/{f}>{f}</a><br>\n'

    return html


@route('/<resource:re:.*\.md>')
def gfmize(resource):
    if resource == 'favicon.ico':
        return ''

    html_file_name = converter.convert(resource)
    path = os.path.join(html_dir, html_file_name)
    path = path[len(root_path):]
    if path[0] in ['/', '\\']:
        path = path[1:]

    return static_file(path, root=root_path)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', type=int, default=5901)
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--live_reload', action='store_true')

    args = parser.parse_args()

    run(host=args.host,
        port=args.port,
        debug=args.debug,
        reloader=args.live_reload)


if __name__ == '__main__':
    main()
