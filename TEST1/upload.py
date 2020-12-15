import requests
import json
import datetime
import multiprocessing


def upload_file(filename, data):
    api_url = "https://api-lab.core.today/v1/object?"
    r = requests.put(api_url, params={"key": filename})
    upload_url = json.loads(r.text)['url']
    r = requests.put(upload_url, data=data)
    return r.status_code


def count_and_print(number, i):
    if number == 1:
        if i % 10 == 0:
            print(i)
    else:
        if i % 100 == 0:
            print(i)
            pass
    

def upload(number, i):
    filename = f'{number}_{i}.json'
    if number < 4:
        upload_path = f'{number}/to_upload/{filename}'
    else:
        sub_dir = (i - 1) // 10000 + 1
        upload_path = f'{number}/to_upload/{sub_dir}/{filename}'

    upload_file(upload_path, filename)
    count_and_print(number, i)


if __name__ == '__main__':

    print('Upload !')

    number_list = list(range(1, 6))
    number = int(input('1 : 100\n2 : 1000\n3 : 10000\n4 : 100000\n5 : 1000000\nnumber : '))
    assert number in number_list, f'number has to be in {number_list}'

    range_number = 10 * (10 ** number) + 1
    iterable = [(number, i) for i in range(1, range_number)]

    start = datetime.datetime.now()

    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)
    pool.starmap(upload, iterable)
    pool.close()
    pool.join()


    print(f'taken time : {datetime.datetime.now() - start}')
    input(f'Upload #{number} is Done (Enter)')
