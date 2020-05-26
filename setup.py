from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cmdbench',
    url='https://github.com/manzik/cmdbench',
    author='Mohsen Yousefian',
    author_email='me@manzik.com',
    # Needed to actually package something
    packages=['cmdbench'],
    # Needed for dependencies
    install_requires=['numpy', 'psutil>=5.7.0'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Quick and easy benchmark for any command.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)