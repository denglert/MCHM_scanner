#!/usr/bin/env bash

CWD=$(pwd)

MCHM_scanner_dir=$(pwd)
export MCHM_scanner_dir

## - Specify the path to MG5 here!
# - Example
MG5_root_dir="/home/de3u14/lib/build/hep/MadGraph/MG5_aMC_v2_4_2"
export MG5_root_dir

PYTHON_MODULES_PATH=${CWD}/python_modules
export PYTHONPATH=${PYTHON_MODULES_PATH}:${PYTHONPATH}
