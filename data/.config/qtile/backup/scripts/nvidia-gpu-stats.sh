#!/usr/bin/bash

# nvidia-smi --help-query-gpu
RESPONSE=$(nvidia-smi --query-gpu=driver_version,pstate,utilization.gpu,temperature.gpu,memory.used --format=csv,noheader,nounits) 
# sed removes comas (,) globally (g)
DRIVER=$(echo $RESPONSE | awk '{print $1}' | sed 's/,//g')
PSTATE=$(echo $RESPONSE | awk '{print $2}' | sed 's/,//g')
UTILIZATION=$(echo $RESPONSE | awk '{print $3}' | sed 's/,//g')
TEMP=$(echo $RESPONSE | awk '{print $4}' | sed 's/,//g')
MEM=$(echo $RESPONSE | awk '{print $5}' | sed 's/,//g')

echo GPU: $UTILIZATION% $PSTATE $TEMPºC "$MEM"M

exit 0
