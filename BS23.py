from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#------------------------------------LINK TO THE WEBSITE-----------------------

driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(30)

#---------------------------------------SIGN IN-------------------------------
link = driver.find_element_by_link_text("Sign in")
link.click()

#-------------------------------------CREATE EMAIL--------------------------------

email = driver.find_element_by_id("email_create")
email.send_keys("humayratasnim05@gmail.com")
email.send_keys(Keys.RETURN)

#-----------------------------YOUR PERSONAL INFORMATION-------------------------

title = driver.find_element_by_id("id_gender2")
title.click()

first_name = driver.find_element_by_id("customer_firstname")
first_name.send_keys("Humayra Tasnim")

last_name = driver.find_element_by_id("customer_lastname")
last_name.send_keys("Rahman")


email_id = driver.find_element_by_id("email")
email_id.clear()
email_id.send_keys("humayratasnim05@gmail.com")

password = driver.find_element_by_id("passwd")
password.send_keys("123456")

date = Select(driver.find_element_by_id("days"))
date.select_by_value("10")

months = Select(driver.find_element_by_id("months"))
months.select_by_value("8")

years = Select(driver.find_element_by_id("years"))
years.select_by_value("1985")

newsletter = driver.find_element_by_id("newsletter")
newsletter.click()

#--------------------------------YOUR ADDRESS------------------------------

f_name = driver.find_element_by_id("firstname")
f_name.clear()
f_name.send_keys("Humayra Tasnim")

L_name = driver.find_element_by_id("lastname")
L_name.clear()
L_name.send_keys("Rahman")

company = driver.find_element_by_id("company")
company.send_keys("Brain Station 23")

address1 = driver.find_element_by_id("address1")
address1.send_keys("Mohakhali")

city = driver.find_element_by_id("city")
city.send_keys("Mesa")

id_state = Select(driver.find_element_by_id("id_state"))
id_state.select_by_value("3")

postal_code = driver.find_element_by_id("postcode")
postal_code.send_keys("85201")

country = Select(driver.find_element_by_id("id_country"))
country.select_by_value("21")

add_info = driver.find_element_by_id("other")
add_info.send_keys("I am interested in this website")

home_phone = driver.find_element_by_id("phone")
home_phone.send_keys("+8801713031133")

mobile_phone = driver.find_element_by_id("phone_mobile")
mobile_phone.send_keys("+8801625724248")

address2 = driver.find_element_by_id("alias")
address2.clear()
address2.send_keys("Dhaka,Bangladesh")

reg = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button")
reg.click()

sign_out = driver.find_element_by_link_text("Sign out")
sign_out.click()

#--------------------------------VERFICATION-----------------------------------------

driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(30)

link1 = driver.find_element_by_link_text("Sign in")
link1.click()

email_confirm = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input")
email_confirm.send_keys("humayratasnim05@gmail.com")

password_confirm = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[2]/span/input")
password_confirm.send_keys("123456")

sign_in = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span")
sign_in.click()

Signout = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a")
Signout.click()
