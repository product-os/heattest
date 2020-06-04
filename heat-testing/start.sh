echo "Starting stressberry ..."
stressberry-run -v
/usr/bin/python3 -m http.server 80&

# stressberry-run out.dat --duration 3600 --ambient 2302 23 #--idle 10 --cooldown 10

# Ignore ambient temp sensor flag for power testing
stressberry-run out.dat --duration 600 --idle 10 --cooldown 10

MPLBACKEND=Agg  stressberry-plot out.dat -f -d 300 -f -l 400 1600 -t 30 90 -o plot.png --not-transparent 
# pytest test/test_stressberry_standard.py
# /usr/bin/python3 test/test_stressberry_standard.py
echo "Done stressberry"
echo "Starting server"

# Snipped to take oscilloscope readings every minute
# while true
# do
#     python2 DS1054Z_screen_capture/OscScreenGrabLAN.py csv 192.168.1.5
#     python2 DS1054Z_screen_capture/OscScreenGrabLAN.py png 192.168.1.5
#     sleep 60 # wait for a minute
# done
