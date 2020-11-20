import os
from API_tester import Tester

mode = 'entity'
API_KEY = '14ff499053fdc7952f20948f33490e27'
current_location = os.getcwd()
previous_location = os.path.dirname(current_location)
text_data_path = os.path.join(previous_location, 'text')
text_file_list = os.listdir(text_data_path)


for i in (1, 10, 100):
    save_path = os.path.join(current_location, str(i))

    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    tester = Tester(API_KEY, mode)
    tester.set_text_path(text_data_path)

    tester.set_save_path(save_path)
    for j in range(i):
        tester.convert(text_file_list[j])
