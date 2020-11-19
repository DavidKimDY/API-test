import json
import os
import requests


API_FOLDER_PATH = '/Users/daeyeop/Work/API test'
ENTITY = '/엔티티 분석'
DEPENDENCY = '/의존 파싱'
MORPHEME = '/형태소 분석'
TEXT = '/Text'


class Tester():
    def __init__(self, api_key):
        self.mor_url = 'https://api.x.core.today/a75a68b0b-f859-4bfa-a487-fa12f1a0bb4a/'
        self.ent_url = 'http://api.x.core.today/ab7eb939d-9d08-41cc-be2f-226065331e7d/'
        self.dep_url = 'http://api.x.core.today/aca29268b-b75d-4009-8db5-22d756a5d36b/'
        self.__api_key = api_key
        self.text = ''
        self.header = {
            'api-key' : self.__api_key
        }
        self.params = {
            'text': self.text
        }

    def convert_to_entity(self, text_file: str):
        assert os.path.isfile(text_file), 'Not found file : {}'.format(text_file)
        with open(text_file, 'r', encoding='utf-8') as f:
            self.text = f.read(f)
        converted = requests.get(self.ent_url, headers=self.header, params=self.params)
        print(json.loads(converted))
