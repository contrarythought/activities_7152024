import os
import sys
import time
import datetime

def get_creation_time(file_path:str):
    c_time_sec = os.path.getctime(file_path)
    c_time_str = time.ctime(c_time_sec)
    c_time_obj = time.strptime(c_time_str)
    return datetime.datetime(year=c_time_obj.tm_year, month=c_time_obj.tm_mon, day=c_time_obj.tm_mday, hour=c_time_obj.tm_hour)

def get_current_time(secs:float):
    curr_time_str = time.ctime(secs)
    curr_time_obj = time.strptime(curr_time_str)
    return datetime.datetime(year=curr_time_obj.tm_year, month=curr_time_obj.tm_mon, day=curr_time_obj.tm_mday, hour=curr_time_obj.tm_hour)

def get_old_files(num_days:int):
    id = os.environ["A_ID"]
    downloads_path = f"C:\\Users\\{id}\\Downloads"

    files_to_del = []
    current_time = get_current_time(time.time())

    for file in os.scandir(downloads_path):
        creation_time = get_creation_time(file.path)
        delta_time = current_time - creation_time
        if delta_time.days >= num_days:
            files_to_del.append(file)

    return files_to_del

def delete_files(files:list):
    for file in files:
        os.remove(file)

if __name__=="__main__":
    if len(sys.argv) != 1:
        print("usage: <number of days>")
        sys.exit(1)
    
    num_days = sys.argv[1]
    if not num_days.isdigit():
        print("argument needs to be an int")
        sys.exit(1)

    old_files = get_old_files(int(num_days))

    delete_files(old_files)
