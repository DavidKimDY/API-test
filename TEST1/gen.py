
import os
import json
import multiprocessing as mp

'''
# Make to_upload, to_download directory for 1~5
for i in range(1, 6):

    os.mkdir(f'{i}')
    os.mkdir(f'{i}/to_upload')
    os.mkdir(f'{i}/to_download')

# Make sub_directory for 4
for i in range(1, 11):
    os.mkdir('4/to_download/{}'.format(i))
    os.mkdir('4/to_upload/{}'.format(i))

# Make sub_directory for 5
for i in range(1, 101):
    os.mkdir('5/to_download/{}'.format(i))
    os.mkdir('5/to_upload/{}'.format(i))
'''

def data(i):
    return {'n': i}


def make_data(number, i):
    x = data(i)
    if number < 4:
        with open(f'{number}/to_upload/{number}_{i}.json', 'w') as f:
            json.dump(x, f)
    else:
        sub_dir = (i - 1) // 10000 + 1
        with open(f'{number}/to_upload/{sub_dir}/{number}_{i}.json', 'w') as f:
            json.dump(x, f)


if __name__ == '__main__':

    for number in [4]: # , 2, 3, 4, 5]:
        range_number = 10 * (10 ** number) + 1
        iterable = [(number, i) for i in range(1, range_number)]
        cpu_count = mp.cpu_count()
        pool = mp.Pool(processes=cpu_count)
        pool.starmap(make_data, iterable)
        pool.close()
        pool.join()
