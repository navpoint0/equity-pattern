#NYSE

Query
```
select * from html where url='http://www.thestreet.com/markets/losers.html' and xpath='//table[@id="nyseData"]/tbody/tr/td[@headers="symbol" or @headers="last" or @headers="percentChange" or @headers="volume"]'
```

[YQL Test URL](https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D'http%3A%2F%2Fwww.thestreet.com%2Fmarkets%2Flosers.html'%20and%20xpath%3D'%2F%2Ftable%5B%40id%3D%22nyseData%22%5D%2Ftbody%2Ftr%2Ftd%5B%40headers%3D%22symbol%22%20or%20%40headers%3D%22last%22%20or%20%40headers%3D%22percentChange%22%20or%20%40headers%3D%22volume%22%5D'&diagnostics=true)

# NASDAQ

Query
```
select * from html where url='http://www.thestreet.com/markets/losers.html' and xpath='//table[@id="nasdaqData"]/tbody/tr/td[@headers="symbol" or @headers="last" or @headers="percentChange" or @headers="volume"]'
```

[YQL Test URL](https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D'http%3A%2F%2Fwww.thestreet.com%2Fmarkets%2Flosers.html'%20and%20xpath%3D'%2F%2Ftable%5B%40id%3D%22nasdaqData%22%5D%2Ftbody%2Ftr%2Ftd%5B%40headers%3D%22symbol%22%20or%20%40headers%3D%22last%22%20or%20%40headers%3D%22percentChange%22%20or%20%40headers%3D%22volume%22%5D'&diagnostics=true)

# AMEX

Query
```
select * from html where url='http://www.thestreet.com/markets/losers.html' and xpath='//table[@id="amexData"]/tbody/tr/td[@headers="symbol" or @headers="last" or @headers="percentChange" or @headers="volume"]'
```

[YQL Test URL](https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20html%20where%20url%3D'http%3A%2F%2Fwww.thestreet.com%2Fmarkets%2Flosers.html'%20and%20xpath%3D'%2F%2Ftable%5B%40id%3D%22amexData%22%5D%2Ftbody%2Ftr%2Ftd%5B%40headers%3D%22symbol%22%20or%20%40headers%3D%22last%22%20or%20%40headers%3D%22percentChange%22%20or%20%40headers%3D%22volume%22%5D'&diagnostics=true)
