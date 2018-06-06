# MCHM scanner

Requirements:
- `python` 2.6 or 2.7 (sadly no py3 due to the fact that MG5 written in written in py2)
- `pandas`
- `numpy`
- `matplotlib`

## Setup

1. Copy the UFO model to the `./models` of your MG5 install.
2. Standing in the root-dir of this package issue `source setup.sh`.


### On IRIDIS

You need to load in a fresh pairs of compiles: 

~~~~
module load gcc/6.1.0
~~~~

## UFO model

The UFO model can be found in `./mg5_model/loop_chm/`.

## Usage

1. Create MG5 code for the processes

    First you need to set up the processes in MG5 - `./create_mg5_process` 

    ~~~~
    ./create_mg5_process.py
    ~~~~

2. Edit `mg5_scanner.py`

You need to specify:
- The scan grid inside `mg5_scanner`.
- run tag as the first argument
- component as the second argument


Example:

~~~~
./mg5_scanner.py test tri
~~~~


### Job submission

Some examples for job submission scripts can be found in `./queue_job/` dir.


## Troubleshooting


### `Your version of gfortran is older than 4.6`

~~~~
ERROR, you could not compile /scratch/de3u14/CHM/MCHM_scanner/mg5_processes/CHM_gg_Zh_tri/Source
because your version of gfortran is older than 4.6. MadGraph5_aMC@NLO will carry on, but will not be
able to compile an executable.
~~~~

You can load in a compatible version of `gfortran` IRIDIS by issuing:

~~~~
module load gcc/6.1.0
~~~~

[MG5]: https://launchpad.net/mg5amcnlo
