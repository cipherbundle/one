#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:35:43 2018

@author: arabhi
"""
#code to take breaks every 2 hrs 3 times in total
import webbrowser
import time
total_breaks = 3
count = 1
sleep_for = 2*60*60
print "The current time is "+time.ctime()
while (count <= total_breaks):
    time.sleep(sleep_for)
    url = 'https://www.youtube.com/watch?v=UZrzOZaI7UE'
    webbrowser.open(url)
    count =count+1