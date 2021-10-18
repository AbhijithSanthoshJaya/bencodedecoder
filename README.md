# Bencode Decoder Module

A Python library that decodes a valid Bencoded data input. The module supports all 4 bencode data types.

## Installation

package_git_repo_url = https://github.com/AbhijithSanthoshJaya/bencodedecoder.git

Note: Kindly make a new virtual environment bprior to installation

To install use the package manager pip:
pip install git+[package_git_repo_url]

Ensure the package is installed correctly using pip list and shows up as bencodedDecoder

## Usage

```python

import bencodeDecoder
from bencodeDecoder import decoder as bencode
# enter integer encoded input --> "i42e"
bencode.decode("i45e")
# result 45

# enter  encoded list input --> "l3:abc4:xyzei35ee"
bencode.decode("l3:abc4:xyzei35ee")
# result ['abc', 'xyze', 35]

# enter  encoded string input --> "5:lover"
bencode.decode("5:lover")
# result "lover

# enter  encoded dictionary input --> "d4:kitei42e3:tri4:spame"
bencode.decode("d4:kitei42e3:tri4:spame")
# result {'kite': 42, 'tri': spam}

```

## Testing

1. Clone the repo in your dev environment.
2. make a virtual environment in the root directory ( python -m env /path/to/environment)
3. activate environment( cd environment; source Scripts/Activate)
4. Change directory to 'tests'
5. pip install nose2
6. run nose2
7. Ensure All test cases Pass( Status: OK)
