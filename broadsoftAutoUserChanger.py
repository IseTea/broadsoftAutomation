from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://myavoice.telesphere.com")

print(driver.title)
print(driver.current_url)

##VARIABLES:
userNames = ["4803394877", "3463277892"]

##ADMIN LOGIN BEGIN##
#Enters UserID
elem = driver.find_element_by_name("EnteredUserID")
elem.clear()
elem.send_keys("tpierce")
#Enters Password and logs in
elem = driver.find_element_by_name("Password")
elem.clear()
elem.send_keys("Lilt56Liev%^")
elem.send_keys(Keys.RETURN)
##ADMIN LOGIN END##

##LOOPS THROUGH USERNAME LIST##
for x in userNames:
	#Goes to system level
	elem = driver.find_element_by_partial_link_text("System")
	elem.send_keys(Keys.RETURN)
	#Goes to user search
	elem = driver.find_element_by_partial_link_text("Users")
	elem.send_keys(Keys.RETURN)
	#Enters username
	elem = driver.find_element_by_name("findValue0")
	elem.send_keys(x)
	elem.send_keys(Keys.RETURN)
	#Selects User
	elem = driver.find_element_by_id("Row1Col0")
	elem.send_keys(Keys.RETURN)
	time.sleep(3)
#driver.close()
