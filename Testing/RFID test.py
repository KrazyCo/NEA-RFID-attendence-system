from pyembedded.rfid_module.rfid import RFID
rfid = RFID(port='COM1', baud_rate=9600)
print(rfid.get_id())