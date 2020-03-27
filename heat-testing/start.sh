echo "Starting stressberry ..."
stressberry-run -v
stressberry-run out.dat --duration 3600 --ambient 2302 23 #--idle 10 --cooldown 10
MPLBACKEND=Agg  stressberry-plot out.dat -f -d 300 -f -l 400 1600 -t 30 90 -o plot.png --hide-legend --not-transparent --line-width 2
# pytest test/test_stressberry_standard.py
/usr/bin/python3 test/test_stressberry_standard.py
echo "Done stressberry"
echo "Starting server"
/usr/bin/python3 -m http.server 80
