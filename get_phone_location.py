import requests
def get_phone_location(phone_number):
    base_url = 'http://shouji.xpcha.com/{}.html'
    url = base_url.format(phone_number)

    r = requests.get(url, timeout=30)

    html=r.text

    soup = BeautifulSoup(html, "html.parser")

    resutl=soup.find('meta',attrs={'name':'description'})

    return resutl.attrs['content'].split('，')[1]
