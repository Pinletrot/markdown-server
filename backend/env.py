import os

root_path = '/'.join(os.path.dirname(__file__).split('/')[:-1])
resource_dir = os.path.join(root_path, 'resources')
markdown_dir = os.path.join(resource_dir, 'markdown')
html_dir = os.path.join(root_path, 'temp')

