from selenium import webdriver
import time


driver = webdriver.Chrome() 
driver.get('https://passport.yandex.ru/auth/')
id_text_box = driver.find_elements_by_class_name("Textinput-Control")
# time.sleep(3)
# id_text_box.click()
# time.sleep(3)
id_text_box[0].click()
id_text_box[0].send_keys("abc")
enter_button = driver.find_element_by_id("passp:sign-in")
enter_button.click()
print(driver.window_handles[0].text)

# search_box.send_keys('ChromeDriver')
# search_box.submit()

# driver.quit()