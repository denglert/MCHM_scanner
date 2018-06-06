#!/bin/bash

RESOURCES="nodes=1:ppn=4,walltime=05:00:00"
#RESOURCES="nodes=1:ppn=8,walltime=02:00:00"
#RESOURCES="nodes=1:ppn=1,walltime=00:30:00"

qsub -l ${RESOURCES} -vTAG=scan_job,COMP=tri ./job_task.sh
qsub -l ${RESOURCES} -vTAG=scan_job,COMP=box ./job_task.sh
qsub -l ${RESOURCES} -vTAG=scan_job,COMP=int ./job_task.sh
qsub -l ${RESOURCES} -vTAG=scan_job,COMP=all ./job_task.sh
