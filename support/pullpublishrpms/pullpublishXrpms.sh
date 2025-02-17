#!/bin/bash

PRGNAME=${0##*/}

if [ $# -lt 1 ]; then
  echo "${PRGNAME}: No publish rpms path and log path are specified. Usage : ${PRGNAME} <publish-rpms-path>"
  exit 1
fi

PUBLISHRPMSPATHDIR=$1
INPUTFILE=xrpmfilelist-$(uname -m)

if [ $# -eq 2 ]; then
  PUBLISHCACHE=$2
  while read FILE; do cp -r $PUBLISHCACHE/$FILE $PUBLISHRPMSPATHDIR/$FILE; done < $INPUTFILE
else
  cat $INPUTFILE | awk '{print "https://packages.vmware.com/photon/photon_publish_x_rpms/"$1}' | xargs -n 1 -P 10 wget --user-agent Mozilla/4.0 -c -nv -nc -r -nH --quiet --cut-dirs=2 -P ${PUBLISHRPMSPATHDIR}
fi
