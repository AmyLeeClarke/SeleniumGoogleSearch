from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://google.in")

button = driver.find_element("xpath", '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div')
button.click()
searchBox = driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
searchBox.send_keys("GitHub")

searchclick = driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
searchclick.click()



