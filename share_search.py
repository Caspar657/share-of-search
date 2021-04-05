import pandas as pd 
import pytrends


def share_of_search(kw_list):

        def calculate_rolling(df): #calculate 12 month rolling average of search index
            columns = list(df) #create list of column names
            for column in columns:
                col_name = str(column) + '_rolling'
                df[col_name] = df.rolling(window=12)[column].mean()
            df = df.drop(columns = columns)
            return df 

        def add_total(df): #add all columns together to get the rolling total
            df['rolling_total'] = df.sum(axis=1)
            return df

        def share_search(df): #divide each search term by the total to get the % share of search
            columns = list(df)
            columns.remove('rolling_total')
            for column in columns:
                col_name = str(column) + '_SOS'
                df[col_name] = df[column] / df.rolling_total
            df = df.drop(columns = columns)
            df = df.drop(columns = ['rolling_total'])
            return df
        
        #query Google Trends
        from pytrends.request import TrendReq
        pytrends = TrendReq(hl='en-US', tz = 600)
        pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='AU', gprop='')

        df = pytrends.interest_over_time()
        df = df.drop(columns = 'isPartial') #remove extra column
        
        #apply transformations to data
        rolling_df = calculate_rolling(df)
        total_df = add_total(rolling_df)
        share_search_df = share_search(total_df)

        return share_search_df