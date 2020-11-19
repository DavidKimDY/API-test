import json
from API_tester import Tester


MORPHEME_KEY = '14ff499053fdc7952f20948f33490e27'
DEPENDENCY_KEY = '0398cc05b56c289b4f506c03f51da339'

mor_tester = Tester(MORPHEME_KEY)
mor_tester.convert_to_entity('1.txt')
