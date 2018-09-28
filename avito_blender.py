import pandas as pd

f1 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2226.csv')
f1.columns = ['item_id','sub_2226']
f2 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2224.csv')
f2.columns = ['item_id','sub_2224']
f3 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2218.csv')
f3.columns = ['item_id','sub_2218']
f4 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2211.csv')
f4.columns = ['item_id','sub_2211']
f5 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2214.csv')
f5.columns = ['item_id','sub_2214']
f6 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2216.csv')
f6.columns = ['item_id','sub_2216']
f7 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2216_blend.csv')
f7.columns = ['item_id','sub_2216_blend']
f8 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2208.csv')
f8.columns = ['item_id','sub_2208']
f9 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2209.csv')
f9.columns = ['item_id','sub_2209']
f10 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2222.csv')
f10.columns = ['item_id','sub_2222']
f11 = pd.read_csv('/Users/sambeet/Downloads/lgsub_2221.csv')
f11.columns = ['item_id','sub_2221']

f = f1.merge(f2,on='item_id',how='left')
f = f.merge(f3,on='item_id',how='left')
f = f.merge(f4,on='item_id',how='left')
f = f.merge(f5,on='item_id',how='left')
f = f.merge(f6,on='item_id',how='left')
f = f.merge(f7,on='item_id',how='left')
f = f.merge(f8,on='item_id',how='left')
f = f.merge(f9,on='item_id',how='left')
f = f.merge(f10,on='item_id',how='left')
f = f.merge(f11,on='item_id',how='left')
f.corr()


f4 = (f1['deal_probability']*0.2 + f2['deal_probability']*0.3 + f3['deal_probability']*0.5 )
ensemble = pd.DataFrame({'item_id':f2['item_id'],'deal_probability':f4})
ensemble = ensemble[['item_id','deal_probability']]
ensemble.to_csv('lgb_2805.csv',index=False)