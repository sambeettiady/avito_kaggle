
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


f1 = pd.read_csv('D:/Kaggle/Avito/lgsub_1.csv')


# In[ ]:


f2 = pd.read_csv('D:/Kaggle/Avito/lgsub_2.csv')


# In[ ]:


f3 = pd.read_csv('D:/Kaggle/Avito/lgsub_2225.csv')            ##This is the new model


# In[ ]:


f4 = (f1['deal_probability']*0.2 + f2['deal_probability']*0.3 + f3['deal_probability']*0.5 )


# In[ ]:


ensemble = pd.DataFrame({'item_id':f2['item_id'],'deal_probability':f4})


# In[ ]:


ensemble = ensemble[['item_id','deal_probability']]


# In[ ]:


ensemble.to_csv('lgb_2105.csv',index=False)

