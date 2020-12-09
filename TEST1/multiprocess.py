import multiprocessing
import datetime
import time

def count(w ,name):
    for i in range(1, 6):
        a = 100**1000000
        print(f'{name} : {i} {w}')

num_list = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']

print('start!!')
print(__name__)
start = datetime.datetime.now()
if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()
    print(f'multiprocessing cpu : {cpu_count}')
    pool = multiprocessing.Pool(processes=3)
    print(pool)
    pool.starmap(count, [(1, 'p1'), (2, 'p2'), (3, 'p3')])
    print('starmap done')
    pool.close()
    print('close done')
    pool.join()
    print('join done')
print('time sleep 5s')
time.sleep(5)
print(f'Taken time : {datetime.datetime.now() - start}')
print('la?')