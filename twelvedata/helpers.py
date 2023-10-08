import requests
import requests_cache
import decimal 
import json 

#def get_stock(search):

#    url = "https://api.twelvedata.com/stocks?symbol=AAPL"

 #   data = requests.get(url).json()


def get_stock(symbol):
    
    api_key = '8e75a5baf1e74e8eb3fd62a149331539'
    endpoint = '/time_series'
    interval = '1min'

    url = f'https://api.twelvedata.com{endpoint}'
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': api_key
    }



    response = requests.get(url, params=params)
    try:
        if response.status_code == 200:
            # Process and use the response_data here
            #print(response_data)

            
            response_data = response.json()

            return(response_data)

        else:
            print('Error:', response_data['error'])

    except requests.exceptions.RequestException as e:
        print('Error:', e)

def get_name(symbol):

    api_key = '8e75a5baf1e74e8eb3fd62a149331539'
    interval = '1min'

    url = f'https://api.twelvedata.com/stocks?symbol={symbol}'
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': api_key
    }

    response = requests.get(url, params=params)
    try:
        if response.status_code == 200:
            # Process and use the response_data here
            #print(response_data)

            
            response_data = response.json()

            return(response_data)

        else:
            print('Error:', response_data['error'])

    except requests.exceptions.RequestException as e:
        print('Error:', e)


