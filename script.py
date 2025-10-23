from selenium import webdriver
from selenium.webdriver.common.by import By

number_of_bot_loops = int(input("Enter the number of subscribers you want: "))
print(f"You will now recieve {number_of_bot_loops} subscribers")

#driver = webdriver.Chrome()

for subscriber_loop in range(number_of_bot_loops):
    driver = webdriver.Chrome()
    driver.get("https://youtube.com")
    print(f"{driver.title} has been opened!")
    driver.quit()
    
print("Process completed!")
