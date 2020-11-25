import sys
import time
import threading

try:
    import neighbors as neighbors
except Exception as e:
    print(e)
    print('Import Fail')
    exit()

class TimedThread(threading.Thread):
    def run(self):
        self.err = None
        try:
            threading.Thread.run(self)
        except Exception as err:
            self.err = err
            print(err)

class RunWithTimeout(object):
    def __init__(self, function, args):
        self.function = function
        self.args = args
        self.answer = None

    def worker(self):
        try:
            self.answer = self.function(*self.args)
        except Exception as e:
            print(e)
            self.answer = 'Fail'

    def run(self, timeout):
        thread = TimedThread(target=self.worker)
        thread.start()
        thread.join(timeout=5)
        if thread.err != None:
            self.answer = 'Fail'
        return self.answer

n = 4
d = [[0, 23, 27, 20],
    [23, 0, 30, 28],
    [27, 30, 0, 30],
    [20, 28, 30, 0]]
a = {}
a[1] = {5: 13.50}
a[2] = {5: 16.50}
a[3] = {4: 12.00}
a[4] = {5: 2.00, 0: 8.00, 3: 12.00}
a[5] = {1: 13.50, 2: 16.50, 4: 2.00}

try:
    proc = RunWithTimeout(neighbors.main, (n, d))
except Exception as e:
    print(e)
    print('Fail')
    exit()
b = proc.run(5)

if b == 'Fail':
    print('Fail')
    exit()

if b == None:
    print('Time')
    exit()

for key in a:
    for node in a[key]:
        if key in b and node in b[key] and b[key][node] == a[key][node]:
            pass
        else:
            print('Answer Fail')
            exit()
print('Pass')
