from flask import Blueprint, render_template, request, flash, redirect
from flask import url_for

from twelvedata.helpers import get_stock, get_name
from twelvedata.models import User, StockData, db
from twelvedata.forms import StockForm


site = Blueprint("site", __name__, template_folder="site_templates")



@site.route("/main", methods=['GET', 'POST'])

def home():


    stockform = StockForm()
    #data= None

    if request.method == 'POST' and stockform.validate_on_submit():

        print("hello!!")
        ticker= stockform.ticker.data
        print(ticker)
        data = get_stock(ticker)
        data2= get_name(ticker)
        

        name = data2["data"][0]["name"]
        symbol = data["meta"]["symbol"]
        open = data["values"][0]["open"]
        close = data["values"][0]["close"]
        volume = data["values"][0]["volume"] 
        
        #print(name, symbol, open, close, volume)
        
        user = User.query.get('55edb504-de94-4b6a-bff1-ed0f655cba35')                
        stock_info = StockData(name, symbol, open, close, volume)
        db.session.add(stock_info)   
        db.session.commit()
        return render_template("index.html", form=stockform, info=stock_info, user=user)
    
    return render_template("index.html", form=stockform)


@site.route("/user/watchlist", methods=['POST'])

def watchlist(id, t_id):

    t_id = StockData.query.get(t_id)

    user = User.query.get(id)
    watchist = user.watchlist

    if t_id in watchlist:
        print("Item already added to watchlist")

    else:
        user.add_to_watchlist(t_id)

        