#!/bin/bash

FILENAME1=$1
FILENAME2=$2

DIFFCMD="diff --ignore-blank-lines --suppress-common-lines"
ODTCMD="odt2txt --width=120"

$ODTCMD $FILENAME1 > ${FILENAME1}.txt.tmp
$ODTCMD $FILENAME2 > ${FILENAME2}.txt.tmp

$DIFFCMD ${FILENAME1}.txt.tmp ${FILENAME2}.txt.tmp | sed '/^>\s*$/d' | sed '/^<\s*$/d'
