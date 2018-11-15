#!/bin/bash

# bump version number by one

OLD=$(cat ./version | cut -d'.' -f3)
NEW=0.0.$(expr $OLD + 1)

echo "$NEW" > version
echo $NEW
