#!/bin/bash


cat AARC_Schema.json\
    | grep -vE "(saml_attribute_name|saml_attribute_urn|status)" \
    | sed s_\ //.*__ \
    | sed s/\"unclear.*\"/true/ \
    | sed s/\"to\ be\ evaluated\"/true/ \
    > AARC_Schema_Parseable.json


cat voPerson_User.json\
    | grep -vE "(saml_attribute_name|saml_attribute_urn|status)" \
    | sed s_\ //.*__ \
    | sed s/\"unclear.*\"/true/ \
    | sed s/\"to\ be\ evaluated\"/true/ \
    > voPerson_User_Parseable.json

