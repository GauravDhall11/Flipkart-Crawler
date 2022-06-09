import bs4
import urllib.request as url
stopwords=[]
import tkinter as tk
def display_text3():
    path1="https://www.flipkart.com/apple-iphone-xr-black-64-gb-includes-earpods-power-adapter/p/itmf9z7zxu4uqyz2?pid=MOBF9Z7ZPHGV4GNH&lid=LSTMOBF9Z7ZPHGV4GNH9IFADQ&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_2_3.banner.BANNER_apple-products-store_2XLEYVFO3M8Z&fm=neo%2Fmerchandising&iid=bf506213-c259-4446-a000-b731d3e01b7f.MOBF9Z7ZPHGV4GNH.SEARCH&ppt=browse&ppn=browse&ssid=riqs49zjps0000001604213061623"
    path2="https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=305d1d22-5fe7-4434-9de1-dcd8b33ed05e.MOBFKCTSVZAXUHGR.SEARCH&ppt=sp&ppn=sp&ssid=34gj75gdhc0000001604213264110&qH=f6cdfdaa9f3c23f3"
    path3="https://www.flipkart.com/apple-iphone-se-black-64-gb-includes-earpods-power-adapter/p/itm832dd5963a08d?pid=MOBFRFXHCKWDAC4A&lid=LSTMOBFRFXHCKWDAC4AEQROVZ&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=6eacb928-794f-4bb7-956b-3a403891c1f1.MOBFRFXHCKWDAC4A.SEARCH&ppt=sp&ppn=sp&ssid=pxekoule340000001604213287319&qH=4673a7c42221208f"
    path4="https://www.flipkart.com/apple-iphone-12-blue-64-gb/p/itm5778ad0d0d255?pid=MOBFWBYZ8DNJNY7N&lid=LSTMOBFWBYZ8DNJNY7NOXBUPN&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=a76c948b-6973-401a-8ae6-02bd8d8d3d18.MOBFWBYZ8DNJNY7N.SEARCH&ppt=sp&ppn=sp&ssid=jozy6hb7hs0000001604213345360&qH=7b7504afcaf2e1ea"
    path5="https://www.flipkart.com/apple-iphone-11-pro-midnight-green-64-gb/p/itm471de0d2e8474?pid=MOBFKCTSN3TG3RFJ&lid=LSTMOBFKCTSN3TG3RFJWPVPDJ&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_ps&fm=SEARCH&iid=67aa794e-814e-4164-b7f6-e487674779be.MOBFKCTSN3TG3RFJ.SEARCH&ppt=sp&ppn=sp&ssid=eaotv9t7lc0000001604213381988&qH=2af92350bd5b683b"
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
    w = tk.Label(main, text="Apple")
    w.config(bg='skyblue', font=('Arial', 24, 'italic', 'bold'))
    w.pack()
    w1 = tk.Label(main, text=p1)
    w1.config(bg='blue',font=('Arial', 8, 'bold'))
    w1.pack(padx=5, pady=5)
    w2 = tk.Label(main, text=p2)
    w2.config(bg='turquoise',font=('Arial', 8, 'bold'))
    w2.pack(padx=5, pady=5)
    w3 = tk.Label(main, text=p3)
    w3.config(bg='yellow',font=('Arial', 8, 'bold'))
    w3.pack(padx=5, pady=5)
    w4 = tk.Label(main, text=p4)
    w4.config(bg='pink',font=('Arial', 8, 'bold'))
    w4.pack(padx=5, pady=5)
    w5 = tk.Label(main, text=p5)
    w5.config(bg='red',font=('Arial', 8, 'bold'))
    w5.pack(padx=5, pady=5)
