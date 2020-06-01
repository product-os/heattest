python2 -m SimpleHTTPServer 8081&
while true
do
    python2 DS1054Z_screen_capture/OscScreenGrabLAN.py csv 192.168.1.5
    python2 DS1054Z_screen_capture/OscScreenGrabLAN.py png 192.168.1.5
    sleep 60
done
