from threading import Thread, Lock

a = 0


def function(l, arg):
    global a
    l.acquire()
    try:
        for i in range(arg):
            a += 1
    finally:
        l.release()


def main():
    lock = Lock()
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(lock, 1000000))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("Total value is {}".format(a))


if __name__ =='__main__':
    main()
