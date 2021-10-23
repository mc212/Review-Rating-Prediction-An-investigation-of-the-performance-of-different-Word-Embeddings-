#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd

path = 'F:/MCM 2020_2021/CA683/yelp data set/20210411/20210411_final_data_265062.csv'
review_col_list2 = ["review_id","stars","text"]
df = pd.read_csv(path, usecols=review_col_list2)


# In[15]:


df.info()


# In[3]:


df = df[~df['text'].isnull()]


# In[4]:


def preprocess(ReviewText):
    ReviewText = ReviewText.str.replace("(<br/>)", "")
    ReviewText = ReviewText.str.replace('(<a).*(>).*(</a>)', '')
    ReviewText = ReviewText.str.replace('(&amp)', '')
    ReviewText = ReviewText.str.replace('(&gt)', '')
    ReviewText = ReviewText.str.replace('(&lt)', '')
    ReviewText = ReviewText.str.replace('(\xa0)', ' ')  
    return ReviewText


# In[5]:


df['text'] = preprocess(df['text'])


# In[11]:


#pip install textblob
#pip install plotly==4.14.3


# In[6]:



from textblob import TextBlob

df['polarity'] = df['text'].map(lambda text: TextBlob(text).sentiment.polarity)


# In[7]:


df['review_len'] = df['text'].astype(str).apply(len)
#df['word_count'] = df['text'].apply(lambda x: len(str(x).split()))


# In[8]:


print('5 random reviews with the highest positive sentiment polarity: \n')
cl = df.loc[df.polarity == 1, ['text']].sample(5).values
for c in cl:
    print(c[0])


# In[18]:


print('5 random reviews with the most neutral sentiment(zero) polarity: \n')
cl = df.loc[df.polarity == 0, ['text']].sample(5).values
for c in cl:
    print(c[0])


# In[19]:


print('2 reviews with the most negative polarity: \n')
cl = df.loc[df.polarity == -1, ['text']].sample(2).values
for c in cl:
    print(c[0])


# In[9]:


import plotly
import plotly.graph_objs as go
from plotly.offline import iplot


# In[22]:


#pip install cufflinks


# In[10]:


#The temp object here is a pandas.series object which does not have a iplot method when not linked to plotly. We need cufflinks to link plotly to pandas and add the iplot method:

import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)


# In[11]:


#The distribution of review sentiment polarity score

df['polarity'].iplot(
    kind='hist',
    bins=50,
    xTitle='polarity',
    linecolor='black',
    yTitle='count',
    title='Sentiment Polarity Distribution')


# In[39]:


#The distribution of review ratings
df['stars'].iplot(
    kind='hist',
    xTitle='rating',
    linecolor='black',
    yTitle='count',
    title='Review Rating Distribution - Subset')


# In[13]:


#The distribution review text lengths -> dung tren bo full 2m8 records
df['review_len'].iplot(
    kind='hist',
    bins=100,
    xTitle='review length',
    linecolor='black',
    yTitle='count',
    title='Review Text Length Distribution')


# In[28]:


column = df['review_len']
max_value = column.max()
min_value = column.min()
print(max_value)
print(min_value)


# In[29]:


#The distribution of review word count
df['word_count'].iplot(
    kind='hist',
    bins=100,
    xTitle='word count',
    linecolor='black',
    yTitle='count',
    title='Review Text Word Count Distribution')


# In[30]:


columnwc = df['word_count']
max_value = columnwc.max()
min_value = columnwc.min()
print(max_value)
print(min_value)


# In[36]:


from sklearn.feature_extraction.text import CountVectorizer


# In[37]:


def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


# In[38]:


common_words = get_top_n_words(df['text'], 20)
for word, freq in common_words:
    print(word, freq)
df2 = pd.DataFrame(common_words, columns = ['text' , 'count'])
df2.groupby('text').sum()['count'].sort_values(ascending=False).iplot(
    kind='bar', yTitle='Count', linecolor='black', title='Top 20 words in review before removing stop words')


# In[ ]:




