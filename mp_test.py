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
    #if arg in [4, 8]:
    #    sleep(0.1)
    sleep(2)
if __name__ == '__main__':
    with Pool(5, init_pool) as pool:
        print('after init')
        tic = time.time()
        pool.map(job, range(50))
        print(time.time()-tic)

print('done')