#modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#vaiables
driver = webdriver.Chrome()
loop = input("How many subscribers do you want? >>")
number_of_revisions = 0
first_name = "monica"
last_name = "geller"

#functions
def create_account():
    driver.get()
    
def login():
    print("test!")

#call functions
create_account()
