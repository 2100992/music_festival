import requests
import json

OUTH_DATA = {'username': 'pws_admin', 'password':'sf_password'}

URL = 'https://deaf-tracts.herokuapp.com/'
JWT_CREATE = 'auth/jwt/create/'
GET_POST = 'blog/api/posts/'


def get_jwt_token():
    resp = requests.post(URL+JWT_CREATE, OUTH_DATA)
    token = resp.json().get('access', None)
    if token:
        return 'JWT ' + token
    else:
        print('Some error in post Authentication')
        return None

def get_posts(jwt_token):
    resp = requests.get(URL+GET_POST, headers={'Authorization': jwt_token})
    return resp.json()['results']

def post_new_post(jwt_token, data):
    resp = requests.post(URL+GET_POST, data=data,  headers={'Authorization': jwt_token})
    # print(resp)
    return resp

def main():
    jwt_token = get_jwt_token()

    new_post_data = {}
    new_post_data['title'] = 'Новый тестовый пост'
    new_post_data['markdown_field'] = '##!!!NEW POST'
    new_post_data['category'] = ['news', 'tests',]

    resp = post_new_post(jwt_token, new_post_data)

    if resp.ok:
        posts = get_posts(jwt_token)
        print(json.dumps(posts, indent=4, sort_keys=True))
    else:
        print('Some error in post request')

if __name__ == "__main__":
    main()