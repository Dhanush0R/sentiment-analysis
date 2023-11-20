from selenium import webdriver
from selenium.webdriver.common.by import By

class ReviewExtraction:
    def __init__(self, movie_name):
        self.chrome_options = self.chrome_settings()
        self.movie = movie_name
    def chrome_settings(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", False)
        return chrome_options

    def extraction(self):
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.get("https://www.imdb.com/?ref_=nv_home")
        search = driver.find_element(By.CSS_SELECTOR, "#suggestion-search")
        search.send_keys(self.movie)
        search.submit()
        movie_id = driver.find_element(By.CSS_SELECTOR, value="li a")
        movie_id.click()
        review_section = driver.find_elements(By.CSS_SELECTOR, value="ul li a")
        review_section[1].click()
        review_data = driver.find_elements(By.CSS_SELECTOR, value=".content .text")
        # reviews = [i.text for i in review_data]
        with open("read.txt", mode='w', encoding="utf-8") as file:
            for rev in review_data:
                # print(i.text)
                file.write(rev.text)
        # print()
# print(reviews)

# ree = ReviewExtraction("avengers endgame")
# ree.extraction()