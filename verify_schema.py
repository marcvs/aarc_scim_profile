#!/usr/bin/env python3
"""script to verify a SCIM resource against a (set of) SCIM schemas"""

import os
import sys
import json
import argparse

from pprint import pprint

sys.path.append(os.getcwd())
try:
    from scimschema import validate
    from scimschema._model.model import Model
except ImportError:
    print(
        """Unable to find python lib 'schimschema'
Please run these command from the folder that also contains the `.git` folder
for this repository:
        git submodule init
        git submodule update
        # Apply patch to allow parsing without core schema
        patch -p1 < scimschema.patch
        export PYTHONPATH=`pwd`/scimschema
"""
    )
    sys.exit(2)


def parseOptions():
    """parse commandline parameters"""
    parser = argparse.ArgumentParser(description="""verify_schema.py""")
    parser.add_argument("--schema", default="AARC_Schema_Parseable.json")
    parser.add_argument("--vopersonschema", default="voPerson_User_Parseable.json")
    parser.add_argument("--scim", default="AARC_SCIM_Example.json")
    return parser.parse_args()


# def load_json_schemas(filenames: list):
#     print("--------------------------------------")
#     retval = {}
#     for filename in filenames:
#         print(F"loading {filename}")
#         temp = load_json_schema(filename)
#         print("--------------------------------------")
#         pprint(temp)
#         print(F"type: {type(temp)}")
#         print("--------------------------------------")
#         print(F"keys: {temp.keys()}")
#         print("--------------------------------------")
#         for key in temp.keys():
#             retval[key]=temp
#     pprint(retval)
#
#
#     return retval
def load_json_schemas(filenames: list):
    """directly load a schema by filename"""
    retval = {}
    for filename in filenames:
        with open(filename) as f:
            schema = Model.load(f)
            retval[schema.id] = schema
    return (retval)


def load_json_schema(filename):
    """directly load a schema by filename"""
    with open(filename) as f:
        schema = Model.load(f)
    return {schema.id: schema}


def load_json_data(filename):
    """load and parse json"""
    with open(filename) as f:
        data = f.read()
    try:
        obj = json.loads(data)
    except json.decoder.JSONDecodeError as ex:
        print(f"Error when decoding JSON:\n{ex}")
        sys.exit(4)
    return obj


args = parseOptions()
aarc_schema_file = args.schema
voperson_schema_file = args.vopersonschema
aarc_scim_file = args.scim

if not os.path.exists(aarc_schema_file) and args.schema == "AARC_Schema_Parseable.json":
    print(
        """Cannot find AARC_Schema_Parseable.json.
Please create it by running:
        ./make_parseable.sh"""
    )
    sys.exit(3)

# scim_schema = load_json_schema(aarc_schema_file)
# scim_schema = load_json_schema(voperson_schema_file)
scim_schema = load_json_schemas([aarc_schema_file, voperson_schema_file])
scim_data = load_json_data(aarc_scim_file)

try:
    validate(data=scim_data, extension_schema_definitions=scim_schema)
except Exception as e:
    print(e)
    sys.exit(1)
print("No news is good news. I.e. your validation worked")
