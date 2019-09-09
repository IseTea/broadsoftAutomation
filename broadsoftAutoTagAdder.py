from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://myavoice.telesphere.com")

print(driver.title)
print(driver.current_url)

#Variables:
groupNames = ["TNL-Scottsdale", "TNL-Demo"]

#Enters UserID
elem = driver.find_element_by_name("EnteredUserID")
elem.clear()
elem.send_keys("INSERTADMINUSERNAMEHERE")

#Enters Password and logs in
elem = driver.find_element_by_name("INSERTADMINPASSWORDHERE")
elem.clear()
elem.send_keys("Lilt56Liev%^")
elem.send_keys(Keys.RETURN)

#Loops through groupNames list
for x in groupNames:
	#Goes to system level
	elem = driver.find_element_by_partial_link_text("System")
	elem.send_keys(Keys.RETURN)
	#Goes to group level
	elem = driver.find_element_by_partial_link_text("Groups")
	elem.send_keys(Keys.RETURN)
	#Searches for group name
	elem = driver.find_element_by_id("findValue0")
	elem.send_keys(x)
	elem.send_keys(Keys.RETURN)
	#Selects Group
	elem = driver.find_element_by_id("Row1Col0")
	elem.send_keys(Keys.RETURN)
	#Selects Utilities
	elem = driver.find_element_by_partial_link_text("Utilities")
	elem.send_keys(Keys.RETURN)
	#Selects Device Configuration
	elem = driver.find_element_by_partial_link_text("Device Conf")
	elem.send_keys(Keys.RETURN)
	#Selects VVX 300
	elem = driver.find_element_by_name("findValue")
	elem.send_keys("Polycom VVX")
	elem = driver.find_element_by_partial_link_text("Find")
	elem.send_keys(Keys.RETURN)
	elem = driver.find_element_by_partial_link_text("Polycom VVX 300")
	elem.send_keys(Keys.RETURN)
	#Selects Custom Tags Tab
	elem = driver.find_element_by_partial_link_text("Custom T")
	elem.send_keys(Keys.RETURN)
	time.sleep(5)


#driver.close()