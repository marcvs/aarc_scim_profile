#!/usr/bin/env python3

import os
import sys
import json
try:
    from scimschema import validate
    from scimschema._model.model import Model
except ImportError:
    print ("""Unable to find python lib 'schimschema'
Please run these command from the folder that also contains the `.git` folder
for this repository:
        git submodule init
        git submodule update
        export PYTHONPATH=`pwd`/schimschema   # (recommended)
""")
    sys.exit(2)

def load_json_schema(filename):
    '''directly load a schema by filename'''
    with open(filename) as f:
        schema = Model.load(f)
    return {schema.id: schema}

def load_json_data(filename):
    '''load and parse json'''
    with open(filename) as f:
        data = f.read()
    try:
        obj = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print(F"Error when decoding JSON:\n{e}")
        sys.exit(4)
    return obj

aarc_schema_file = "AARC_Schema_Parseable.json"
aarc_scim_file   = "AARC_SCIM_Example.json"

if not os.path.exists(aarc_schema_file):
    print ("""Cannot find AARC_Schema_Parseable.json.
Please create it by running:
        ./make_parseable.sh""")
    sys.exit(3)

scim_schema = load_json_schema(aarc_schema_file)
scim_data   = load_json_data  (aarc_scim_file)

try:
    validate(data=scim_data, extension_schema_definitions=scim_schema)
except Exception as e:
    print(e)
    sys.exit(1)
print("No news is good news. I.e. your validation worked")
