# HeatTest

Raspberry Pi family heating test (

To start running a test, set an environment variable called `RUN` (either device or service
variable for the `main service`). Then the application starts the data recording and shows
the saved fileaname `testrun.YYYYMMDD_HHmmss.csv` format. After a 30s delay, it will start
a `stress --cpu 8` thread to stress the device, and will start `tail`ing the data file.

To stop the test, just delete the `RUN` env var.

If you enable device public URL, there you can find a web server to download the recorded files at `/`.
Also, if you go to `/plot/`, you can see the relevant `.csv` files, and have an option to quick plot
the recording as well.
