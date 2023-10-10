import yaml

from forwardgram import start

with open('config.yml', 'rb') as f:
    config = yaml.safe_load(f)
start(config)
