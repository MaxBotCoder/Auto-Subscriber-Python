#modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#variables
subscribers_desired = int(input("Enter the number of subscribers you want: "))
driver = webdriver.Chrome()
google_login_url = "https://accounts.google.com/lifecycle/steps/signup/name?continue=https://www.youtube.com/signin?action_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252Fwatch%253Fv%253Ds7u9wTtJ9Mk&dsh=S1662636084:1762120792162411&ec=65620&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en-GB&ifkv=ARESoU3U7Ao9ZsaiBc7RcxgBZDO10o9EF_Y9b6ijUw1K0O2GZIcy3yVh_MyNdPVuDzpMleCFZbCA&service=youtube&TL=ANzgctR99Orzzkb4GppBH1ZXPgHU2-PWMIDeZq9In5zONE_KqPwaWDwfR_iP9TWO"
revisions = 0
first_name = "Robyn"
last_name = "Alison"

#fucntions
def subscribe_function():
    print("filler")

def account_creation_function():
    driver.get(google_login_url)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div/div/div/button").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/input[1]").send_keys(first_name)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/input").send_keys(last_name)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div/div/div/button").click()
    time.sleep(2.5)
    
def call_function_function(repeats):
    for subscribe in range(repeats):
        account_creation_function()
        subscribe_function()

#call functions
call_function_function(subscribers_desired)
