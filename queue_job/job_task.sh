#!/bin/bash
#
#TAG=$1
#COMP=$2

###

WORKDIR=/scratch/de3u14/CHM/cross_section_scan
#PROGRAM=/scratch/de3u14/CHM/cross_section_scan/xsec_scan.py
PROGRAM=/scratch/de3u14/CHM/cross_section_scan/mg5_scanner.py

###

source /home/de3u14/lib/setup_env/setup_env_py27.sh

cd ${WORKDIR}
${PROGRAM} ${TAG} ${COMP}
