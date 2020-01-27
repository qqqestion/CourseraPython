import sys
import json
import os
import tempfile
from os import path
from collections import OrderedDict


def add_field(filename, key, value):
    with open(filename, 'r') as fin:
        json_elems = json.loads(fin.read())
        elements = dict(json_elems)
        if key not in elements:
            elements[key] = [value]
        else:
            elements[key].append(value)
    with open(filename, 'w') as fout:
        fout.write(json.dumps(elements))


def print_field(filename, key):
    with open(filename, 'r') as fin:
        json_elems = json.loads(fin.read())
        elements = dict(json_elems)
        if key in elements:
            print(', '.join(elements[key]))
        else:
            print('')


# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
storage_path = '../files/json.txt'
if not path.exists(storage_path):
    file = open(storage_path, 'w')
    file.write('{}')
    file.close()
args = sys.argv[1:]
if len(args) == 2 and args[0] == '--key':
    print_field(storage_path, args[1])
else:
    add_field(
        storage_path,
        args[args.index('--key') + 1],
        args[args.index('--val') + 1]
    )
