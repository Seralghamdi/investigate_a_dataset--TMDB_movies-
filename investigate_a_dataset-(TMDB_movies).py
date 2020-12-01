#!/usr/bin/env python
# coding: utf-8

# # # Project: TMDb Movies Data Analysis
# 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>
# 
# ### In this report I am going to explore following questions :
# 
# ###### Question 1 (Which years do movies have the Highest budget?)
# 
# ###### Question 2 (What is the Average Revenue earned by the movies?)
# 
# ###### Question 3 Top 15 movies by the budget and runtime

# <a id='intro'></a>
# ## Introduction
# 

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# ### General Properties

# In[26]:


df=pd.read_csv('tmdb-movies.csv')
df.head()


# In[27]:


df.shape


# In[28]:


df.describe()


# In[29]:


df.info()


# In[30]:


df.isnull().sum()


# ### Data Cleaning (handling unused & missing values)

# In[40]:


df.hist(figsize=(10,8));


# In[31]:


#Deleting the columns that is not required
# list of columns that are to be deleted/dropped

df.drop(['imdb_id','cast','homepage','director','tagline','keywords','overview','production_companies'],axis=1,inplace=True)


# In[7]:


df.info()


# In[32]:


#the count of zeros in the budget and revenue columns 
df[['budget','revenue','release_year']].groupby('release_year').count()


# In[35]:


#drop zeros 
df.drop(df[df['revenue']==0].index,inplace=True)


# In[36]:


#show the number of rows after drop zeros
df.shape


# In[11]:


# i decided to drop all the missing values in geners rows
df.dropna(inplace=True)
df.info()


# In[38]:


#Delete duplicate rows in the dataset
df.duplicated().sum()


# In[39]:


df.drop_duplicates(inplace=True)
df.shape


# In[16]:


#change budget and revenue into integer
df['budget'] = df['budget'].astype(int)
df['revenue'] = df['revenue'].astype(int)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# 

# ### Question 1  (Which years do movies have the Highest budget?)
# 
# 

# In[41]:


#we going to group total budget by each years
budget_yr = df.groupby('release_year')['budget'].sum()
budget_yr.tail(10)


# In[47]:


#plot
budget_yr.plot(figsize = (10,6), color="red")
plt.xlabel('Movies released year')
plt.ylabel('Budget')
plt.title('the movies had the highest budget');


# ##### we can see that the last 10 years movies have the highest budget than other old years

# ### Question 2  (What is the Average of Revenue earned by the movies?)

# In[43]:


#first we're going to creat a new column called 'profit' 
df['profit'] =df['revenue'] - df['budget']

df['revenue'] = df['revenue'].astype(int)
df.head(1)


# In[44]:


# find average 
df['profit'].mean()


# ### Question 3 Top 15 movies by the budget and runtimes

# In[45]:


top_movies_budget = df['budget'].sort_values(ascending=False)[:15]
high_budget=pd.DataFrame()
titles_exp=[]
budgets=[]
for i in top_movies_budget.index:
    titles_exp.append(df.loc[i,'original_title'])
    budgets.append(top_movies_budget.loc[i])
high_budget['Titles']=titles_exp
high_budget['Budgets']=budgets
high_budget.set_index('Titles',inplace=True)
high_budget.plot(kind ='bar',figsize=(10,6), color='purple')
plt.title('Top 15 movies with the most budget ');
plt.ylabel('Budget in 100\'s of million');


# #### we can obviously see that the Warrior's Way movie has the highest budget
# 
# 

# In[46]:


# Create a histogram for movie runtimes.
plt.figure(figsize=(8,8), dpi=100)
df['runtime'].hist(rwidth = 0.9, bins =30)
plt.xlabel('Runtime')
plt.ylabel('Number of Movies')
plt.title('Runtime distribution of all the movies');


# #### 2500 movies have (1 hour 40 minutes) runtime

# <a id='conclusions'></a>
# ## Conclusions
# 
# 

# #### 1: at first question,this line chart depicts in which year do movies had the highest budget 
# #### it is clearly from the graph that the budget increased gradually from 2006-2013 after that there is a slighty decreased ,
# #### also we can cleary see the movies of 2013 have the highest budget .
# 
# 
# #### 2 : at second question ; the total profit is over 13 billions so i found the average of the profit is about 60 millions. which i think
# #### the budget must be around 60 millions for movies to be in successful criteria
# 
# 
# #### 3: Thierd question : this bar chart depicts the top 15 movies with the most budget in 100's of million . it is clear from the graph as an aggregate the budget of movies between (2.5-3) but the most budget as we can see was for ( Warrior's Way movie (2010) )
# 
# ### Top 15 movies by runtime
# #### I created a histogram to see the runtime distributions of all the movies and it is clear from the graph 2500 movies have ( 1 hour 40 minutes ) after there are over 1500 movies have about 2 hours runtime .

# #### Limitaions:
# #####  there are many  droped  rows contained 0 values and null values.
# ##### The dataset was cut by few thousand rows of movies, which would definitly affect the result.
# ##### the budget and revenue column do not have currency unit, it might be possible different movies have budget in different currency according to the country they are produce in.
# 
# 

# In[ ]:




