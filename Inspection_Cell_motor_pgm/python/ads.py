from pyads import *

with AdsDevice(amsTarget="169.254.46.62.4.1:851") as device:
    info = device.ReadDeviceInfo()
    print(info)
