import bs4
import urllib.request as url

movie = input('Enter movie name:')
m= '+'.join(movie.split())
path='https://www.imdb.com/find?ref_=nv_sr_sm&q='+m

http = url.urlopen(path)
page = bs4.BeautifulSoup(http,'lxml')

title = page.find('td',class_="result_text")
print('Title:',title.text)

div = page.find('td',class_="result_text")
a_tag = div.find('a')
hr = a_tag['href']
newurl = 'https://www.imdb.com' + hr
#print(newurl)
http1 = url.urlopen(newurl)
page1 = bs4.BeautifulSoup(http1,'lxml')

s = page1.find('div', class_="summary_text")
print('\nSummary:',s.text.strip())

atag = page1.find_all('a',class_="quicklink")
rhr = atag[2]['href']
newurl2='https://www.imdb.com'+rhr

http2 = url.urlopen(newurl2)
page2 = bs4.BeautifulSoup(http2,'lxml')

rating = page2.find_all('span',class_="rating-other-user-rating")
review = page2.find_all('a',class_="title")

print("\nReviews and Ratings:\n")

for i,j in zip(rating,review):
    print(i.text.strip() , j.text.strip())
