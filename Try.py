import bs4
import urllib.request as url
stopwords=[]

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
p1=page1.find('span',class_="_35KyD6") + ' ' + page1.find('div',class_="_1vC4OE _3qQ9m1") + "\n" + page1.find('div',class_="g2dDAR")
p2=page2.find('span',class_="_35KyD6") + ' ' + page2.find('div',class_="_1vC4OE _3qQ9m1") + "\n" + page2.find('div',class_="g2dDAR")
p3=page3.find('span',class_="_35KyD6") + ' ' + page3.find('div',class_="_1vC4OE _3qQ9m1") + "\n" + page3.find('div',class_="g2dDAR")
p4=page4.find('span',class_="_35KyD6") + ' ' + page4.find('div',class_="_1vC4OE _3qQ9m1") + "\n" + page4.find('div',class_="g2dDAR")
p5=page5.find('span',class_="_35KyD6") + ' ' + page5.find('div',class_="_1vC4OE _3qQ9m1") + "\n" + page5.find('div',class_="g2dDAR")
for word in stopwords:
    if word in p1 and p2 and p3 and p4 and p5:
        p1=p1.replace(word,'')
        p2=p2.replace(word,'')
        p3=p3.replace(word,'')
        p4=p4.replace(word,'')
        p5=p5.replace(word,'')
print("1.",p1)
print("2.",p2)
print("3.",p3)
print("4.",p4)
print("5.",p5)