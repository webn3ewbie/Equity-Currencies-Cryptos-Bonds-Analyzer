import streamlit as st
import yfinance as yf


def intro():
    import streamlit as st

    st.write("# Welcome to ExtractAlpha! ")
    st.sidebar.success("Select an Analyzer above.")

    st.markdown(
        """
        ExtractAlpha is an open-source app framework built specifically to analyze equities, bonds, commodities, currencies, cryptos

        Select a dashboard from the dropdown on the left to analyze equities, bonds, commodities, currencies, cryptos see some examples
        of what ExtractAlpha can do!

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
    import yfinance as yf
    
    st.title('Asset Price Analyzer')
    
    st.write("""
             Crude Oil: CL=F 
             
             Gold: GC=F 
             
             Silver: SI=F  
             
             U.S. 5 Year Treasury Yield: ^FVX
             
             U.S. 10 Year Treasury Yield: ^TNX
             
             U.S. 30 Year Treasury Yield: ^TYX
             
             Dow Jones Industrial Average: ^DJI
             
             S&P 500: ^GSPC
             
             Nasdaq: ^IXIC
             
             """)

    tickers = st.text_input("Tickers", "AAPL MSFT")
    tickers = tickers.split()
    tickers_data = yf.download(tickers, period="5y", interval="1d")
    st.line_chart(tickers_data.Close)

    

def asset_return():

    import streamlit as st 
    import pandas as pd
    import yfinance as yf
 
    st.title('Asset Return Analyzer')
    
    tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','LMT','AMZN','SPY','BRK-B','META','UNH','V','NVDA','JNJ','WMT','XOM','JPM','PG','MA','GOOG','CL=F','GC=F','SI=F','^TNX','EURUSD=X','^FVX','^TYX','^RUT','^IXIC','^GSPC','^DJI')

    dropdown = st.multiselect('Select your assests', tickers)

    start = st.date_input('Start', value = pd.to_datetime('2000-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))
    
    def relativeret(df):
        rel = df.pct_change()
        cumret = (1+rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret
    
    if len (dropdown) > 0:
        df = yf.download(dropdown,start,end)['Adj Close']
        st.header('Returns of {}'.format(dropdown))
        df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
        st.line_chart(df)

    
def asset_price_prediction():
    
    import pandas as pd
    from prophet import Prophet
    from prophet.plot import plot_plotly
    from plotly import graph_objs as go
    
    start = st.date_input('Start', value = pd.to_datetime('2000-01-01'))
    end = st.date_input('End',value = pd.to_datetime('today'))


    st.title('Stock Forecast App')

    stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','SPY','MSTR','QQQ','^GSPC','META','CL=F')
    selected_stock = st.selectbox('Select dataset for prediction', stocks)

    n_years = st.slider('Years of prediction:', 1, 5)
    period = n_years * 365


    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, start,end)
        data.reset_index(inplace=True)
        return data

    	
    data_load_state = st.text('Loading data...')
    data = load_data(selected_stock)
    data_load_state.text('Loading data... done!')

    st.subheader('Raw data')
    st.write(data.tail())

    # Plot raw data
    def plot_raw_data():
    	fig = go.Figure()
    	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    	st.plotly_chart(fig)
    	
    plot_raw_data()

    # Predict forecast with Prophet.
    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Show and plot forecast
    st.subheader('Forecast data')
    st.write(forecast.tail())
        
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)


page_names_to_funcs = {
    "Home": intro,
    "Asset Return Comparison": asset_return,
    "Asset Price Comparison": price_comparison,
    "Assest Price Prediction": asset_price_prediction
}

demo_name = st.sidebar.selectbox("Choose a dashboard", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

ose a dashboard", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
