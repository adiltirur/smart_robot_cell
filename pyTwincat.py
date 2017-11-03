import pyads
import time
pyads.open_port()
adr=pyads.AmsAddr('169.254.46.62.1.1',851)
#status=pyads.read_by_name(adr,'MAIN.partReadyToRot',pyads.PLCTYPE_BOOL)
pyads.write_by_name(adr, 'MAIN.partAngle', '51', pyads.PLCTYPE_STRING)
while True:
    pyads.write_by_name(adr, 'MAIN.partReadyToRot', False, pyads.PLCTYPE_BOOL)
    pyads.write_by_name(adr, 'MAIN.partReadyToPick', True, pyads.PLCTYPE_BOOL)
    time.sleep(1)
    pyads.write_by_name(adr, 'MAIN.partReadyToRot', True, pyads.PLCTYPE_BOOL)
    pyads.write_by_name(adr, 'MAIN.partReadyToPick', False, pyads.PLCTYPE_BOOL)
    time.sleep(1)
    #print(status)
pyads.close_port()
