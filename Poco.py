import bs4
import urllib.request as url
stopwords=[]
import tkinter as tk
def display_text2():
    path1="https://www.flipkart.com/poco-x2-atlantis-blue-128-gb/p/itm36af4a9c20dd5?pid=MOBFZGJ6GQRXFZGT&lid=LSTMOBFZGJ6GQRXFZGTUKRV1T&marketplace=FLIPKART&srno=b_1_1&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFZGJ6GQRXFZGT.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
    path2="https://www.flipkart.com/poco-m2-pro-out-blue-64-gb/p/itm9fa1bcc61b2c1?pid=MOBFT7MKRQXK9KKF&lid=LSTMOBFT7MKRQXK9KKFVOC7BR&marketplace=FLIPKART&srno=b_1_2&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFT7MKRQXK9KKF.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
    path3="https://www.flipkart.com/poco-m2-pro-green-greener-64-gb/p/itm795e36b373b6f?pid=MOBFT7MK3Q89BGWR&lid=LSTMOBFT7MK3Q89BGWRP2OFTB&marketplace=FLIPKART&srno=b_1_5&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFT7MK3Q89BGWR.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
    path4="https://www.flipkart.com/poco-m2-pitch-black-64-gb/p/itm83f2e2d3b71ca?pid=MOBFV9V92KHMFCVF&lid=LSTMOBFV9V92KHMFCVFXHKCWC&marketplace=FLIPKART&srno=b_1_19&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=2c26c1b4-7fa6-47ec-83eb-52bcd9270a41.MOBFV9V92KHMFCVF.SEARCH&ppt=browse&ppn=browse&ssid=zmxh7xliao0000001600084680760"
    path5="https://www.flipkart.com/poco-f1-graphite-black-64-gb/p/itmf8fyjyssnt25c?pid=MOBF85V7A6PXETAX&lid=LSTMOBF85V7A6PXETAXYPRPZ7&marketplace=FLIPKART&srno=b_1_22&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp12&fm=neo%2Fmerchandising&iid=d202fca9-313d-44ed-bb3d-6666dfc6513d.MOBF85V7A6PXETAX.SEARCH&ppt=browse&ppn=browse&ssid=9jkpcsj41s0000001600168433574"
    http1=url.urlopen(path1)
    http2=url.urlopen(path2)
    http3=url.urlopen(path3)
    http4=url.urlopen(path4)
    http5=url.urlopen(path5)
    page1=bs4.BeautifulSoup(http1,"lxml")
    page2=bs4.BeautifulSoup(http2,"lxml")
    page3=bs4.BeautifulSoup(http3,"lxml")
    page4=bs4.BeautifulSoup(http4,"lxml")
    page5=bs4.BeautifulSoup(http5,"lxml")
    p1=page1.find('span',class_="B_NuCI").text + ' ' + page1.find('div',class_="_30jeq3 _16Jk6d").text + "\n" + page1.find('div',class_="_1AtVbE col-6-12").text
    p2=page2.find('span',class_="B_NuCI").text + ' ' + page2.find('div',class_="_30jeq3 _16Jk6d").text + "\n" + page2.find('div',class_="_1AtVbE col-6-12").text
    p3=page3.find('span',class_="B_NuCI").text + ' ' + page3.find('div',class_="_30jeq3 _16Jk6d").text + "\n" + page3.find('div',class_="_1AtVbE col-6-12").text
    p4=page4.find('span',class_="B_NuCI").text + ' ' + page4.find('div',class_="_30jeq3 _16Jk6d").text + "\n" + page4.find('div',class_="_1AtVbE col-6-12").text
    p5=page5.find('span',class_="B_NuCI").text + ' ' + page5.find('div',class_="_30jeq3 _16Jk6d").text + "\n" + page5.find('div',class_="_1AtVbE col-6-12").text
    for word in stopwords:
        if word in p1 and p2 and p3 and p4 and p5:
            p1=p1.replace(word,'')
            p2=p2.replace(word,'')
            p3=p3.replace(word,'')
            p4=p4.replace(word,'')
            p5=p5.replace(word,'')
    main = tk.Tk()
    w = tk.Label(main, text="Poco")
    w.config(bg='skyblue', font=('Arial', 24, 'italic', 'bold'))
    w.pack()
    w1 = tk.Label(main, text=p1)
    w1.config(bg='turquoise',font=('Arial', 8, 'bold'))
    w1.pack(padx=5, pady=5)
    w2 = tk.Label(main, text=p2)
    w2.config(bg='pink',font=('Arial', 8, 'bold'))
    w2.pack(padx=5, pady=5)
    w3 = tk.Label(main, text=p3)
    w3.config(bg='blue',font=('Arial', 8, 'bold'))
    w3.pack(padx=5, pady=5)
    w4 = tk.Label(main, text=p4)
    w4.config(bg='red',font=('Arial', 8, 'bold'))
    w4.pack(padx=5, pady=5)
    w5 = tk.Label(main, text=p5)
    w5.config(bg='yellow',font=('Arial', 8, 'bold'))
    w5.pack(padx=5, pady=5)
