import requests

OUTH_DATA = {'username': 'pws_admin', 'password':'sf_password'}

URL = 'http://localhost:8000/'
JWT_CREATE = 'auth/jwt/create/'
GET_POST = 'blog/api/posts/'


def get_jwt_token():
    resp = requests.post(URL+JWT_CREATE, OUTH_DATA)
    return 'JWT ' + resp.json()['access']

def get_posts(jwt_token):
    resp = requests.get(URL+GET_POST, headers={'Authorization': jwt_token})
    return resp.json()['results']

def post_new_post(jwt_token, data):
    resp = requests.post(URL+GET_POST, data=data,  headers={'Authorization': jwt_token})
    print(resp)

def main():
    jwt_token = get_jwt_token()

    new_post_data = {}
    new_post_data['title'] = 'Новый тестовый пост'
    new_post_data['markdown_field'] = '##!!!NEW POST'
    new_post_data['category'] = ['news', 'tests']

    post_new_post(jwt_token, new_post_data)

    posts = get_posts(jwt_token)

    print(posts)

if __name__ == "__main__":
    main()