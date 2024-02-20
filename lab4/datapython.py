from datetime import *;

#1 task 

timenow = datetime.now();
fivedaysago = timenow - timedelta(days=5);

print("Date that was five days ago:", fivedaysago);

#2 task

yesterday = timenow - timedelta(days=1);
tomorrow = timenow + timedelta(days=1);

print("Yesterday:", yesterday, "\nToday:", timenow, "\nTomorrow", tomorrow);

#3 task

def twois(time):
    return time.strftime("%Y/%m/%d %H:%M:%S")

print(twois(timenow));

#4 task

def difftotime(time1,time2):
    difftime = abs(time1 - time2);
    return difftime.total_seconds();

print(difftotime(yesterday, tomorrow))