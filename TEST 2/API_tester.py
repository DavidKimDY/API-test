import json
import os
import requests


class Tester():
    def __init__(self, api_key, mode=None):
        assert mode is not None, 'Tester.__init__ expected a key argument, one of [entity, morpheme, dependency]'
        assert mode in ['entity', 'morpheme', 'dependency'], 'one of [entity, morpheme, dependency], not {}'.format(mode)
        self.morpheme_url = 'https://api.x.core.today/a75a68b0b-f859-4bfa-a487-fa12f1a0bb4a/'
        self.entity_url = 'http://api.x.core.today/ab7eb939d-9d08-41cc-be2f-226065331e7d/'
        self.dependency_url = 'http://api.x.core.today/aca29268b-b75d-4009-8db5-22d756a5d36b/'
        self.save_path = ''
        self.url_dict = {
                        'entity': self.entity_url,
                        'morpheme': self.morpheme_url,
                        'dependency': self.dependency_url
                         }
        self.__api_key = api_key
        self.mode = mode
        self.load_path = ''
        self.header = {'api-key': self.__api_key}
        self.params = {'text': ''}

    def _convert_and_save(self, text_file: str, url):
        path = os.path.join(self.load_path, text_file)
        assert os.path.isfile(path), 'Not found file : {} in {}'.format(text_file, path)

        with open(path, 'r', encoding='utf-8') as f:
            self.params['text'] = f.read()

        converted = requests.get(url, headers=self.header, params=self.params)
        json_data = json.loads(converted.text)
        self.save(json_data, text_file)

    def convert(self, text_file: str):
        url = self.url_dict[self.mode]
        self._convert_and_save(text_file, url)

    def set_text_path(self, load_path):
        self.load_path = load_path

    def set_save_path(self, save_path):
        self.save_path = save_path

    def save(self, json_data, text_file):
        name = self.get_file_name(text_file)
        save_path = os.path.join(self.save_path, self.mode)
        print(save_path)
        if not os.path.isdir(save_path):
            os.mkdir(save_path)

        save_file_name = self.mode + '_' + name + '.json'
        save_file_path = os.path.join(self.save_path, self.mode, save_file_name)

        with open(save_file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent='\t')

    def get_file_name(self, text_file: str):
        name = text_file.split('.')[0]
        return name


