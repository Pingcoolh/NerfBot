import requests, bs4

# Convert HTML to BS object
res = requests.get("http://nerf.wikia.com/wiki/Category:N-Strike_blasters")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Find elements
elems = soup.select("tr")
info = elems[0].select("a")

# Get the text
for data in info:
    print(data.getText() + ": " + data.attrs["href"])



def get_gun_info():
    res = requests.get("http://nerf.wikia.com/wiki/Hailfire")

    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select("aside")
    info = elems[0].select(".pi-data")

    msg = ""
    for data in info:
        msg = msg + "\n" + data.select("h3")[0].getText() + ": " + data.select("div")[0].getText()
    return msg
print(get_gun_info())