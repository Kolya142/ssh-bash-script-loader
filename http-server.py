import config
import os
os.system(f'cd scripts; {config.python_runtime} -m http.server {config.your_port}')