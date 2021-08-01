import requests


class YaDrive():
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Accept': 'application/json',
                'Authorization': f'OAuth {self.token}'
                }

    def create_new_folder(self, path):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        parameters = {'path': path}
        req = requests.put(URL, headers=self.get_headers(), params=parameters)
        print(req.json())
        return req.status_code

    def get_files_list(self, path_to_cloud=None):
        if path_to_cloud is None:
            path_to_cloud = '/'
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        parametrs = {
            'path':  path_to_cloud,
            'limit': 1000
        }
        response = requests.get(files_url, headers=headers, params=parametrs)
        files = [file['name'] for file in
                 response.json()['_embedded']['items']]
        return files


if __name__ == '__main__':
    token = 'AQAAAAAKRLFpAADLW2fzaHlsdk-GmbND08s4yJE'
    disk = YaDrive(token)
    d = disk.create_new_folder('/folder_One')

    print(d)

    files = disk.get_files_list()
    if 'folder_One' in files:
        print('ok')
