from threading import *
def show1():
    for i in range(10):
        print(current_thread().getName(),":Good")
def show2():
    for i in range(10):
        print(current_thread().getName(),":Morning")

def show3():
    for i in range(10):
        print(current_thread().getName(),":User")

t1=Thread(target=show1,name="child1")
t2=Thread(target=show2,name="child2")
t3=Thread(target=show3,name="child3")
t1.start()
t2.start()
t3.start()




#more thread cocepts in images