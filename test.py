import requests, bs4

# Convert HTML to BS object
'''res = requests.get("http://nerf.wikia.com/wiki/Category:N-Strike_blasters") # get the HTML
soup = bs4.BeautifulSoup(res.text, "html.parser") # Parse the HTML into soup object

# Find elements
elems = soup.select("tr") # get list of all tr tags in the soup object
info = elems[0].select("a") # get list of all a tags in first tr tag

# Get the text
for data in info: # Iterate through the info list
    print(data.getText() + ": " + data.attrs["href"]) # print out the text in the tag and the attribute "href" (the link)
'''

def search(search):
    res = requests.get("http://nerf.wikia.com/wiki/Special:Search?search=" + search.replace(' ', '+'))
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(".Results")
    results = elems[0].select("a")
    return get_gun(results[0].attrs["href"])


def get_gun(url):
    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select("aside")
    info = elems[0].select(".pi-data")

    msg = ""
    for data in info:
        msg = msg + "\n" + data.select("h3")[0].getText() + ": " + data.select("div")[0].getText()
    return msg

print(search("hailfire"))