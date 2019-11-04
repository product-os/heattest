#!/bin/bash

echo "Starting web server"
python3 server.py &

if [ -n "${RUN}" ]; then
   date=$(date +%Y%d%m_%H%M%S)
   filename="/data/testrun.$date.csv"
   echo "Starting measurement"
   echo "Output filename: ${filename}"
   bash internaltemp.sh > "${filename}" &
   sleep "${DELAY:-30}"
   echo "Starting stress --cpu 8":
   stress --cpu 8 &
   tail -f "${filename}"
else
    echo "Set the env var RUN to some value to run the test."
    echo "When finished, just delete the RUN env var, and the application restarts to stop the run"
fi

while : ; do
   sleep 600
done
