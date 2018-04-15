import os

ms_encoding = 'utf-8'

root_path = '/'.join(os.path.dirname(__file__).split('/')[:-1])

resource_dir = os.path.join(root_path, 'resources')

template_dir = os.path.join(resource_dir, 'templates')

markdown_dir = os.path.join(resource_dir, 'markdown')

html_dir = os.path.join(resource_dir, 'html')
html_extension = '.html'

css_dir = os.path.join(resource_dir, 'css')
css_name = 'github.css'
css_path = os.path.join(css_dir, css_name)
