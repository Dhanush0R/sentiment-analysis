from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/?ref_=nv_home")
search = driver.find_element(By.CSS_SELECTOR, "#suggestion-search")
search.send_keys("the avengers 2012")
search.submit()
movie_id = driver.find_element(By.CSS_SELECTOR, value="li a")
movie_id.click()
review_section = driver.find_elements(By.CSS_SELECTOR, value="ul li a")
review_section[1].click()
review_data = driver.find_elements(By.CSS_SELECTOR, value=".content .text")
# reviews = [i.text for i in review_data]
with open("read.txt", mode='w', encoding="utf-8") as file:
    for i in review_data:
        # print(i.text)
        file.write(i.text)
        # print()
# print(reviews)
