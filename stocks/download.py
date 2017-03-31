import urllib

base_url = "http://ichart.finance.yahoo.com/table.csv?s="

def make_url(ticker_symbol):
    return base_url + ticker_symbol

output_path = "/Users/andym/scripts/stocks"

def make_filename(ticker_symbol, directory="S&P"):
    return output_path + "/" + directory + "/" + ticker_symbol + ".csv"

def pull_historical_data(ticker_symbol, directory="data"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()


#for i in ticker_symbol
# This is a test to download data 
pull_historical_data('AMZN', directory="data")
pull_historical_data('GOOG', directory="data")