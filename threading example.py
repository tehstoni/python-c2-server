import threading
import time


def test():
    print("this got executed")
    time.sleep(1)


for i in range(0, 10):
    t = threading.Thread(target=test())
    t.start()



