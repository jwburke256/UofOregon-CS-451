from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
 
url = 'https://angular.io/' 

service = webdriver.FirefoxService(executable_path="/usr/sbin/firefox")
driver = webdriver.Firefox(service=service)

driver.get(url) 
 
print(driver.page_source)
