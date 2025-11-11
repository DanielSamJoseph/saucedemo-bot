from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user="standard_user"
password="secret_sauce"



driver=webdriver.Chrome()

driver.get("https://www.saucedemo.com/")#Opens the saucedemo login page
time.sleep(5)
#types the username in the username field
elem=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
elem.clear()
elem.send_keys(user)

elem=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
elem.clear()
elem.send_keys(password)
time.sleep(5)

#clicks the login button
login=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
login.click()
time.sleep(10)

#clicks on the first product to the cart
product=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
product.click()
time.sleep(5)

#then logs out
threebars=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
threebars.click()
time.sleep(2)

logout=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]")
logout.click()
time.sleep(5)
