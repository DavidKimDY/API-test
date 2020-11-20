import os
from API_tester import Tester


API_KEY = '14ff499053fdc7952f20948f33490e27'
current_location = os.getcwd()
text_data_path = os.path.join(current_location, 'text')
one_save_path = os.path.join(current_location, '1')
ten_save_path = os.path.join(current_location, '10')
hundred_save_path = os.path.join(current_location, '100')

if os.path.isdir(one_save_path):
    print('yes there is')
else:
    os.mkdir(one_save_path)

print(text_data_path)


mode_list = ['morpheme', 'dependency', 'entity']
text_file_list = os.listdir(text_data_path)


for i, save_path in zip((1, 10, 100), [one_save_path, ten_save_path, hundred_save_path]):
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    for mode in mode_list:
        tester = Tester(API_KEY, mode)
        tester.set_text_path(text_data_path)
        tester.set_save_path(save_path)
        for j in range(i):
            tester.convert(text_file_list[j])

