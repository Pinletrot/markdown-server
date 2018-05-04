import os

root_path = '/'.join(os.path.dirname(__file__).split('/')[:-2])
tmp_dir = os.path.join(root_path, '.tmp')
data_dir = os.path.join(root_path, 'data')
note_dir = os.path.join(data_dir, 'notes')
slide_dir = os.path.join(data_dir, 'slides')
template_dir = os.path.join(data_dir, 'templates')
