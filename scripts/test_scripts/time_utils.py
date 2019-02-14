
import datetime

def add_seconds(time_stamp, secs):
    time_stamp = time_stamp + datetime.timedelta(seconds=secs)
    return time_stamp



def reduce_seconds(time_stamp, secs):
    time_stamp = time_stamp - datetime.timedelta(seconds=secs)
    return time_stamp.strftime("%Y-%m-%d %H:%M:%S")


reduce_seconds(1546842021, 2700)
