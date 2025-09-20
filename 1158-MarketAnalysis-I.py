# Problem 2: Market Analysis I https://leetcode.com/problems/market-analysis/

# solution 1

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = orders[(orders['order_date']>='2019-01-01') & (orders['order_date'] <= '2019-12-31')]

    df = users.merge(df, how = 'left', left_on='user_id', right_on = 'buyer_id')[['user_id', 'join_date', 'order_id']]

    df = df.groupby(['user_id', 'join_date'])['order_id'].count().reset_index(name='orders_in_2019')

    return df.rename(columns={'user_id':'buyer_id'})

# solution 2
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    df = df.merge(users, how='left', left_on='buyer_id', right_on='user_id')
    df = df.groupby(['user_id', 'join_date']).agg(orders_in_2019=('order_id', 'count')).reset_index()
    df = df.rename(columns={'user_id': 'buyer_id'})
    return df

# solution 3
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]

    order_counts = orders_2019['buyer_id'].value_counts().reset_index(name='orders_in_2019')
    
    result = users.merge(order_counts, left_on='user_id', right_on='buyer_id', how='left')

    result['orders_in_2019'] = result['orders_in_2019'].fillna(0)
    
    return result[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id':'buyer_id'})