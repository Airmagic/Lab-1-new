import requests

key = ''

base_url = 'http://www.omdbapi.com/'

movie = input('What movie name? ')

params = {'apikey' : key, 't' : movie}
data = requests.get(base_url, params ).json()

print(data)

print('Rating for the movie; ')
print(data['Ratings'][0]['Value'])
