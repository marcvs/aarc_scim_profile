#!/bin/bash

INPUT="AARC_Schema.json"
OUPUT="AARC_Schema_Parseeble.json"

cat AARC_Schema.json \
    | grep -vE "(saml_attribute_name|saml_attribute_urn|status)" \
    | sed s_\ //.*__ \
    | sed s/\"unclear.*\"/true/ \
    | sed s/\"to\ be\ evaluated\"/true/ \
    > AARC_Schema_Parseable.json
#cat ${INTPUT} \
#    | grep -vE "(saml_attribute_name|saml_attribute_urn|status)" \

