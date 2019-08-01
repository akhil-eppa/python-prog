# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:07:27 2019

@author: Akhil
"""
def time(start,end):
    t1=start[0]*3600+start[1]*60+start[2]
    t2=end[0]*3600+end[1]*60+end[2]
    diff=abs(t1-t2)
    h=diff//3600
    m=(diff%3600)//60
    s=(diff%3600)%60
    return [h,m,s]

starttime=input("Enter start time as hh,mm,ss:").split(",")
endtime=input("Enter end time as hh,mm,ss:").split(",")
for i in range(3):
    starttime[i]=int(starttime[i])
    endtime[i]=int(endtime[i])
timediff=time(starttime,endtime)
print("The time difference is:",timediff)