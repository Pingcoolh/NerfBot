import requests, bs4

res = requests.get("http://nerf.wikia.com/wiki/Alpha_Trooper_CS-12")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select("aside")
info = elems[0].select(".pi-data")

msg = ""
for data in info:
    msg = msg + "\n" + data.select("h3")[0].getText() + ": " + data.select("div")[0].getText()
print(msg)