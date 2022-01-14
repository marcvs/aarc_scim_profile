## Overview
The suggested schema contains claims in addition to those specified in
[RFC7643](https://datatracker.ietf.org/doc/html/rfc7643):

- `saml_attribute_name`: To maintain information from the original specification
- `saml_attribute_urn`: To maintain information from the original specification
- `status`: To indicate how stable it is at the moment

## Parsing
To verify a JSON object against a SCIM schema, I've included a small tool
`verify_scim.py`.  Usage is self descriptive, just follow the
instructions.

Since the current schema contains additional fields that would break
parsing, there is a quick (and only mildly dirty) preprocessor
(`make_parseable.sh`) that will generate `AARC_Schema_Parseable.json` from
`AARC_Schema.json`.

## Changelog (of the schema file)

- Fri Jan 14:
    - Replace `id` fields with `$ref` fields
    - Adjust the `name` of the schema to be RFC compliant
    - Fix errors in multi-valuedness of `entitlements` and `email`
    - Rename main entry of multivalued entries to `value`


## Open points

It might make sense to explicityly name the OIDC claim names. Currently
those are specified in the values of the `name` attributes.

One next step is to add example output.
