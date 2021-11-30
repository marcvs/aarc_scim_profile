#!/usr/bin/env python3

import json
import textwrap
from sys import stdout

show_defaults = False

short_scim_attributes = { # a dict with default values
    "caseExact": "false",
    "multiValued": "false",
    "mutability": "readWrite",
    "required": "false",
    "returned": "default",
    # "subAttributes": [],
    "uniqueness": "none"
}
scim_attributes = { # a dict with default values
    # "name": "",
    # "description": "",
    # "canonicalValues": "",
    "referenceTypes": [],
    # "subAttributes": [],
    "type": "",
}
additional_attributes = {
    "saml_attribute_name": "",
    "saml_attribute_urn": "",
}

fh=open("AARC_Schema.json", "r")
schema_json = json.loads(fh.read())

# print(json.dumps(schema_json, sort_keys=True, indent=4, separators=(',', ': ')))


for item in schema_json[0]['attributes']:
    stdout.write("-"*113+"\n")
    stdout.write(F"{item['name']+':'[0:28]:28}")

    # Description
    if len(item["description"]) == 0:
        stdout.write("\n")
    else:
        lines = textwrap.wrap(item['description'], 84, break_long_words=False)
        spacers = ""
        for line in lines:
            stdout.write(F"{spacers}{line}\n")
            spacers = 28*" "

    # short attributes
    stdout.write(28*" " + "|")
    for attr in short_scim_attributes:
        stdout.write(F" {attr:12}|")
    stdout.write("\n" + 28 * " " + "|")
    for attr in short_scim_attributes:
        try:
            stdout.write(F" {item[attr]:<12}|")
        except KeyError:
            stdout.write(F" {short_scim_attributes[attr]+'(dflt)':<12}|")
    stdout.write("\n")


    # other attributes
    for attr in list(additional_attributes.keys()) + list(scim_attributes.keys()):
    # for attr in  scim_attributes.keys():
        try:
            temp = item[attr]
            stdout.write(F"    {attr+':':24}")
        except KeyError:
            if show_defaults:
                stdout.write(F"    {attr:24}")
        try:
            try: 
                stdout.write(F"{item[attr][0:90]:<24}\n")
            except TypeError:
                if type(item[attr]) is list:
                    stdout.write(F"{', '.join(item[attr])}\n")
                    # stdout.write(F"\n")
                    # for e in item[attr]:
                    #     stdout.write(F"        {e}")
                else:
                    stdout.write(F"{item[attr]:<24}\n")

        except KeyError:
            if show_defaults:
                stdout.write(F"{scim_attributes[attr]}(dflt)\n")
    

    # sub attributes
    if item.get('subAttributes'):
        print("    subAttributes:")
        for sub_attr in item['subAttributes']:
            print (F"        - {sub_attr['name']}")



