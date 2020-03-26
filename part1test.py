
# coding = utf-8
#1 database wirte for the register and log in
from selenium import webdriver
import time

#case 1.1 language select chinese(original)-english-chinese/ times:5 
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("english").click()
    time.sleep(2)
    browser.find_element_by_name("chinese").click()
    time.sleep(3)
    browser.quit()


#case 2.1 login in success/ times:5 
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("username").send_keys("sun")
    browser.find_element_by_name("password").send_keys("123456")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    browser.quit()
#case 2.2 login in failure with wrong password/ 5 times
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("username").send_keys("sun")
    browser.find_element_by_name("password").send_keys("1111")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    browser.quit()
#case 2.3 login in failure with wrong username/ 5 times
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("username").send_keys("s")
    browser.find_element_by_name("password").send_keys("123456")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    browser.quit()


#case 3.1 user registration success/ times:5 
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("new").click()
    time.sleep(2)
    newuser='new'+str(num)
    browser.find_element_by_name("username").send_keys(newuser)
    browser.find_element_by_name("password").send_keys("123456")
    browser.find_element_by_name("password2").send_keys("123456")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    browser.quit()
#case 3.2 user registration failer with not same password/ times:5 
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("new").click()
    time.sleep(2)
    newuser='newwrong'+str(num)
    browser.find_element_by_name("username").send_keys(newuser)
    browser.find_element_by_name("password").send_keys("123456")
    browser.find_element_by_name("password2").send_keys("111111")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    browser.quit()
#case 3.3 user registration failer with already exist user/ times:5 
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("new").click()
    time.sleep(2)
    browser.find_element_by_name("username").send_keys("sun")
    browser.find_element_by_name("password").send_keys("123456")
    browser.find_element_by_name("password2").send_keys("123456")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(3)
    browser.quit()
