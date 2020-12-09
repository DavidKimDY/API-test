import requests
import json
from io import BytesIO
import datetime
import multiprocessing

def download_file(download_path, filename):
    api_url = "https://api-lab.core.today/v1/object?"
    r = requests.get(api_url, params={"key": filename})
    download_url = json.loads(r.text)['url']
    res = requests.get(download_url)
    assert res.status_code == 200, 'No file'
    with open(download_path, "wb") as f:
        data = BytesIO(res.content).getbuffer()
        f.write(data)
    return 200
1

def count_and_print(number, i):
    if number == 1:
        if i % 10 == 0:
            print(i)
    else:
        if i % 100 == 0:
            print(i)


def download(number, i):
    filename = f'{number}_{i}.json'
    if number < 4:
        download_path = f'{number}/to_download/{filename}'
    else:
        sub_dir = (i - 1) // 10000 + 1
        download_path = f'{number}/to_download/{sub_dir}/{filename}'

    download_file(download_path, filename)
    count_and_print(number, i)


if __name__ == '__main__':

    number_list = list(range(1,6))
    number = int(input('1 : 100\n2 : 1000\n3 : 10000\n4 : 100000\n5 : 1000000\nnumber : '))
    assert number in number_list, f'number has to be in {number_list}'

    range_number = 10 * (10 ** number) + 1
    iterable = [(number, i) for i in range(1, range_number)]

    start = datetime.datetime.now()

    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)
    pool.starmap(download, iterable)
    pool.close()
    pool.join()

    print(f'Taken time : {datetime.datetime.now() - start}')
    input(f'Download #{number} is Done (Enter)')
