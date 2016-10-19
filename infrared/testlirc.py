import lirc

sockid = lirc.init("testlirc")

while True:
    code = lirc.nextcode()
    if (len(code)>0):
        print ("Button pressed is "+code[0])
    else:
        print ("Unknown button")

