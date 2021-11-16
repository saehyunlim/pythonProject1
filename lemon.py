from bs4 import beautifulsoup4
url = 'https://www.reddit.com/r/Bitcoin/comments/qbthox/daily_discussion_october_20_2021/'
response = requests.get(url)
if response.status_code ==200;
html = response.text
soup = BeautifulSoup(html,'html.parser')
title = soup.select_one('//*[@id="t1_hhgex9u"]/div[2]/div[2]/div[2]/div/p')
print(title)
else :
  print(response.status_code)