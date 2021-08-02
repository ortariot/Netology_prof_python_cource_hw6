import pytest
from yadrive_folders import YaDrive


class TestYaDrive():
    token = 'you token'
    disk = YaDrive(token)

    def setup_class(cls):
        print('stat testing')

# test for creating new folder
# test for creating new folder with nonexistent pash
# test for creating new folder with has incorrect format

    @pytest.mark.parametrize('path, result', [('new_folder_1', 201),
                                              ('new_folder_2/new_folder_3',
                                               409),
                                              (':\\??', 400)
                                              ])
    def test_creating_folder(self, path, result):
        assert self.disk.create_new_folder(path) == result

# test for creating and cheking folder in disk
    def test_create_new_folder_c2(self):
        self.disk.create_new_folder('new_folder_4')
        assert 'new_folder_4' in self.disk.get_files_list()

# test for allready existing folder
    def test_create_exist_folder(self):
        self.disk.create_new_folder('new_folder_5')
        assert self.disk.create_new_folder('new_folder_5') == 409

    def teardown_class(cls):
        print('Testing completed')
