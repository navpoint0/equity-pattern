import requests
import psycopg2
import sys

class Stock:
    def __init__(self, symbol, last, percentChange, volume):
        self.symbol = symbol
        self.last = last
        self.percentChange = percentChange
        self.volume = volume
    def toString(self):
        print "Ticker: ", self.symbol, ", Last: ", self.last, ", % Change: ", self.percentChange, ", Volume: ", self.volume

results = requests.get("http://bit.ly/ep-losers-nasdaq").json()

stocks = []
counter = 0
for result in results['query']['results']['td']:
    if ( counter == 4 ):
        stock = Stock(symbol, last, percentChange, volume);
        stocks.append(stock)
        counter = 0

    if ( result['headers'] == 'symbol' ):
        symbol = result['a']['content']
        counter += 1
        continue
    if ( result['headers'] == 'last' ):
        last = result['p']
        counter += 1
        continue
    if ( result['headers'] == 'percentChange' ):
        # percentChange = result['p']
        percentChange = 0
        counter += 1
        continue
    if ( result['headers'] == 'volume' ):
        volume = result['p']
        counter += 1
        continue   

print 'NASDAQ losers parsed: %d' % len(stocks)

con = None
try:
    con = psycopg2.connect(database='equities', user='postgres', host='localhost', password='pa55w0rd')
    cur = con.cursor()
    for stock in stocks:
        cur.execute("INSERT INTO equities.stock_master (id, index, ticker, tracking_date, initial_direction) VALUES (DEFAULT, 'NASDAQ', %s, CURRENT_DATE, 'D') RETURNING id", (stock.symbol,))
        iid = cur.fetchone()
        cur.execute("INSERT INTO equities.stock_data (id, stock_id, date, close_price) VALUES (DEFAULT, %s, CURRENT_DATE, %s)", (iid[0], stock.last))
        con.commit()
    print 'NASDAQ losers saved'
except psycopg2.DatabaseError, e:   
    if con:
        con.rollback()    
    print 'Error %s' % e    
    sys.exit(1)        
finally:   
    if con:
        con.close()

sys.exit(0);
