echo "Starting stressberry ..."
stressberry-run out.dat
MPLBACKEND=Agg stressberry-plot out.dat -o out.png
echo "Done stressberry"
echo "Starting server"
/usr/bin/python3 -m http.server
