
# coding = utf-8
#1 database wirte for the register and log in
from selenium import webdriver
import time
import os
#case 3.1 upload post/ times:5 
for num in range(1,6):
    browser = webdriver.Firefox()
    browser.get("http://localhost:8080/")
    time.sleep(2)
    browser.find_element_by_name("username").send_keys("sun")
    browser.find_element_by_name("password").send_keys("123456")
    time.sleep(2)
    browser.find_element_by_class_name("btn").click()
    time.sleep(2)
    browser.find_element_by_name("photo").click()
    #upload
    os.system(r"C:\Users\admin\Desktop\test\upload.exe") 
    time.sleep(2)
    browser.find_element_by_name("share").click()
    


