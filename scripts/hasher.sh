#!/bin/bash

INPFILE=$1

echo "File: $INPFILE"
echo "MD5: $(md5sum $INPFILE | cut -d" " -f1)"
echo "SHA1: $(sha1sum $INPFILE | cut -d" " -f1)"
echo "SHA256: $(sha256sum $INPFILE| cut -d" " -f1)"
echo "ssdeep: $(ssdeep -s hash.sh | tail -n1 | cut -d"," -f1)"
