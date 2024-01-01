from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import string
import numpy as np

class gamespot:
    def __init__(self, target_title, url, driver):
        self.url = url
        self.target_title = target_title
        self.driver = driver
        
    def start_driver(self):
        try:
            self.driver.get(self.url)
        except:
            self.driver = np.nan
        
    def cleaned_string(self, text):
        return text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()
    
    def find_xpath(self):
        #find top 3 search
        for i in range(1,4):
            try:
                xpath_title = f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[{i}]/div[2]/h4[1]/span[1]/a[1]"
                game_selector = self.driver.find_element(By.XPATH,xpath_title)
            except NoSuchElementException:
                xpath_title = f"/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/section[1]/ul[1]/li[{i+1}]/div[2]/h4[1]/span[1]/a[1]"
                game_selector = self.driver.find_element(By.XPATH,xpath_title)
            game_title = game_selector.text
            if self.cleaned_string(game_title) == self.target_title:
                return game_selector
        return np.nan
            
    def retrieve_score(self):
        try:
            self.game_selector.click()
        except:
            return ('Error', 'Error', 'Error')
            
        try:
            xpath_superscore = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/dl[1]/dt[1]/a[1]/div[1]/div[3]/div[1]/div[1]/span[1]"
            superscore = self.driver.find_element(By.XPATH,xpath_superscore).text
        except NoSuchElementException:
            superscore = np.nan
            
        try: 
            xpath_metacritic = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/dl[2]/dd[1]/a[1]"
            metacritic = self.driver.find_element(By.XPATH,xpath_metacritic).text
        except NoSuchElementException:
            metacritic = np.nan
            
        try:
            xpath_user = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/dl[3]/dd[1]/a[1]"
            user = self.driver.find_element(By.XPATH,xpath_user).text
        except NoSuchElementException:
            user = np.nan

        return superscore, metacritic, user
        
    def load_url(self):
        try:
            self.start_driver()
            if not pd.isna(self.driver):
                self.game_selector = self.find_xpath()
                if pd.isna(self.game_selector):
                    return (np.nan, np.nan, np.nan)
                else:
                    output = self.retrieve_score()
                    return output
            else:
                return ('Error', 'Error', 'Error')
        except NoSuchElementException:
            print(self.url, self.target_title)
            return (np.nan, np.nan, np.nan)
        

def main(x,y):
    data = pd.read_csv('data.csv')
    game_title = list(data['Title'].map(lambda x: x.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()))
    game_list = list(data['Title'].map(lambda x: x.lower().replace(" ","+")))
    url_list = ["https://www.gamespot.com/search/?q="+x for x in game_list]
    game = list(zip(game_title, url_list))
    edge_driver_path = r'driver/msedgedriver.exe'
    service = Service(executable_path=edge_driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Edge(service=service, options=options)
    history = []
    for title, url in game[x:y]:
        instance = gamespot(title, url, driver)
        history.append(instance.load_url())
    driver.quit()
    result = pd.DataFrame(history)
    result.to_csv(f"gamesplot_{x}_{y}.csv")

if __name__ == "__main__":
    start = int(input("Start: "))
    end = int(input("End: "))
    start_time = time.time()
    main(start, end)
    end_time = time.time()
    print("processing time",  end_time - start_time)