#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:41:42 2020

@author: mohinivembu
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

### 2020
driver = webdriver.Chrome(
        '/Users/mohinivembu/Documents/Roger Federer/chromedriver')
driver.get('https://www.atptour.com/en/players/roger-federer/f324/player-activity?year=all')

out_data = pd.DataFrame()
wait = WebDriverWait(driver,10)

### click into match stats and extract info

all_tourn = driver.find_elements(By.CLASS_NAME,'activity-tournament-table')
all_match = driver.find_elements(By.CLASS_NAME,'day-table-name')
dates = driver.find_elements(By.CLASS_NAME, 'tourney-dates')


for i in range(len(all_tourn)):
    t1_elements = driver.find_element(
   By.XPATH,'//*[@id="currentTabContent"]/div[3]/div['+str(i + 1)+']/table[1]/tbody')
    t2_elements = driver.find_element(
   By.XPATH,'//*[@id="currentTabContent"]/div[3]/div['+str(i + 1)+']/table[2]/tbody')
    n_match = len(t2_elements.find_elements(By.CLASS_NAME, 'day-table-name')) 
    ### PULL DATES, LOCATION, SURFACE, NAME                                                
    location = t1_elements.find_elements(By.CLASS_NAME, 'tourney-location')[0].text
    dates = t1_elements.find_elements(By.CLASS_NAME, 'tourney-dates')[0].text   
    surface = t1_elements.find_elements(By.CLASS_NAME, 'tourney-dates')[0].text
    name = t1_elements.find_elements(By.CLASS_NAME, 'tourney-title')[0].text
    surface = t1_elements.find_element(By.XPATH,
    'tr/td[3]/table/tbody/tr/td[2]/div[2]/div/span').text      
                                       
    for j in range(n_match):
        match_id = j
        ### CLICK INTO THE MATCH
        ##### if there's nothing to click, skip to next iteration
        try:
            link = wait.until(expected_conditions.element_to_be_clickable((
                    By.XPATH, 
    '//*[@id="currentTabContent"]/div[3]/div['+str(i + 1)+']/table[2]/tbody/tr['+str(j+1)+']/td[5]/a')))
            link.click()
        except (TimeoutException, ElementClickInterceptedException):
            continue
        
        ### IDENTIFY THE WINNER AND LOSER
        ##### if there is no data, skip to next iteration and go back to OG page
        try:
            winner_1= wait.until(
                    expected_conditions.visibility_of_element_located((
                            By.CLASS_NAME,'player-left-name')))
            winner = winner_1.text
        except (TimeoutException, NoSuchElementException):
            driver.back()
            continue
                
        loser = wait.until(
            expected_conditions.visibility_of_element_located((
                    By.CLASS_NAME,'player-right-name'))).text
                
        ### MATCH ROUND, TOURNAMENT, AND TIME
        trn_round = wait.until(
                expected_conditions.visibility_of_element_located((
        By.XPATH,
        '//*[@id="completedScoreBox"]/div/div/div/table/caption/span[1]'))).text
        
        match_time = wait.until(
        expected_conditions.visibility_of_element_located((
        By.CLASS_NAME,'time'))).text            

        header = wait.until(
                expected_conditions.visibility_of_element_located((
        By.XPATH,
        '//*[@id="match-stats-container"]/div[1]/h3'))).text.split("| ")[1]

        ### TABLE WITH KEY MATCH STATS
        list_elements = driver.find_element(
        By.XPATH,'//*[@id="completedMatchStats"]/table/tbody')
        ##### Stat Labels
        stat = list()
        links = list_elements.find_elements(By.CLASS_NAME,"match-stats-label")
        for k in range(len(links)):
            stat.append(links[k].text)

        ##### Stats for winner
        win_val = list()
        links = list_elements.find_elements(By.CLASS_NAME,"match-stats-number-left")
        for k in range(len(links)):
            win_val.append(links[k].text)

        ##### Stats for lower seeded player
        loser_val = list()
        links = list_elements.find_elements(By.CLASS_NAME,"match-stats-number-right")
        for k in range(len(links)):
            loser_val.append(links[k].text)
        
        ### JOIN INTO A DATASET    
        match_data = pd.DataFrame(
            {'match_id':match_id,
             'tournament':header,
             'match_time': match_time,
             'round' : trn_round,
             'stats': stat,
             'winner': winner,
             'loser': loser,
             'winner_stat':win_val,
             'loser_stat':loser_val,
             'tourn_dates': dates,
             'location': location,
             'surface': surface,
             'tourn_name':name,
             })
    
        ### COMBINE WITH EXISTING DATA
        out_data = pd.concat([out_data, match_data])
        
        ### RETURN TO ORIGINAL PAGE
        driver.back()

            
out_data.to_csv('/Users/mohinivembu/Documents/Roger Federer/Data/Raw Out.csv')
