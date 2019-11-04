#!/bin/bash

piMeasurement() {
   echo "date,temperature,clockspeed"
   while : ; do
      echo "$(date +%s),$(vcgencmd measure_temp | sed "s/.*=\(.*\)'C/\1/"),$(vcgencmd measure_clock arm | sed "s/.*=\(.*\)/\1/")"
      sleep 1
   done
}

thermalZoneMeasurement() {
   local header="date,"

   # Calculate thermal zones
   local zones=()
   while IFS=' ' read -r zone
   do
      zones+=("$zone")
      header+="$(basename $zone),"
   done <<< "$(find /sys/devices/virtual/thermal/ -name "thermal_zone*" | sort -n)"

   # Calculate frequencies
   local cores=()
   while IFS=' ' read -r core
   do
      cores+=("$core")
      header+="$(basename $core),"
   done <<< "$(find /sys/devices/system/cpu/ -name "cpu[0-9]*" | sort -n)"

   echo "${header}"
   while : ; do
      echo -n "$(date +%s),"
      for zone in "${zones[@]}"; do
         local -i temperature
         temperature=$(cat "$zone/temp")
         echo -n "$(bc -l <<< "scale=2; $temperature/1000"),"
      done

      for core in "${cores[@]}"; do
         local -i frequency
         frequency=$(cat "${core}/cpufreq/scaling_cur_freq")
         echo -n "${frequency},"
      done

      echo
      sleep 1
   done
}

if command vcgencmd > /dev/null 2>&1 ; then
   # We are on a Rapberry Pi
   piMeasurement
else
   # We use some other device
   thermalZoneMeasurement
fi
