import json

import requests


class NasaAPI:
    def __init__(self, api_key):
        self._api_key = api_key

    def get_api_key(self):
        return self._api_key

    def get_today_image(self, update):
        f = open("./README.md", "w")

        endpoint = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(self._api_key)

        res = requests.get(endpoint)
        data = json.loads(res.text)

        date = data['date']

        f.write(f'''
          # Awesome space image of the day from [NASA](https://api.nasa.gov/)

          ### Today image : {data['title']}
          Date : {date}

          ![]({data['url']})

          <small>Latest update : {update}</small>
        ''')

        f.close()
