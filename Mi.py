import bs4
import urllib.request as url
stopwords=[]
import tkinter as tk
def display_text5():
    path1="https://www.flipkart.com/redmi-note-8-neptune-blue-64-gb/p/itm873f03260c0a7?pid=MOBFHFFSG69TGSXQ&lid=LSTMOBFHFFSG69TGSXQU5MCK7&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Mi&fm=SEARCH&iid=b86708a3-a18e-43fb-8715-ca63046df1ee.MOBFHFFSG69TGSXQ.SEARCH&ppt=browse&ppn=browse"
    path2="https://www.flipkart.com/redmi-note-9-pro-interstellar-black-128-gb/p/itmf3ca2c1dc70d0?pid=MOBFUZYNSYP64TQK&lid=LSTMOBFUZYNSYP64TQKRLCVXM&marketplace=FLIPKART&srno=b_1_9&otracker=nmenu_sub_Electronics_0_Mi&fm=SEARCH&iid=b86708a3-a18e-43fb-8715-ca63046df1ee.MOBFUZYNSYP64TQK.SEARCH&ppt=browse&ppn=browse"
    path3="https://www.flipkart.com/redmi-8-ruby-red-64-gb/p/itm6981a578c4d90?pid=MOBFKPYDCVSCZBYR&lid=LSTMOBFKPYDCVSCZBYR7PKM5A&marketplace=FLIPKART&srno=b_1_6&otracker=nmenu_sub_Electronics_0_Mi&fm=SEARCH&iid=b86708a3-a18e-43fb-8715-ca63046df1ee.MOBFKPYDCVSCZBYR.SEARCH&ppt=browse&ppn=browse"
    path4="https://www.flipkart.com/redmi-9-prime-space-blue-128-gb/p/itmcf3b9282de0fd?pid=MOBFUT9YYVEXJHF2&lid=LSTMOBFUT9YYVEXJHF2K4J1DD&marketplace=FLIPKART&srno=b_1_4&otracker=nmenu_sub_Electronics_0_Mi&fm=SEARCH&iid=b86708a3-a18e-43fb-8715-ca63046df1ee.MOBFUT9YYVEXJHF2.SEARCH&ppt=browse&ppn=browse"
    path5="https://www.flipkart.com/redmi-8a-dual-sea-blue-32-gb/p/itmdf5aeea4214e3?pid=MOBFP764TNKZRSB8&lid=LSTMOBFP764TNKZRSB8Y3PP4A&marketplace=FLIPKART&srno=b_1_3&otracker=nmenu_sub_Electronics_0_Mi&fm=SEARCH&iid=b86708a3-a18e-43fb-8715-ca63046df1ee.MOBFP764TNKZRSB8.SEARCH&ppt=browse&ppn=browse"
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
    w = tk.Label(main, text="Mi")
    w.config(bg='skyblue', font=('Arial', 24, 'italic', 'bold'))
    w.pack()
    w1 = tk.Label(main, text=p1)
    w1.config(bg='pink',font=('Arial', 8, 'bold'))
    w1.pack(padx=5, pady=5)
    w2 = tk.Label(main, text=p2)
    w2.config(bg='red',font=('Arial', 8, 'bold'))
    w2.pack(padx=5, pady=5)
    w3 = tk.Label(main, text=p3)
    w3.config(bg='turquoise',font=('Arial', 8, 'bold'))
    w3.pack(padx=5, pady=5)
    w4 = tk.Label(main, text=p4)
    w4.config(bg='blue',font=('Arial', 8, 'bold'))
    w4.pack(padx=5, pady=5)
    w5 = tk.Label(main, text=p5)
    w5.config(bg='yellow',font=('Arial', 8, 'bold'))
    w5.pack(padx=5, pady=5)
