#Multithreading : Thread is a light weight process
#Every Python program has atleast one thread which is main thread
#We can implement threading by inheriting Thread class
#Thread class has two methods start() and run()
#we can call start() method,internaly it calls run() method

from threading import Thread
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)#sleep for 1 sec
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)#sleep for 1 sec

t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)#sleep for 0.2 secs
t2.start()
t1.join()#wait until thread terminates
t2.join()#wait until thread terminates
print("Bye...Bye...")#executed by main thread