from multiprocessing import Pool
from time import sleep
import time
print('start')
class Foo:
    def __init__(self):
        print('init foo')
        self.list = []
def init_pool():
    global foo
    foo = Foo()
    sleep(4)
def job(arg):
    foo.list.append(arg)
    print(foo.list)
    if arg in [4, 8]:
        sleep(10)
    sleep(.1)
if __name__ == '__main__':
    with Pool(4, init_pool) as pool:
        print('after init')
        tic = time.time()
        pool.map(job, range(40), 1)
        print(time.time()-tic)

print('done')