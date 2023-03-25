




#Project: Stock Market Data Analysis and Visualization
# Requirements:
# 1. Implement a command-line application that retrieves stock market data from an API (e.g., Alpha Vantage or Yahoo Finance) and stores the data in a local file (CSV or JSON format).
# 2. Use loops, list comprehensions, and functions effectively.
# 3. Implement error handling for potential issues, such as invalid API responses or incorrect user input.
# 4. Use an external library (e.g., matplotlib) to create graphs and visualizations of the stock market data.
# 5. Analyze the data and provide insights, such as average price, trends over time, and price comparisons between different stocks.
# Tips:
# 1. Create functions to retrieve stock market data for a given stock symbol and time range (e.g., past week or month).
# 2. Use the requests library to interact with the API and the json or csv library to parse the API responses and store the data in a local file.
# 3. Create functions to calculate statistics (e.g., mean, median, and mode) for the retrieved stock market data.
# 4. Use the matplotlib library to create graphs and visualizations, such as line graphs for stock prices over time or bar graphs for price comparisons between different stocks.
#############################################################
#CODE
#############################################################
#Caling the libaryis
import json
import requests
import datetime as dt
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
from matplotlib import style
from pandas_datareader import data as pdr

#Gets ticker symbol 
stock_code = input ("Enter the name of the stock")
url = "https://s.yimg.com/aq/autoc"
parameters = {'query': stock_code, 'lang': 'en-US'}
response = requests.get(url = url, params = parameters)
data = response.json()
company_code = data['ResultSet']['Result'][0]['symbol']
#Create the graph
def graph_generator ():
   start = dt.datetime(2019 , 1, 1)
   end  =  dt.datetime(2023, 3, 24)
   stock_graph = pdr.DataReader(company_code, "yahoo",start,end)
   style.use("ggplot")
   stock_graph["Close"].plot(figsize=(8,8), label = company_code)
   plt.show()


def web_contetnt_html(web_content,class_path, value):
    web_content.find_all(value)
    try: 
        if value != "None": 
            spans = web_contetnt_html[0].find_all(value)
            texts = [spans.get_text() for span in spans]
        else:
            texts = []
    except IndexError:
        texts=[]

    return texts , web_content


def main():
    for stock_code in Stock :
      stock_price,change,volume,latest_pattern , one_year_target, Error = real_time_price(stock_code)


# function to get the stocks 
def real_time_price(stock_code):
    url = "https://finance.yahoo.com/quote/" + stock_code +"?p=" + stock_code +"&.t.src=fin-srch"
    try:
       response = requests.get(url)
       web_content = BeautifulSoup(response.text, "lxml")
       texts  = web_contetnt_html(web_content, "D(ib) Mend(20px)", "fin-streamer")
       print(texts)
       price , change = texts[0], texts[1] +""+texts[2]
       web_contetnt_html(web_content, "", "fin-streamer")
       return change , volume , latest_pattern , one_year_target , stock_code
    except (ConnectionError):
         price , change , volume , latest_pattern, one_year_target = [], [], [] ,[]
         raise ConnectionError("There is a connection error please try again latter")
    
Stock = ["ES=F", "AAPL"]
main()
graph_generator()
data = {
    "stock_symbol":"AAPL",
    "start_date": "2019 , 1, 1",
    "end_date":"2023, 3, 24",
    "open":"123.3600",
    "high":"125.3600",
    "low":"122.880",
    "close":"125.2900",
    "volume":"3809264"
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)
















