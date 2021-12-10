## Overview
The suggested schema contains claims in addition to those specified in
[RFC7643](https://datatracker.ietf.org/doc/html/rfc7643):

- `saml_attribute_name`: To maintain information from the original specification
- `saml_attribute_urn`: To maintain information from the original specification
- `status`: To indicate how stable it is at the moment

## Open points

It might make sense to explicityly name the OIDC claim names. Currently
those are specified in the values of the `name` attributes.
