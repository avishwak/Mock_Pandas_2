# Problem 1: Sales Analysis III https://leetcode.com/problems/sales-analysis-iii/

# solution 1
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    df = sales.groupby('product_id').agg(
        min_date = ('sale_date', 'min'),
        max_date = ('sale_date', 'max')
    ).reset_index()
    
    df = df[(df['min_date'] >= '2019-01-01') & (df['max_date'] <= '2019-03-31')][['product_id']]
    result = df.merge(product, on = 'product_id', how = 'inner')[['product_id', 'product_name']]
    return result

# solution 2
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    df = sales.merge(product, how = 'inner', on = 'product_id')

    in_q1 = (df['sale_date'] >= '2019-01-01') & (df['sale_date'] <= '2019-03-31')
    outside_q1 = (df['sale_date'] < '2019-01-01') | (df['sale_date'] > '2019-03-31')

    products_outside_q1 = set(df.loc[outside_q1, 'product_id'])

    result = df.loc[in_q1, ['product_id', 'product_name']]\
    .drop_duplicates()\
    .query("product_id not in @products_outside_q1")

    return result
