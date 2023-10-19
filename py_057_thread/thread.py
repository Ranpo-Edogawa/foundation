from time import sleep
from threading import Thread


def get_to_ten(name, delay):
    for i in range(10):
        print(i,name)
    

t1 = Thread(target=get_to_ten, args=('Thread1', 1))
t2 = Thread(target=get_to_ten, args=('Thread2', 2))

t2.start()
t1.start()
# get_to_ten('Thraed1', 1)
# get_to_ten('Thraed2', 2)

