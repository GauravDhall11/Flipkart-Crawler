import bs4
import urllib.request as url
stopwords=[]
import tkinter as tk
def display_text4():
    path1="https://www.flipkart.com/vivo-v20-sunset-melody-256-gb/p/itm3c6e689e97959?pid=MOBFVWB4ABCGNZQG&lid=LSTMOBFVWB4ABCGNZQGJ9MU8P&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Vivo&fm=SEARCH&iid=cc966c6a-603d-4be7-a6d8-a2229285bb39.MOBFVWB4ABCGNZQG.SEARCH&ppt=browse&ppn=browse&ssid=53xpdab9k00000001604213480357"
    path2="https://www.flipkart.com/vivo-s1-pro-mystic-black-128-gb/p/itm60bf6c78dfe9a?pid=MOBFNENDVWSUPNHH&lid=LSTMOBFNENDVWSUPNHHXIQTLM&marketplace=FLIPKART&srno=b_1_9&otracker=nmenu_sub_Electronics_0_Vivo&fm=SEARCH&iid=cc966c6a-603d-4be7-a6d8-a2229285bb39.MOBFNENDVWSUPNHH.SEARCH&ppt=browse&ppn=browse&ssid=53xpdab9k00000001604213480357"
    path3="https://www.flipkart.com/vivo-y50-iris-blue-128-gb/p/itmd0dcc06ffbe06?pid=MOBFSCFZPGRX6UFJ&lid=LSTMOBFSCFZPGRX6UFJOLVPXK&marketplace=FLIPKART&srno=b_1_6&otracker=nmenu_sub_Electronics_0_Vivo&fm=SEARCH&iid=cc966c6a-603d-4be7-a6d8-a2229285bb39.MOBFSCFZPGRX6UFJ.SEARCH&ppt=browse&ppn=browse&ssid=53xpdab9k00000001604213480357"
    path4="https://www.flipkart.com/vivo-y20-purist-blue-64-gb/p/itm10285cb0a8dd9?pid=MOBFUU8SGHTDYC6F&lid=LSTMOBFUU8SGHTDYC6FFERICB&marketplace=FLIPKART&srno=b_1_14&otracker=nmenu_sub_Electronics_0_Vivo&fm=SEARCH&iid=cc966c6a-603d-4be7-a6d8-a2229285bb39.MOBFUU8SGHTDYC6F.SEARCH&ppt=browse&ppn=browse&ssid=53xpdab9k00000001604213480357"
    path5="https://www.flipkart.com/vivo-y30-dazzle-blue-128-gb/p/itm1791342f24d04?pid=MOBFT26A63WG6Z8F&lid=LSTMOBFT26A63WG6Z8FH46N8L&marketplace=FLIPKART&srno=b_1_12&otracker=nmenu_sub_Electronics_0_Vivo&fm=SEARCH&iid=cc966c6a-603d-4be7-a6d8-a2229285bb39.MOBFT26A63WG6Z8F.SEARCH&ppt=browse&ppn=browse&ssid=53xpdab9k00000001604213480357"
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
    w = tk.Label(main, text="Vivo")
    w.config(bg='skyblue', font=('Arial', 24, 'italic', 'bold'))
    w.pack()
    w1 = tk.Label(main, text=p1)
    w1.config(bg='yellow',font=('Arial', 7, 'bold'))
    w1.pack(padx=5, pady=5)
    w2 = tk.Label(main, text=p2)
    w2.config(bg='blue',font=('Arial', 8, 'bold'))
    w2.pack(padx=5, pady=5)
    w3 = tk.Label(main, text=p3)
    w3.config(bg='red',font=('Arial', 8, 'bold'))
    w3.pack(padx=5, pady=5)
    w4 = tk.Label(main, text=p4)
    w4.config(bg='turquoise',font=('Arial', 8, 'bold'))
    w4.pack(padx=5, pady=5)
    w5 = tk.Label(main, text=p5)
    w5.config(bg='pink',font=('Arial', 8, 'bold'))
    w5.pack(padx=5, pady=5)
