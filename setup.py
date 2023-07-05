from setuptools import setup
from chainlink import __version__

with open('requirements.txt', 'r') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name = 'chainlink',
    version = __version__,
    packages = [
        'chainlink',
        'chainlink.app',
        'chainlink.model'
    ]
)
