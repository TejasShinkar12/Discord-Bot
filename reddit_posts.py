import requests
import os
import pandas as pd


def get_posts():
  ID = os.environ['Client ID']
  SECRET = os.environ['Client secret']

  auth = requests.auth.HTTPBasicAuth(ID, SECRET)

  data = {
    'grant_type': 'password',
    'username': 'MidKnightRider12',
    'password': os.environ['reddit_pass']
  }

  headers = {'User-Agent': 'MyAPI/0.0.1'}

  response = requests.post('https://www.reddit.com/api/v1/access_token',
                           auth=auth,
                           data=data,
                           headers=headers)

  TOKEN = response.json()['access_token']

  headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

  response = requests.get('https://oauth.reddit.com/r/Python/hot',
                          headers=headers,
                          params={'limit': 5})

  data = {'subreddit': [], 'title': [], 'Up': [], 'Link': []}

  for post in response.json()['data']['children']:
    data['subreddit'].append(post['data']['subreddit'])
    data['title'].append(post['data']['title'])
    data['Up'].append(post['data']['ups'])
    data['Link'].append(
      f"https://www.reddit.com/r/Python/comments/{post['data']['id']}/")

  df = pd.DataFrame(data)

  return (df)
