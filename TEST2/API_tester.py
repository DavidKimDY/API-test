import json
import os
import requests


class Tester():
    def __init__(self, api_key, mode=None):
        assert mode is not None, 'Tester.__init__ expected a \'mode\' argument, one of [entity, morpheme, dependency]'
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

    def _convert_and_save(self, text_file, url):
        path = os.path.join(self.load_path, text_file)
        print(text_file)
        assert os.path.isfile(path), 'Not found file : {} in {}'.format(text_file, path)

        with open(path, 'r', encoding='utf-8') as f:
            self.params['text'] = f.read()

        converted = requests.get(url, headers=self.header, params=self.params)
        json_data = json.loads(converted.text)
        try:
            status = json_data['status']
        except:
            status = None
        assert status != 'error', json_data['message']

        self.save(json_data, text_file)

    def convert(self, text_file):
        url = self.url_dict[self.mode]
        self._convert_and_save(text_file, url)

    def set_load_path(self, load_path):
        self.load_path = load_path

    def set_save_path(self, save_path):
        self.save_path = save_path

    def save(self, json_data, text_file):
        name = self.get_file_name(text_file)
        if not os.path.isdir(self.save_path):
            os.mkdir(self.save_path)

        save_file_name = self.mode + '_' + name + '.json'
        save_file_path = os.path.join(self.save_path, save_file_name)

        with open(save_file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent='\t')

    def get_file_name(self, text_file):
        name = text_file.split('.')[0]
        return name


class Test():
    def __init__(self, mode, text_data_path=None):
        if text_data_path is None:
            previous_location = os.path.dirname(os.getcwd())
            self.text_data_path = os.path.join(previous_location, 'text')
        else:
            self.text_data_path = text_data_path
        base_url = 'https://core.today/api/market/product/key/'
        API_url_dict = {
            'entity': 'ab7eb939d-9d08-41cc-be2f-226065331e7d',
            'morpheme': 'a75a68b0b-f859-4bfa-a487-fa12f1a0bb4a',
            'dependency': 'aca29268b-b75d-4009-8db5-22d756a5d36b'
        }

        self.text_file_list = [int(file_name.replace('.txt', '')) for file_name in os.listdir(self.text_data_path)]
        self.text_file_list = [str(file_name)+'.txt' for file_name in sorted(self.text_file_list)]
        self.mode = mode
        print('Visit to get API key : ', base_url + API_url_dict[mode])
        self.API_KEY = input('{} API: '.format(mode))
        self.tester = Tester(self.API_KEY, self.mode)
        self.tester.set_load_path(self.text_data_path)

    def __call__(self):

        for i in (1, 10, 100):
            save_path = os.path.join(os.getcwd(), self.mode, str(i))
            if not os.path.isdir(save_path):
                os.mkdir(save_path)
            self.tester.set_save_path(save_path)
            print('Data Quantity : {}'.format(i))
            for j in range(i):
                if j == 0:
                    print('processing...\n')
                self.tester.convert(self.text_file_list[j])

