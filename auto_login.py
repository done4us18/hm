from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = 'chromedriver.exe' ##Same Directory as Python Program

driver = webdriver.Chrome(executable_path=PATH)


##### Login Functions 
def login_fb(fid,fpsd):
    driver.get("https://www.facebook.com/")

    def login(id,password):
        email = driver.find_element_by_id("email")
        email.send_keys(id)
        Password = driver.find_element_by_id("pass")
        Password.send_keys(password)
        button = driver.find_element_by_id("u_0_d_Dw").click()
        pass

    login(fid,fpsd)

### Like Facebook Write Login Function For Other Platforms Too.
def login_insta():
    pass

def login_medium():
    pass

def login_twitter():
    pass

def login_linkedin():
    pass


login_fb("YOUR_LOGIN_ID", "YOUR_PASSWORD")
login_insta()
login_medium()
login_twitter()
login_linkedin()
