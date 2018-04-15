import os

root_path = '/'.join(os.path.dirname(__file__).split('/')[:-1])
note_dir = os.path.join(root_path, 'notes')
temp_dir = os.path.join(root_path, 'temp')

