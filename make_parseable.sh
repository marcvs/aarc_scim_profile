#!/bin/bash

INPUT="AARC_Schema.json"
OUPUT="AARC_Schema_Parseeble.json"

cat AARC_Schema.json \
    | grep -vE "(saml_attribute_name|saml_attribute_urn|status)" \
    > AARC_Schema_Parseable.json
#cat ${INTPUT} \
#    | grep -vE "(saml_attribute_name|saml_attribute_urn|status)" \

