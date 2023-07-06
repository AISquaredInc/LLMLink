from setuptools import setup
from chainlink import __version__

with open('requirements.txt', 'r') as f:
    requirements = [line for line in f.read().splitlines() if line]

setup(
    name='chainlink',
    version=__version__,
    packages=[
        'chainlink',
        'chainlink.app',
        'chainlink.model'
    ],
    description = 'Chainlink is a Python package that allows users to easily create LLM-powered Gradio applications',
    long_description=open('README.md', 'r').read(),
    author = 'Jacob Renn',
    author_email = 'jacob.renn@squared.ai',
    url = 'https://github.com/jacobrenn/chainlink.git'
)
