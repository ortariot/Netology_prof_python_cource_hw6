from selenium import webdriver
import time
# import pytest


class TestYaAuth:
    login = 'you_login'
    pas = 'you_password'
    delay = 1

    def setup_class(cls):
        print('stat testing')

    def teardown_class(cls):
        print('Testing completed')

    def test_work_login_page(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        id_text_box = driver.find_elements_by_class_name("Textinput-Control")
        id_text_box[0].click()
        id_text_box[0].send_keys("abc")
        enter_button = driver.find_element_by_id("passp:sign-in")
        enter_button.click()
        time.sleep(self.delay)
        assert driver.current_url == 'https://passport.yandex.ru/auth/welcome'
        driver.close()
        driver.quit()

    def test_work_login_page_bad_login(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        id_text_box = driver.find_elements_by_class_name("Textinput-Control")
        id_text_box[0].click()
        id_text_box[0].send_keys('!@#$%%')
        enter_button = driver.find_element_by_id("passp:sign-in")
        enter_button.click()
        time.sleep(self.delay)
        print(driver.page_source)
        hint = driver.find_element_by_id("field:input-login:hint")
        assert 'Такой логин не подойдет' == hint.text
        driver.close()
        driver.quit()

    def test_work_pas_page_empty_pas(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        id_text_box = driver.find_elements_by_class_name("Textinput-Control")
        id_text_box[0].click()
        id_text_box[0].send_keys('abc')
        enter_button = driver.find_element_by_id("passp:sign-in")
        enter_button.click()
        time.sleep(self.delay)
        pas_button = driver.find_element_by_id("passp:sign-in")
        pas_button.click()
        time.sleep(self.delay)
        hint = driver.find_elements_by_id("field:input-passwd:hint")
        assert hint[0].text == "Пароль не указан"
        driver.close()
        driver.quit()

    def test_work_pas_page_bad_pas(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        id_text_box = driver.find_elements_by_class_name("Textinput-Control")
        id_text_box[0].click()
        id_text_box[0].send_keys('abc')
        enter_button = driver.find_element_by_id("passp:sign-in")
        enter_button.click()
        time.sleep(self.delay)
        pas_text_box = driver.find_element_by_name("passwd")
        pas_text_box.click()
        pas_text_box.send_keys('12345')
        pas_button = driver.find_element_by_id("passp:sign-in")
        pas_button.click()
        time.sleep(self.delay)
        hint = driver.find_elements_by_id("field:input-passwd:hint")
        assert hint[0].text == "Неверный пароль"
        driver.close()
        driver.quit()

    def test_work_pas_page_good_pas(self):
        driver = webdriver.Chrome()
        driver.get('https://passport.yandex.ru/auth/')
        id_text_box = driver.find_elements_by_class_name("Textinput-Control")
        id_text_box[0].click()
        id_text_box[0].send_keys(self.login)
        enter_button = driver.find_element_by_id("passp:sign-in")
        enter_button.click()
        time.sleep(self.delay)
        pas_text_box = driver.find_element_by_name("passwd")
        pas_text_box.click()
        pas_text_box.send_keys(self.pas)
        pas_button = driver.find_element_by_id("passp:sign-in")
        pas_button.click()
        time.sleep(self.delay)
        assert driver.current_url == 'https://passport.yandex.ru/profile'
        driver.close()
        driver.quit()
