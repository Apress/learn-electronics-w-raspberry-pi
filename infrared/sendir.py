import os
import time

REMOTE = "photoremote"
DELAY = 20

def send_ir_cmd (remote, op):
	os.system("irsend SEND_ONCE "+remote+" "+op);


send_ir_cmd (REMOTE, "Power")
time.sleep(DELAY)
send_ir_cmd (REMOTE, "Power")
