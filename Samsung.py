import bs4
import urllib.request as url
stopwords=[]
import tkinter as tk
def display_text():
    path1="https://www.flipkart.com/samsung-galaxy-a21s-blue-128-gb/p/itm9b1380dccb8dc?pid=MOBFWCFDZWGKHXNG&lid=LSTMOBFWCFDZWGKHXNGRN8EX0&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_83d625a5-a847-4dc6-b32f-e07c6920e7bc_1_1BUWY8OBA8L9_MC.MOBFWCFDZWGKHXNG&ppt=clp&ppn=samsung-mobile-store&ssid=di4dsz3wi80000001604212305838&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_3_1.productCard.PMU_V2_Samsung%2BGalaxy%2BA21s%2B%2528Blue%252C%2B128%2BGB%2529_samsung-mobile-store_MOBFWCFDZWGKHXNG_neo%2Fmerchandising_2&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_3_NA_view-all&cid=MOBFWCFDZWGKHXNG"
    path2="https://www.flipkart.com/samsung-galaxy-f41-fusion-black-128-gb/p/itme88b8042fe996?pid=MOBFV5PWUHRY2MZZ&lid=LSTMOBFV5PWUHRY2MZZXXFGKQ&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_83d625a5-a847-4dc6-b32f-e07c6920e7bc_1_1BUWY8OBA8L9_MC.MOBFV5PWUHRY2MZZ&ppt=clp&ppn=samsung-mobile-store&ssid=di4dsz3wi80000001604212305838&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_6_1.productCard.PMU_V2_Samsung%2BGalaxy%2BF41%2B%2528Fusion%2BBlack%252C%2B128%2BGB%2529_samsung-mobile-store_MOBFV5PWUHRY2MZZ_neo%2Fmerchandising_5&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_6_NA_view-all&cid=MOBFV5PWUHRY2MZZ"
    path3="https://www.flipkart.com/samsung-galaxy-a70s-prism-crush-black-128-gb/p/itm8690f29183d3d?pid=MOBFKKGRNTSSPSSZ&marketplace=FLIPKART"
    path4="https://www.flipkart.com/samsung-galaxy-a70s-prism-crush-black-128-gb/p/itm8690f29183d3d?pid=MOBFKKGRNTSSPSSZ&marketplace=FLIPKART"
    path5="https://www.flipkart.com/samsung-galaxy-s20-cosmic-gray-128-gb/p/itm7087be7ae167c?pid=MOBFZXZ25TPA68VH&marketplace=FLIPKART"
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
    w = tk.Label(main, text="Samsung")
    w.config(bg='skyblue', font=('Arial', 24, 'italic', 'bold'))
    w.pack()
    w1 = tk.Label(main, text=p1)
    w1.config(bg='red',font=('Arial', 8, 'bold'))
    w1.pack(padx=5, pady=5)
    w2 = tk.Label(main, text=p2)
    w2.config(bg='turquoise',font=('Arial', 8, 'bold'))
    w2.pack(padx=5, pady=5)
    w3 = tk.Label(main, text=p3)
    w3.config(bg='pink',font=('Arial', 8, 'bold'))
    w3.pack(padx=5, pady=5)
    w4 = tk.Label(main, text=p4)
    w4.config(bg='blue',font=('Arial', 8, 'bold'))
    w4.pack(padx=5, pady=5)
    w5 = tk.Label(main, text=p5)
    w5.config(bg='yellow',font=('Arial', 8, 'bold'))
    w5.pack(padx=5, pady=5)