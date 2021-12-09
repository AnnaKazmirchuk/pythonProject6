from pprint import pprint
import requests


with open('VK_TOKEN.txt', 'r') as file_object:
    VK_TOKEN = file_object.read().strip()

class VKUser:

    url = 'https://api.vk.com/method/'
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.get_photos_url = self.url + 'photos.get'


    def get_photos_from_VK(self):
        params = {'access_token': self.token,
                  'v': '5.131',
                  'album_id': 'profile',
                  'owner_id': self.user_id,
                  'extended': 1,
                  'photo_sizes': 1
                  }

        res = requests.get(self.get_photos_url, params=params)
        photos_data = res.json()
        # pprint(photos_data)

        photo_album = {}
        photo_list = []
        for photo in photos_data['response']['items']:
            photo_name = photo['likes']['count']
            photo_size = photo['sizes'][-1]['type']
            photo_date = photo['date']
            url_download = photo['sizes'][-1]['url']
            new_photo_album = {'file_name': f'{photo_name}.jpg', 'size': photo_size}
            if photo_album.get(new_photo_album['file_name']):
                new_photo_album['file_name'] = f'{photo_name}.jpg'
            else:
                new_photo_album['file_name'] = f'{photo_name}_{photo_date}.jpg'
                photo_album.update(new_photo_album)
                # pprint(photo_album)
                photo_list.append(photo_album)
        pprint(photo_list)


with open('YaDisk_TOKEN.txt', 'r') as file_object:
    YaDisk_TOKEN = file_object.read().strip()

class YandexDisk:

    url = "https://cloud-api.yandex.net/v1/disk/resources/"
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }





if __name__ == '__main__':

    user1 = VKUser(390905222, VK_TOKEN)
    user1.get_photos_from_VK()







