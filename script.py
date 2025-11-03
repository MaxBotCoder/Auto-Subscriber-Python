#modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#variables
subscribers_desired = int(input("Enter the number of subscribers you want: "))
email_filler = input("Put something random in for the email filler or this wont work \n a good example might be something \n like pancakeRuffloniePomoms something like that: ")
driver = webdriver.Chrome()
google_login_url = "https://accounts.google.com/lifecycle/steps/signup/name?continue=https://www.youtube.com/signin?action_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252Fwatch%253Fv%253Ds7u9wTtJ9Mk&dsh=S1662636084:1762120792162411&ec=65620&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en-GB&ifkv=ARESoU3U7Ao9ZsaiBc7RcxgBZDO10o9EF_Y9b6ijUw1K0O2GZIcy3yVh_MyNdPVuDzpMleCFZbCA&service=youtube&TL=ANzgctR99Orzzkb4GppBH1ZXPgHU2-PWMIDeZq9In5zONE_KqPwaWDwfR_iP9TWO"
revisions = 0
first_name = "Robyn"
last_name = "Alison"
password_filler = "A@B56tTQMOejeheui8hwu@U&*#GYDG&kshrdyeugqgwuyqenfeiqhjawiawjwjahw"

#fucntions
def subscribe_function():
    print("filler")

def get_email():
    if driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div/input"):
        print("!button detected!")
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div/input").click()
        print("clciked!")
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div[1]/div/div/button").click()
    elif driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div[1]/div/div[1]/input"):
        print("!input detected!")
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div[1]/div/div[1]/input").send_keys(email_filler)
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div[1]/div/div/button").click()
                
def create_password():
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(password_filler)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(password_filler)
    print("Sleep Started!")
    time.sleep(10)
    print("Its finished!")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div/div/div/button").click()

def account_creation_function():
    driver.get(google_login_url)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div/div/div/button").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/input[1]").send_keys(first_name)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/input").send_keys(last_name)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div/div/div/button").click()
    time.sleep(2.5)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/input").send_keys("1")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[1]").click()
    time.sleep(10)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/input").send_keys("2000")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[2]/div[1]/div[1]/div/div[1]/div").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[2]/div[1]/div[1]/div/div[2]/ul/li[2]").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[3]/div/div/div/div/button").click()
    time.sleep(10)
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/c-wiz/main/div[2]/div/div/div/form/span/section/div/div/div[2]/button").click()
    time.sleep(2.5)
    get_email()
    time.sleep(2.5)
    create_password()
    
def call_function_function(repeats):
    for subscribe in range(repeats):
        account_creation_function()
        subscribe_function()
        time.sleep(10.5)
        driver.quit()

#call functions
call_function_function(subscribers_desired)
