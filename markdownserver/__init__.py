from bottle import route, run, template, static_file
from md_converter import MarkdownConverter
from env import *
import os

converter = MarkdownConverter()


@route('/')
def homepage():
    return 'hello'


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
    run(host=ms_host, port=ms_port, debug=ms_debug, reloader=ms_reloader)


if __name__ == '__main__':
    main()
