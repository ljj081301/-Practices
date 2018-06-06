import time

def text():
    return "texttext"



def timer():
    for i in (0,2):
        time.sleep(0.5)

    print "done!"

print text()
timer()