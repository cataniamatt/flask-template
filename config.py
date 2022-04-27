import os

# Create a random hash
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'a5909De13719bdfcaCca061adcd1b29b'
	