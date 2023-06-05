import shutil
import psutil
import os
print("This programme copies everything from your pendrive")


def cheeck(path):
    if os.path.isfile(path):
        return False
    else:
        return True


while True:
    devices = psutil.disk_partitions()
    hello = False
    for device in devices:
        if device.opts == "rw,removable":
            var = device.mountpoint
            hello = True
    if hello == True:
        break
if hello == True:
    lists = os.listdir(var)
    for l in lists:
        if l == "System Volume Information":
            pass
        else:
            if cheeck(var+l) == False:
                shutil.copy(var+l, os.getcwd())
            else:
                shutil.copytree(var+l, os.getcwd()+f"\\{l}")
    print("Everything is copied from your pendrive to the current working directory.")

else:
    print("Pendrive Is Unplugged")
