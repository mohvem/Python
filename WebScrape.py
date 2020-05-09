#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string


url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2019'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[33:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2019 = pd.DataFrame(player_stats2, columns = txt)
stats_2019['Season'] = '2018-2019'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2018'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[32:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2018 = pd.DataFrame(player_stats2, columns = txt)
stats_2018['Season'] = '2017-2018'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2017'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[33:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2017 = pd.DataFrame(player_stats2, columns = txt)
stats_2017['Season'] = '2016-2017'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2016'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[34:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2016 = pd.DataFrame(player_stats2, columns = txt)
stats_2016['Season'] = '2015-2016'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2015'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[34:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2015 = pd.DataFrame(player_stats2, columns = txt)
stats_2015['Season'] = '2014-2015'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2014'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[35:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2014 = pd.DataFrame(player_stats2, columns = txt)
stats_2014['Season'] = '2013-2014'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2013'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[35:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2013 = pd.DataFrame(player_stats2, columns = txt)
stats_2013['Season'] = '2012-2013'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2012'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[32:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2012 = pd.DataFrame(player_stats2, columns = txt)
stats_2012['Season'] = '2011-2012'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2011'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[33:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2011 = pd.DataFrame(player_stats2, columns = txt)
stats_2011['Season'] = '2010-2011'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2010'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:30]]
rows = soup.findAll('tr')[36:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 29:
        index.append(i)

player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_2010 = pd.DataFrame(player_stats2, columns = txt)
stats_2010['Season'] = '2009-2010'

url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog-playoffs/'
html = urlopen(url)
soup = BeautifulSoup(html)
soup.findAll('th')
txt = [th.getText() for th in soup.findAll('th')[1:31]]
rows = soup.findAll('tr')[37:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
index = []
for i in range(len(player_stats)):
    length = len(player_stats[i])
    if length == 30 and player_stats[i][1] != '':
        index.append(i)
        
player_stats2 = [player_stats[i] for i in index] ### remove inactive 
stats_po = pd.DataFrame(player_stats2, columns = txt)
stats_po['Season'] = 'Playoff'
stats_po['Date'] = stats_po['2013 Playoffs']
stats_po = stats_po.drop(columns = ['2013 Playoffs'])
names_po = stats_po.columns.tolist()
names_po[3] = 'Away'
names_po[6] = 'Result'
stats_po.columns = names_po

### Bind Rows
all_stats = stats_2010
all_stats = all_stats.append(stats_2011)
all_stats =all_stats.append(stats_2012)
all_stats =all_stats.append(stats_2013)
all_stats =all_stats.append(stats_2014)
all_stats =all_stats.append(stats_2015)
all_stats =all_stats.append(stats_2016)
all_stats =all_stats.append(stats_2017)
all_stats =all_stats.append(stats_2018)
all_stats =all_stats.append(stats_2019)

all_stats['Series'] = 'Regular Season'
all_stats['G#'] = 1
all_stats = all_stats.drop(columns = ['Age'])
names_all = all_stats.columns.tolist()
names_all[3] = 'Away'
names_all[5] = 'Result'
all_stats.columns = names_all
all_stats = pd.concat([all_stats,stats_po], axis = 0)

all_stats.to_csv('/Users/mohinivembu/Documents/Steph Curry Project/Steph Curry Stats.csv')



