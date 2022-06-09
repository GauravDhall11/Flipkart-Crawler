import bs4
import urllib.request as url
stopwords=[' Expandable','Upto','512 GB','5000 mAh Lithium-ion Polymer Battery','Camera']
path1="https://www.flipkart.com/mobiles/pr?sid=tyy,4io&p[]=facets.brand%255B%255D%3DPOCO&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp14&fm=neo%2Fmerchandising&iid=M_a985cbaf-b439-4678-9c27-8a78b5c25ea5_16.O1WYX08RHODP&ppt=clp&ppn=mobile-phones-store"
path2="https://www.flipkart.com/mobiles/pr?sid=tyy,4io&p[]=facets.brand%255B%255D%3DPOCO&otracker=clp_metro_expandable_2_16.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp14&fm=neo%2Fmerchandising&iid=M_a985cbaf-b439-4678-9c27-8a78b5c25ea5_16.O1WYX08RHODP&ppt=clp&ppn=mobile-phones-store"
http=url.urlopen(path1)
http2=url.urlopen(path2)
page1=bs4.BeautifulSoup(http,"lxml")
page2=bs4.BeautifulSoup(http2,"lxml")
p1=page1.find('div',class_='_3wU53n').text + ' ' + page1.find('div',class_='_1vC4OE _2rQ-NK').text + '\n' + page1.find('ul',class_='vFw0gD').text
p2=page2.find('div',class_='_3wU53n').text
for word in stopwords:
    if word in p1 and p2:
        p1=p1.replace(word,'')
        p2 = p2.replace(word, '')
p1=p1.replace('Display48MP','Display 48MP')
print(p1[0:179])
print(p2)

