import base64
import yfinance as yf
import streamlit as st
import datetime as dt


yf.pdr_override()

st.write("""
# Historical Stock Price Downloader
1. Populate the **ticker(s)** box on the left with the ticker symbols you'd like historical information for, with each ticker symbol separated by a comma e.g., AAPL, GOOG, TSLA. 
2. Then provide the **time period** you're interested in.
3. Click **download** below for the historical info in a csv file.
""")

st.sidebar.header('User Input Parameters')

today = dt.date.today()


def previous_quarter_start():
    today = dt.date.today()

    if today.month < 4:
        return dt.date(today.year - 1, 10, 1)
    elif today.month < 7:
        return dt.date(today.year, 1, 1)
    elif today.month < 10:
        return dt.date(today.year, 4, 1)
    return dt.date(today.year, 7, 1)


def previous_quarter_end():
    today = dt.date.today()

    if today.month < 4:
        return dt.date(today.year, 1, 1)
    elif today.month < 7:
        return dt.date(today.year, 4, 1)
    elif today.month < 10:
        return dt.date(today.year, 7, 1)
    return dt.date(today.year, 10, 1)


def user_input_features():
    ticker = st.sidebar.text_input("Ticker(s)", 'ADS.DE, NKE, UA, LULU, 7936.T, JD.L, FL, PUM.DE, ZAL.DE, ^GSPC')
    start_date = st.sidebar.text_input("Start Date", previous_quarter_start())
    end_date = st.sidebar.text_input("End Date", previous_quarter_end())
    return ticker, start_date, end_date

symbol, start, end = user_input_features()

download = st.button('Download csv file')

if download:
    'Download Started!'
    Ticker = symbol
    df_download = yf.download(Ticker, start=start, end=end)['Close']
    csv = df_download.to_csv()
    b64 = base64.b64encode(csv.encode()).decode()  # some strings
    linko = f'<a href="data:file/csv;base64,{b64}" download="Historical_Stock_Prices.csv">Download csv file</a>'
    st.markdown(linko, unsafe_allow_html=True)