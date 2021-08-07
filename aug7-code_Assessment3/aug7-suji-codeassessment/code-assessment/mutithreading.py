import threading,time,logging
try:
    def even(getlist):
        for i in getlist:
            if i%2==0:
                time.sleep(1)
                print("even number:",i)
    def odd(getlist):
        for i in getlist:
            if i%2!=0:
                time.sleep(2)
                print("odd number:",i)
    mylist=[3,57,896,284,63,156]  
    a=threading.Thread(target=even,args=(mylist,))    
    b=threading.Thread(target=odd,args=(mylist,))
    a.start()
    b.start()
    a.join()
    b.join()
    print("*******")
except:
    logging.error("something wrong")