echo "Starting stressberry ..."
stressberry-run out.dat
MPLBACKEND=Agg  stressberry-plot out.dat -f -d 300 -f -l 400 1600 -t 30 90 -o plot.png --hide-legend --not-transparent --line-width 2
echo "Done stressberry"
echo "Starting server"
/usr/bin/python3 -m http.server
