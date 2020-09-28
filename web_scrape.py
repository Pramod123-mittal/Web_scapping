import requests
from bs4 import BeautifulSoup
import time
from datetime import date
import csv
import send_mail
urls = ["https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch","https://finance.yahoo.com/quote/BHEL.NS?p=BHEL.NS&.tsrc=fin-srch"
"https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/SBIN.NS?p=SBIN.NS&.tsrc=fin-srch","https://finance.yahoo.com/quote/RELIANCE.NS?p=RELIANCE.NS&.tsrc=fin-srch"]

#html_page = requests.get(url)
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
#headers are used  to avoid 
#To avoid bot request most websites usually have scripts. Here we use this header to mimic our request as a browser.
#print(html_page.content)
today = str(date.today())+".csv"
csv_file = open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Current Price','Previous Close',
'Open','Bid','Ask','Day-Range','52 Week-Range','Volume','Avg.Volume'])

for url in urls:
    stock = []
    html_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(html_page.content, 'lxml')
    #print(soup.title)
    #title  = soup.find('title').get_text()
    #print(title)
    header_info = soup.find_all("div",id = "quote-header-info")[0]
    stock_title = header_info.find("h1").get_text()
    #print(stock_title)
    current_price = header_info.find("div",class_ = "My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()
    #print(current_price)
    stock.append(stock_title)
    stock.append(current_price)

    table_info = soup.find_all("div",class_ = "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all('tr')
    '''previous_close_heading = table_info[0].find_all('span')[0].get_text()
    previous_close_value = table_info[0].find_all('span')[1].get_text()
    print(previous_close_heading + "-" + previous_close_value)'''

    for i in range(0,8):
        #heading = table_info[i].find_all('td')[0].get_text()
        value = table_info[i].find_all('td')[1].get_text()
        #print(heading + "  :  " + value)
        stock.append(value)
    #print('------------------------------')
    csv_writer.writerow(stock)
    
    time.sleep(5)

csv_file.close()
send_mail.send(filename = today)







































