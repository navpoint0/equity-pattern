import requests
import psycopg2
import sys

# maps to http://download.finance.yahoo.com/d/quotes.csv
# returns open_price,close_price
url = "http://tiny.cc/ep-stock/?f=ol1&s=" 

con = None
try:
    con = psycopg2.connect(database='equities', user='postgres', host='localhost', password='pa55w0rd')
    cur = con.cursor()
    cur.execute('SELECT id, ticker, CURRENT_DATE - tracking_date FROM equities.stock_master WHERE (CURRENT_DATE - tracking_date) < 5')
    rows = cur.fetchall()
    for row in rows:
        results = requests.get(url + row[1]).content
        oc = results.strip('\r\n').split(',')
        opn = 0 if oc[0] == 'N/A' else oc[0]    # Y! Finance occasionally returns open_price of N/A
        cur.execute("INSERT INTO equities.stock_data (id, stock_id, date, trend_days, open_price, close_price) VALUES (DEFAULT, %s, CURRENT_DATE, %s, %s, %s)", (row[0], row[2], opn, oc[1]))
    con.commit()
except psycopg2.DatabaseError, e:   
    if con:
        con.rollback()    
    print 'Error %s' % e    
    sys.exit(1)        
finally:   
    if con:
        con.close()


