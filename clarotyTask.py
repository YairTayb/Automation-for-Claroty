from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#initializing the webdriver
driver = webdriver.Chrome()#initializing the chrome webdriver.
driver.get("https://www.google.co.il/")


#type in the search line and send an enter.
searchQuery = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
searchQuery.send_keys("claroty")
searchQuery.send_keys(Keys.ENTER)
result=driver.find_element_by_xpath("//*[@id='resultStats']")
print("Current nubmer of results when searching: "+result.text[2:(result.text.index(' '))])

#first link info collecting.
siteData=driver.find_element_by_xpath("//*[@id='rso']/div/div/div[1]/div/div/div[1]/a[1]")

if(siteData.get_attribute("href")!="https://www.claroty.com/"):
	print("first link is not claroty!")
else:
	siteData.click()

#count the amount of jobs currently opened.
driver.get("https://www.claroty.com/careers")
jobsList=driver.find_elements_by_class_name("w-dyn-item")
print("Claroty currently has "+str(len(jobsList))+" jobs available.")

