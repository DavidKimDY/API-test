import json
from API_tester import Tester


MORPHEME_KEY = '14ff499053fdc7952f20948f33490e27'
DEPENDENCY_KEY = '0398cc05b56c289b4f506c03f51da339'
ENTITY_KEY = 'ef35bfb1abb5f4b6c2ac8c00a2203f2c'

tester = Tester(MORPHEME_KEY, 'dependency')
tester.set_text_path('/Users/daeyeop/Work/API test/text/')
tester.convert('1.txt')


