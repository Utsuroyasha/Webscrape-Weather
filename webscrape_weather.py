from wsgiref import headers
from requests_html import HTMLSession

s = HTMLSession()

query = 'miami'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'})

temp = r.html.find('Span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.wob_dcp', first=True).find('span#wob_dc', first=True).text
time_day = r.html.find('div.wob_dts', first=True).text

print(query, temp + unit, desc, time_day)
