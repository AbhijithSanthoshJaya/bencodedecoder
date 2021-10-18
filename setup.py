from setuptools import setup, find_packages

setup(
    name='bencode-decoder',
    version='0.0.1',

    description="Bencoded data Decoder package",
    long_description=open('README.md').read(),
    license='GPLv2',
    url= 'https://github.com/AbhijithSanthoshJaya/bencode-decoder',
    author='Abhijith Santhosh Jaya',
    author_email='abhijithsj100@gmail.com',

    packages=find_packages(
        exclude=['tests']
    ),

    test_suite='tests',

    # install_requires=[
        
    # ],

    # tests_require=[
        
    # ],

    entry_points={
        'console_scripts': [
        ]
    },
)
