import streamlit as st

def intro():
    import streamlit as st

    st.write("# Welcome to AssessAlpha! ")
    st.sidebar.success("Select an Analyzer above.")

    st.markdown(
        """
        AssessAlpha is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        Select a dashboard from the dropdown on the left to anaylzy equities, bonds, commodities, currincies, cryptos see some examples
        of what AssessAlpha can do!

        ### Want to learn more?

        - Check out the repo [here](https://github.com/webn3ewbie/Equity-Currencies-Cryptos-Bonds-Analyzer)
        - Connect with me on [LinkedIn](https://www.linkedin.com/in/joseph-biancamano/)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def price_comparison():
    import streamlit as st
    import pandas as pd
    import yfinance as yf
    
   
    st.title('Asset Price Analyzer')
    
    st.write("""
             Crude Oil: CL=F 
             
             Gold: GC=F 
             
             Silver: SI=F  
             
             U.S. 5 Year Treasury Yield: ^FVX
             
             U.S. 10 Year Treasury Yield: ^TXN
             
             U.S. 30 Year Treasury Yield: ^TYX
             
             Dow Jones Industrial Average: ^DJI
             
             S&P 500: ^GSPC
             
             Nasdaq: ^IXIC
             
             """)
   
    tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','LMT','AMZN','SPY','BRK.B','META','UNH','V','NVDA','JNJ','WMT','XOM','JPM','PG','MA','GOOG','CL=F','GC=F','SI=F','^TNX','EURUSD=X','^FVX','^TYX','^RUT','^IXIC','^GSPC','^DJI')

    dropdown = st.multiselect('Select your assests', tickers)

    start = st.date_input('Start', value = pd.to_datetime('2000-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))

    if len (dropdown) > 0:
        df = yf.download(dropdown,start,end)['Adj Close']
        st.header('Prices of {}'.format(dropdown))
        st.line_chart(df)


def asset_return():

    
    import pandas as pd
    import yfinance as yf
 
    st.title('Asset Return Analyzer')
 
    tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','LMT','AMZN','SPY','BRK.B','META','UNH','V','NVDA','JNJ','WMT','XOM','JPM','PG','MA','GOOG','CL=F','GC=F','SI=F','^TNX','EURUSD=X','^FVX','^TYX','^RUT','^IXIC','^GSPC','^DJI')
 
    dropdown = st.multiselect('Select your assests', tickers)
 
    start = st.date_input('Start', value = pd.to_datetime('2010-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))

    def relativeret(df):
        rel = df.pct_change()
        cumret = (1+rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret

    if len (dropdown) > 0:
       df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
       st.header('Returns of {}'.format(dropdown))
       st.line_chart(df)
       
      

          
def asset_price_prediction():
    
    
    import pandas as pd
    import numpy as np
    import yfinance as yf

page_names_to_funcs = {
    "Home": intro,
    "Asset Return Comparison": asset_return,
    "Asset Price Comparison": price_comparison,
    "Assest Price Prediction": asset_price_prediction
}

demo_name = st.sidebar.selectbox("Choose a dashboard", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
