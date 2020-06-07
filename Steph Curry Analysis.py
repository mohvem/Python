#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import numpy
import pandas as pd
import string

steph = pd.read_csv('/Users/mohinivembu/Documents/Steph Curry Project/Steph Curry Stats.csv',
                    header = 0)
pd.options.mode.chained_assignment = None
### Clean up the Data
steph = steph.drop(columns = ['Unnamed: 0', 'Tm'])
steph = steph.rename(columns = {'Result':'Score'})
steph['Result'] = numpy.where(steph['Score'].str.contains(pat = 'L'), 'Loss','Win')

### Home v Away
home = steph[pd.isnull(steph.Away)]
away = steph[pd.notnull(steph.Away)]

home = home.drop(columns = ['Away', 'GS', 'G#', 'Score', 'MP', 'PF'])
away = away.drop(columns = ['Away', 'GS', 'G#', 'Score', 'MP', 'PF'])

##### Reshape the datasets so that they are long in the statistic 
home_long = pd.melt(home, id_vars = ['Date','Result','Season','Series', 'Opp','GmSc', 'G'],
                    var_name = 'statistic')
away_long = pd.melt(away, id_vars = ['Date','Result','Season','Series', 'Opp', 'GmSc', 'G'],
                    var_name = 'statistic')
home_long['Location'] = 'Home'
away_long['Location'] = 'Away'
stacked = pd.concat([home_long,away_long], axis = 0)

### Clean up data so no missing values and clean up syntax, collapse similar teams
stacked = stacked[stacked['value'].notnull()]
unique_stats = stacked.drop_duplicates(subset = ['statistic'])
print(stacked.dtypes)
stacked['value'] = stacked['value'].astype(str).astype(float)
stacked['Opp'] = numpy.where(stacked['Opp'] == 'NJN', 'BRK', stacked['Opp'])
stacked['Opp'] = numpy.where(stacked['Opp'] == 'CHO', 'CHA', stacked['Opp'])
stacked['Opp'] = numpy.where(stacked['Opp'] == 'NOH', 'NOP', stacked['Opp'])
tms = stacked.drop_duplicates(subset = ['Opp'])
print(stacked.dtypes)

##### Summarize the various statistics by opponent, and location

stacked_grp = stacked.groupby(by = ['statistic','Location', 'Opp'])
game_results = stacked_grp['Result'].value_counts()
game_results = game_results.to_frame().rename(columns = {'Result':'N Games'}).reset_index().drop(columns = ['statistic']).drop_duplicates()

##### for each team, summarize by all games, and home, and away games
sum_stats_h_a = stacked_grp['value'].agg({'mean':numpy.mean,
                       'std':numpy.std,
                       'max':numpy.max,
                       'min':numpy.min,
                       'median':numpy.median}).reset_index()
n_games1 = stacked_grp['value'].size().reset_index(name = 'n_games')
sum_stats_h_a = sum_stats_h_a.merge(how = "left", right = n_games1, on = ['statistic', 'Location',
                                                                 'Opp'])
sum_stats_all = stacked.groupby(by = ['statistic','Opp'])['value'].agg({'mean':numpy.mean,
                       'std':numpy.std,
                       'max':numpy.max,
                       'min':numpy.min,
                       'median':numpy.median}).reset_index()
n_games2 = stacked.groupby(by = ['statistic','Opp'])['value'].size().reset_index(name = 'n_games')
sum_stats_all = sum_stats_all.merge(how = "left", right = n_games2, on = ['statistic', 'Opp'])

##### summarize by all home, all away, and overall
h_a_games = stacked.groupby(by = ['statistic', 'Location'])['value'].agg({'mean':numpy.mean,
                       'std':numpy.std,
                       'max':numpy.max,
                       'min':numpy.min,
                       'median':numpy.median}).reset_index()
overall = stacked.groupby(by = ['statistic'])['value'].agg({'mean':numpy.mean,
                       'std':numpy.std,
                       'max':numpy.max,
                       'min':numpy.min,
                       'median':numpy.median}).reset_index()
n_games = stacked.groupby(by = ['statistic', 'Location'])['value'].size().reset_index(name = 'n_games')
n_games2 = stacked.groupby(by = ['statistic'])['value'].size().reset_index(name = 'n_games')
h_a_games = h_a_games.merge(how = "left", right = n_games, on = ['statistic', 'Location'])
overall = overall.merge(how = "left", right = n_games2, on = ['statistic'])

### Set up the Data for analysis
overall['Location'] = 'All Games'
sum_stats_all['Location'] = 'All Games'
all_games = pd.concat([h_a_games, overall], axis = 0)
sum_stats_team = pd.concat([sum_stats_h_a, sum_stats_all]).sort_values(by = ['Opp','statistic','Location'])

##### for each team there are 3 comparisons I care about
##### Team Home Game v overall home performance - are there teams he performs better/worse against at home?
##### Team Game v overall performance - are there teams where he does better/worse than usual?
##### Team Away Game v overall away performance - are there certain away venues that are particularly tough?
def setup(indata, suffix):
    comp = indata.merge(how = "left", right = all_games, on = ['statistic', 'Location'],
                       suffixes = ['', suffix])
    comp = pd.melt(comp, id_vars = ['Opp','Location', 'statistic', 'n_games' + suffix, 'n_games'], 
                   var_name = 'sum_stat')
    reg = comp['sum_stat'].str.contains(suffix, regex = True)
    comp_tm = comp[~reg].drop(columns = ['n_games' + suffix])
    comp_cmp = comp[reg].drop(columns = ['n_games'])
    comp_cmp['sum_stat'] = comp_cmp['sum_stat'].str.replace(suffix,'')
    comp_mrg = comp_tm.merge(how = "left", right = comp_cmp, on = ['statistic', 'Opp', 'sum_stat'],
                         suffixes = ['', suffix]).sort_values(['Opp', 'statistic', 'sum_stat'])  
    return(comp_mrg)
comp1 = setup(sum_stats_team[sum_stats_team['Location'] == 'Home'], '_home')
comp2 = setup(sum_stats_team[sum_stats_team['Location'] == 'All Games'], '_all')
comp3 = setup(sum_stats_team[sum_stats_team['Location'] == 'Away'], '_away')

### Difference in statistics
### which stats is higher dif better?
higher_better= ['+/-', 'PTS', 'ORB', 'DRB', 'TRB', 'BLK', 'STL',
              'AST', '3P', '3PA','3P%', 'FG', 'FGA','FG%',
              'FT', 'FT%', 'FTA']
lower_better = ['TOV']

def difs(indata,suffix):
    difs = indata.assign(dif = indata['value'] - indata['value' + suffix])
    difs['Perf'] = numpy.where(difs['statistic'].isin(higher_better),
        numpy.where(difs['dif'] > 0, 'Does Better vs. Team',
                    'Does Worse vs. Team'), 
                    numpy.where(difs['dif'] > 0,
                               'Does Worse vs. Team',
                               'Does Better vs. Team'))
    return(difs)

comp1_difs = difs(comp1, '_home')
comp2_difs = difs(comp2, '_all')
comp3_difs = difs(comp3, '_away')

### Which Metrics does he do better/worse in? Let's only look at mean here.
def perf(indata):
    better = indata[indata['Perf'] == 'Does Better vs. Team'].sort_values(
            by = ['Opp', 'statistic', 'sum_stat'])
    worse = indata[indata['Perf'] == 'Does Worse vs. Team'].sort_values(
            by = ['Opp', 'statistic', 'sum_stat'])
    return(better,worse)
perf1_better, perf1_worse = perf(comp1_difs)
perf2_better, perf2_worse = perf(comp2_difs)
perf3_better, perf3_worse = perf(comp3_difs)

### Output
writer = pd.ExcelWriter('Comps.xlsx', engine='xlsxwriter')

perf1_better.to_excel(writer, sheet_name = "1.Better")
perf1_worse.to_excel(writer,sheet_name = "1.Worse")
perf2_better.to_excel(writer,sheet_name = "2.Better")
perf2_worse.to_excel(writer,sheet_name = "2.Worse")
perf3_better.to_excel(writer,sheet_name = "3.Better")
perf3_worse.to_excel(writer,sheet_name = "3.Worse")

writer.save()

stacked.to_excel('All Data Long.xlsx')
