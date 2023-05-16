#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:04:44 2019

@author: marcoaqil
Adapted by Ralph Wientjens(ralphw713@hotmail.com)
"""
import sys
import os
from session import PRFSession
from datetime import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():
    subject = sys.argv[1]
    sess =  sys.argv[2]
    # We would do 5 runs, which are loaded individually
    run = sys.argv[3]
    eyetracker_on = bool(sys.argv[4])
    
    output_str= subject+'_'+sess+'_'+run
    
    output_dir = './logs/'+output_str+'_Logs'
    
    if os.path.exists(output_dir):
        print("Warning: output directory already exists. Renaming to avoid overwriting.")
        output_dir = output_dir + datetime.now().strftime('%Y%m%d%H%M%S')
    
    settings_file='./expsettings_2R.yml'

    ts = PRFSession(output_str=output_str, output_dir=output_dir, settings_file=settings_file, eyetracker_on=eyetracker_on)
    ts.run()

if __name__ == '__main__':
    main()