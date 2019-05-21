#!/bin/bash

echo "date,temperature,clockspeed"
while : ; do
   echo "$(date +%s),$(vcgencmd measure_temp | sed "s/.*=\(.*\)'C/\1/"),$(vcgencmd measure_clock arm | sed "s/.*=\(.*\)/\1/")"
   sleep 1
done