#!/usr/bin/env python
# coding: utf-8

# In[23]:


from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlite3
import random

APP = Flask(__name__)


# In[53]:


# db build for query
# Creating SQLite DB for NBA draft Data

# import data from data.world website
nba = pd.read_csv('https://query.data.world/s/rfugrlxorfagiv2cxyac6rujtzz6fw')

# create sqlite db
conn = sqlite3.connect('nba_db3.sqlite3')

# create cursor to db
c = conn.cursor()

# create table players
# c.execute("""CREATE TABLE PLAYERS(
#            [Unnamed: 0] integer,  [Player], [All_NBA] integer, [All.Star] integer,
#            [Draft_Yr] integer, [Pk] integer,
#            [Team] text,[College] text,
#            [Yrs] integer, [Games] integer, [Minutes.Played] integer,
#            [PTS] integer, [TRB] integer, [AST] integer,
#            [FG_Percentage] real, [TP_Percentage] real, [FT_Percentage] real,
#            [Minutes.per.Game] real,
#            [Points.per.Game] real, [TRB.per.game] real, [Assits.per.Game] real,
#            [Win.Share] integer,
#            [WS_per_game] real, [BPM] real, [VORP] real, [Executive] text,
#            [Tenure] date, [Exec_ID] integer,
#            [Exec_draft_exp] integer, [attend_college] integer, [first_year] integer,
#            [second_year] integer,
#            [third_year] integer, [fourth_year] integer, [fifth_year] integer)"""
#            )


# In[22]:


# loop for players to add to db
for player in range(len(nba)):
  sequence = (tuple(nba.loc[player].values))
  insert_player = """INSERT INTO "main"."PLAYERS"
        VALUES """ + str(sequence) + ';'
  c.execute(insert_player)


# In[ ]:


# ('Unnamed: 0', 'Player', 'All_NBA', 'All.Star', 'Draft_Yr', 'Pk', 'Team',
#            'College', 'Yrs', 'Games', 'Minutes.Played', 'PTS', 'TRB', 'AST',
#            'FG_Percentage', 'TP_Percentage', 'FT_Percentage', 'Minutes.per.Game',
#            'Points.per.Game', 'TRB.per.game', 'Assits.per.Game', 'Win.Share',
#            'WS_per_game', 'BPM', 'VORP', 'Executive', 'Tenure', 'Exec_ID',
#            'Exec_draft_exp', 'attend_college', 'first_year', 'second_year',
#            'third_year', 'fourth_year', 'fifth_year')


# In[ ]:


### IDEA FLOW###

# Query to show stats result of player

# Then pull from model to show similar players


# In[54]:


# use given info to search for (a) given player info (b) model prediction
player = nba['Player'].sample(1).values[0]
print("Player selected: ", player)


# In[55]:


# (a)send searched player info to webpage
nba.loc[nba['Player'] == player]


# In[56]:


# (b) send info to model
# model sends back names
player_abc = nba['Player'].sample(3).values[:]
player_abc


# In[52]:


# for loop to predicted player details
predict_players = []
for single in player_abc:
    finder = nba.loc[nba['Player'] == single]
    predict_players.append(finder)
    
print("Predict players: ", predict_players)


# In[48]:

query = """SELECT *
FROM PLAYERS"""
c.execute(query)
player_test = c.fetchall()
print("This is a player test: ", player_test)


# In[ ]:




