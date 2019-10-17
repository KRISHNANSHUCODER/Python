from selenium import webdriver
browser = webdriver.Chrome("C:\\Users\\ASUS\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe")
browser.get("http://www.seleniumhq.org")
elem=browser.find_element_by_link_text("Download")
elem.click()
search = browser.find_element_by_id("q")
search.send_keys("HELLO")