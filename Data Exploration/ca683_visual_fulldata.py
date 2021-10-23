#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

path = 'F:/MCM 2020_2021/CA683/yelp data set/YelpData1719.csv'
#review_col_list2 = ["review_id","stars","text","useful"]
#df = pd.read_csv(path, usecols=review_col_list2)
df = pd.read_csv(path)

#df = pd.read_pickle('F:/MCM 2020_2021/CA683/yelp data set/20210411/restaurant_len_useful_wo0_data.txt')


# In[58]:


df.head(5)


# In[2]:


df.info()


# In[40]:


df = df[~df['text'].isnull()]c


# In[41]:


def preprocess(ReviewText):
    ReviewText = ReviewText.str.replace("(<br/>)", "")
    ReviewText = ReviewText.str.replace('(<a).*(>).*(</a>)', '')
    ReviewText = ReviewText.str.replace('(&amp)', '')
    ReviewText = ReviewText.str.replace('(&gt)', '')
    ReviewText = ReviewText.str.replace('(&lt)', '')
    ReviewText = ReviewText.str.replace('(\xa0)', ' ')  
    return ReviewText


# In[42]:


df['text'] = preprocess(df['text'])


# In[43]:


df['review_len'] = df['text'].astype(str).apply(len)
df['word_count'] = df['text'].apply(lambda x: len(str(x).split()))


# In[44]:


import plotly
import plotly.graph_objs as go
from plotly.offline import iplot


# In[8]:


import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


# In[45]:


df['stars'].iplot(
    kind='hist',
    xTitle='rating',
    linecolor='black',
    yTitle='count',
    title='Review Rating Distribution')


# In[46]:


df['review_len'].iplot(
    kind='hist',
    bins=100,
    xTitle='review length',
    linecolor='black',
    yTitle='count',
    title='Review Text Length Distribution')


# In[10]:


df['word_count'].iplot(
    kind='hist',
    bins=100,
    xTitle='word count',
    linecolor='black',
    yTitle='count',
    title='Review Text Word Count Distribution')


# In[47]:


#The distribution of "useful"
df.groupby('useful').count()['review_id'].iplot(kind='bar', yTitle='Count', linecolor='black', opacity=0.8,
                                                           title='Bar chart of Useful', xTitle='Useful')


# In[51]:


# 
df.info()


# In[54]:


df['mean_stars'] = df.round({'mean_stars': 1})


# In[ ]:


df.groupby('useful').count()['review_id'].iplot(kind='bar', yTitle='Count', linecolor='black', opacity=0.8,
                                                           title='Bar chart of Useful', xTitle='Useful')


# In[ ]:





# In[28]:


#distribution of useful with restaurant stars
y0 = df.loc[df['mean_stars'] == 0]['business_stars']
y1 = df.loc[df['useful'] == 1]['stars']
y2 = df.loc[df['useful'] == 2]['stars']
y3 = df.loc[df['useful'] == 3]['stars']
y4 = df.loc[df['useful'] == 4]['stars']
y5 = df.loc[df['useful'] == 5]['stars']
y6 = df.loc[df['useful'] == 6]['stars']
y7 = df.loc[df['useful'] == 7]['stars']
y8 = df.loc[df['useful'] == 8]['stars']
y9 = df.loc[df['useful'] == 9]['stars']
y10 = df.loc[df['useful'] == 10]['stars']


trace0 = go.Box(
    y=y0,
    name = '0',
    marker = dict(
        color = 'rgb(214, 12, 140)',
    )
)
trace1 = go.Box(
    y=y1,
    name = '1',
    marker = dict(
        color = 'rgb(0, 128, 128)',
    )
)
trace2 = go.Box(
    y=y2,
    name = '2',
    marker = dict(
        color = 'rgb(10, 140, 208)',
    )
)
trace3 = go.Box(
    y=y3,
    name = '3',
    marker = dict(
        color = 'rgb(12, 102, 14)',
    )
)
trace4 = go.Box(
    y=y4,
    name = '4',
    marker = dict(
        color = 'rgb(10, 0, 100)',
    )
)
trace5 = go.Box(
    y=y5,
    name = '5',
    marker = dict(
        color = 'rgb(100, 0, 10)',
    )
)
trace6 = go.Box(
    y=y6,
    name = '6',
    marker = dict(
        color = 'rgb(100, 0, 10)',
    )
)
trace7 = go.Box(
    y=y7,
    name = '7',
    marker = dict(
        color = 'rgb(100, 0, 10)',
    )
)
trace8 = go.Box(
    y=y8,
    name = '8',
    marker = dict(
        color = 'rgb(100, 0, 10)',
    )
)
trace9 = go.Box(
    y=y9,
    name = '9',
    marker = dict(
        color = 'rgb(100, 0, 10)',
    )
)
trace10 = go.Box(
    y=y10,
    name = '10',
    marker = dict(
        color = 'rgb(100, 0, 10)',
    )
)
data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
layout = go.Layout(
    title = "Rating Boxplot of Useful"
)

fig = go.Figure(data=data,layout=layout)
iplot(fig, filename = "Rating Boxplot of Useful")


# In[29]:


display(y5)


# In[ ]:




