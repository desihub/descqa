#!/bin/bash

# go to a subshell
(

# make sure all commands are executed
set -e

# activate python env
source /project/projectdirs/desi/software/desi_environment.sh
export PYTHONPATH=/global/homes/j/jderose/desi/mocks/desiqa/cori/lib/python3.5/site-packages/:$PYTHONPATH
# set output directory
OUTPUTDIR="/project/projectdirs/desi/mocks/desiqa/run/"


# to allow wildcards in arguments go to master.py
set -o noglob

# run master.py
echo $PYTHONPATH
CMD="import descqarun; descqarun.main()"
python -E -c "$CMD" "$OUTPUTDIR" "$@"

# end subshell
)
