from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import string
import numpy as np
import re

class metacritic:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.error = []
        
    def start_driver(self):
        try:
            self.driver.get(self.url)
        except:
            self.error.append('the driver cannot get into the link')
            self.driver = np.nan
            
    def retrieve_score(self):
        try:
            xpath_metascore = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]"
            metascore = self.driver.find_element(By.XPATH,xpath_metascore).text
        except NoSuchElementException:
            self.error.append('unable to get the rating')
            metascore = np.nan
        try:
            xpath_user = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]"
            user = self.driver.find_element(By.XPATH,xpath_user).text
        except NoSuchElementException:
            self.error.append('unable to get the user rating')
            user = np.nan
        return metascore, user
        
    def load_url(self):
        try:
            self.start_driver()
            if not pd.isna(self.driver):
                output = self.retrieve_score()
                return output
            else:
                return (np.nan, np.nan)
        except NoSuchElementException:
            self.error.append('some other error happen')
            return (np.nan, np.nan)
        
    def get_log(self):
        return self.error
        
        
def main(x,y):
    data = pd.read_csv('data.csv')
    data['Title'] = data['Title'].map(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())
    data['Title'] = data['Title'].map(lambda x: re.sub(r'\s+', ' ', x))
    game_list = list(data['Title'].map(lambda x: x.lower().strip().replace(" ","-")))
    url_list = ["https://www.metacritic.com/game/"+x for x in game_list]
    game = url_list
    
    edge_driver_path = r'driver/msedgedriver.exe'
    service = Service(executable_path=edge_driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Edge(service=service, options=options)
    history = []
    log = []
    for url in game[x:y]:
        instance = metacritic(url, driver)
        history.append(instance.load_url())
        log.append(instance.get_log())
    driver.quit()
    result = pd.DataFrame(history)
    result['log'] = pd.Series(log)
    result.to_csv(f"metacritic/metacritic_{x}_{y}.csv")
    

if __name__ == "__main__":
    start = int(input("Start: "))
    end = int(input("End: "))
    start_time = time.time()
    main(start, end)
    end_time = time.time()
    print("processing time",  end_time - start_time)