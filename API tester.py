import json
import requests

API_FOLDER_PATH = '/Users/daeyeop/Work/API test'
ENTITY = '/엔티티 분석'
DEPENDENCY = '/의존 파싱'
MORPHEME = '/형태소 분석'
TEXT = '/Text'


headers = {
    "api-key": "5012f035sfj93ka923dk8s2fc5ce6"
}
params = {
    "text": "안녕하세요 좋은 하루 입니다"
}
api_url = "https://api.x.core.today/a75a68b0b-f859-4bfa-a487-fa12f1a0bb4a/"
r = requests.get(api_url, headers=headers, params=params)
print(json.loads(r.text))


class Tester():
    pass


class TestEntity(Tester):
    pass


class TestMorpheme(Tester):
    pass


class TestDependency(Tester):
    pass