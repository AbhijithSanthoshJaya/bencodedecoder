# Bencode Decoder Module

A Python library that decodes a valid Bencoded data input. The module supports all 4 bencode data types.

## Installation

package_git_repo_url = https://github.com/AbhijithSanthoshJaya/bencodedecoder.git

Use the package manager pip:
pip install git+[package_git_repo_url]

Ensure

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

# enter  encoded string input --> ""
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
