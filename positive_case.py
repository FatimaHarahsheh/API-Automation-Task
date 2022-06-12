import pytest
import requests


base_url = 'https://jsonplaceholder.typicode.com'


class Tests:
    def test_get_all_posts(self):
        url = '/posts'
        req_test = requests.get(base_url+url)
        assert req_test.status_code == 200

    def test_get_specific_posts(self):
        url = '/posts/1'
        req_test = requests.get(base_url+url)
        assert req_test.status_code == 200
        data = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
        assert req_test.json() == data

    def test_get_all_comments(self):
        url = '/comments?postId=1'
        req_test = requests.get(base_url+url)
        assert req_test.status_code == 200

    def test_post_new_posts(self):
        url = '/posts'
        data = {
            "userId": 3,
            "id": 3,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        }
        req_test = requests.post(base_url+url, data)
        assert req_test.status_code == 201

    def test_delete(self):
        url = '/posts/1'
        req_test = requests.delete(base_url+url)
        assert req_test.status_code == 200
