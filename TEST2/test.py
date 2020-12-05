from API_tester import Test
import os

MODE_DICT = {'1': 'entity', '2': 'morpheme', '3': 'dependency'}
number = input('1 : 엔티티\n2 : 형태소 분석\n3 : 의존 파싱\nnumber : ')
numbers = MODE_DICT.keys()
assert number in numbers, '\nWrong number! Number has to be in {}\n'.format(numbers)

MODE = MODE_DICT[number]
text_data_path = os.path.join(os.getcwd(), 'text')
test = Test(MODE, text_data_path=text_data_path)
test()