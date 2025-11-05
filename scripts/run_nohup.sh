#!/bin/bash
cd /home/letto/Desktop/simple_analyzer/simple_analyzer
nohup python3 main.py > ../out.log 2>&1 &
