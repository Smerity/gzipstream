from setuptools import setup, find_packages

setup(
    name='gzipstream',
    version='0.1.0',
    author='Smerity',
    author_email='smerity@smerity.com',
    packages=['gzipstream', 'gzipstream.tests'],
    scripts=[],
    url='https://github.com/Smerity/gzipstream',
    license='LICENSE',
    description='gzipstream allows Python to process multi-part gzip files from a streaming source',
    long_description=open('README.md').read(),
    test_suite='gzipstream.tests'
)
