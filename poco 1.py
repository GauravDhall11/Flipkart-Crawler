import bs4
import urllib.request as url
path1="https://www.flipkart.com/poco-x2-atlantis-blue-128-gb/p/itm36af4a9c20dd5?pid=MOBFZGJ6GQRXFZGT&lid=LSTMOBFZGJ6GQRXFZGTUKRV1T&marketplace=FLIPKART&srno=b_1_1&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFZGJ6GQRXFZGT.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
path2="https://www.flipkart.com/poco-m2-pro-out-blue-64-gb/p/itm9fa1bcc61b2c1?pid=MOBFT7MKRQXK9KKF&lid=LSTMOBFT7MKRQXK9KKFVOC7BR&marketplace=FLIPKART&srno=b_1_2&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFT7MKRQXK9KKF.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
path3="https://www.flipkart.com/poco-m2-pro-green-greener-64-gb/p/itm795e36b373b6f?pid=MOBFT7MK3Q89BGWR&lid=LSTMOBFT7MK3Q89BGWRP2OFTB&marketplace=FLIPKART&srno=b_1_5&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFT7MK3Q89BGWR.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
path4="https://www.flipkart.com/poco-m2-pitch-black-64-gb/p/itm83f2e2d3b71ca?pid=MOBFV9V92KHMFCVF&lid=LSTMOBFV9V92KHMFCVFXHKCWC&marketplace=FLIPKART&srno=b_1_19&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFV9V92KHMFCVF.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
path5="https://www.flipkart.com/poco-f1-graphite-black-64-gb/p/itmf8fyjyssnt25c?pid=MOBF85V7A6PXETAX&lid=LSTMOBF85V7A6PXETAXYPRPZ7&marketplace=FLIPKART&srno=b_1_22&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fm=neo%2Fmerchandising&iid=d202fca9-313d-44ed-bb3d-6666dfc6513d.MOBF85V7A6PXETAX.SEARCH&ppt=browse&ppn=browse&ssid=9jkpcsj41s0000001600168433574"
path=[path1,path2,path3,path4,path5]
http=url.urlopen(path)
for i in range(1,5):
    path=path[i]
    http[i]=url.urlopen(path[i])
    page[i]=bs4.BeautifulSoup(http[i],"lxml")
    p[i]=page[i].find('span',class_="_35KyD6").text + ' ' + page[i].find('div',class_="_1vC4OE _3qQ9m1").text + "\n" + page[i].find('div',class_="g2dDAR").text
print(http[1])