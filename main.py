import os, time, datetime,shutil

path = "/home/island/Documents/temp/"
now = time.time()
old = now - 7 * 86400
print("today: " + str(now))
print("old: " + str(old) + "\n")

for root, dirs, files in os.walk(path):
    for _dir in dirs:
        tarikh = time.mktime(datetime.datetime.strptime(_dir,"%Y-%m-%d").timetuple())
        print(_dir)
        print(tarikh)

        if tarikh < old:
            print(f"Removing: {path}{_dir}")
            shutil.rmtree(path + _dir,ignore_errors=False, onerror=None)

        else:
            print("false" + "\n")
