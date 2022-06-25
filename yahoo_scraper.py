import requests
from bs4 import BeautifulSoup


response=requests.get('https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI')
soup=BeautifulSoup(response.text,'lxml')

date=soup.find('time').get('datatime')

rows=soup.find_all('div',{'Bgc(#fff) table-row D(f) H(48px) Ai(c) Bgc(#e7f3ff):h Fz(16px) Px(12px) Bxz(bb) Bdbs(s) Bdbw(1px) Bdbc($bd-primary-divider)'})
for row in rows:
    company=row.find('div',{'class':'Lh(20px) Fw(600) Fz(16px) Ell'}).getText()
    price=row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'})[0].getText()
    status=row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0].getText()
    percentage=row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1].getText()
    print(date, company,price,status,percentage)
