import streamlit as st

def intro():
    import streamlit as st

    st.write("# Welcome to AplhaLight! ")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        AlphaLight is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        Select a dashboard from the dropdown on the left to anaylzy equities, bonds, commodities, currincies, cryptos see some examples
        of what AlphaLight can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
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

    st.title('Asset Performace Dashboard')
    
    st.write("Crude Oil:CL=F")                           
    st.write("Gold:GC=F")  
    st.write("Silver:SI=F")
    st.write("U.S. 5 Year Treasury Yield:^FVX")
    st.write("U.S. 10 Year Treasury Yield:^TXN")
    st.write("U.S. 30 Year Treasury Yield:^TYX")
    st.write("EUR/USD:EURUSD=X")
    st.write("Dow Jones Industrial Average:^DJI")
    st.write("S&P 500:^GSPC")
    st.write("Nasdaq:^IXIC")
    
      
      

    tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','LMT','AMZN','SPY','BRK.B','META','UNH','V','NVDA','JNJ','WMT','XOM','JPM','PG','MA','GOOG','CL=F','GC=F','SI=F','^TNX','EURUSD=X','^FVX','^TYX','^RUT','^IXIC','^GSPC','^DJI')

    dropdown = st.multiselect('Select your assests', tickers)

    start = st.date_input('Start', value = pd.to_datetime('1970-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))

    if len (dropdown) > 0:
        df = yf.download(dropdown,start,end)['Adj Close']
        st.line_chart(df)


def asset_return():
   import streamlit as st
   import pandas as pd
   import numpy as np
   import yfinance as yf
   
   
   tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','LMT','AMZN','SPY','BRK.B','META','UNH','V','NVDA','JNJ','WMT','XOM','JPM','PG','MA','GOOG','CL=F','GC=F','SI=F','^TNX','EURUSD=X','^FVX','^TYX','^RUT','^IXIC','^GSPC','^DJI')
   dropdown = st.multiselect('Select your assests', tickers)

   start = st.date_input('Start', value = pd.to_datetime('1970-01-01'))
   end = st.date_input('End',value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.filna(0)
    return cumret

     if len (dropdown) > 0:
         df = yf.download(dropdown,start,end)['Adj Close']
         st.line_chart(df)
         
def data_frame_demo():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import yfinance as yf

page_names_to_funcs = {
    "Home": intro,
    "Asset Return Comparison": asset_return,
    "Asset Price Comparison": price_comparison,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a dashboard", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()