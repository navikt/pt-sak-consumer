#!/bin/bash

source /var/run/secrets/nais.io/vault/environments
export NLS_LANG=NORWEGIAN_NORWAY.AL32UTF8

python3.6 app.py
