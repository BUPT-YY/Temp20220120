#!/bin/bash

BUAD_RATE=115200
SERIAL=/dev/ttyUSB0
LOGFILE=./rawlog.txt

#$(date "+%Y-%m-%d-%H-%M-%S")

stty -F ${SERIAL} ispeed ${BUAD_RATE} ospeed ${BUAD_RATE} cs8


cat ${SERIAL} >> ${LOGFILE}

#30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
