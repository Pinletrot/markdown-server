import os
from env import template_dir

with open(os.path.join(template_dir, 'footer.html')) as f:
    HTML_FOOTER = f.read()

with open(os.path.join(template_dir, 'header.html')) as f:
    HTML_HEADER = f.read()

