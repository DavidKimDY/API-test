import os
import json

API_list = ['entity', 'morpheme', 'dependency']
Test_list = ['1', '10', '100']

def json_validation(path, test):
    filelist = os.listdir(path)
    log = ''
    for file in filelist:
        file = os.path.join(path, file)
        with open(file, "r") as f:
            data = f.read()
        try:
            json.loads(data)
        except:
            log += f'\nin the folder {test}, {file} is NOT JSON'
        else:
            log += f'\nin the folder {test}, {file} is JSON'
    return log

print('1 : 엔티티\n2 : 형태소 분석\n3 : 의존 파싱')

api_dict = {1: 'entity', 2: 'morpheme', 3: 'dependency'}
valid = int(input('Enter a number : '))
assert valid in [1, 2, 3], 'number entered has to be 1 or 2 or 3'
api = api_dict[valid]

for test in Test_list:
    path = os.path.join(api, test)
    try:
        filelist = os.listdir(path)
        log = json_validation(path, test)
    except FileNotFoundError:
        raise 'The API has to be tested.'
    # print(log)
    with open(f'Result_{api}_{test}.txt', 'w') as f:
        f.write(log)
    print(f'Result_{api}_{test}.txt is created.')

input('\nValidation is Done ! (any key)')
