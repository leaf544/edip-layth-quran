import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

def fetch_surah(surah):
    url = "https://quranix.org/" + str(surah) + "/"
    uClient = uReq(url)
    page = uClient.read()
    uClient.close()
    page_soup = Soup(page, "html.parser")
    
    containers = page_soup.findAll("div", {"class":"translation tr-qmt"})

    f = open(str(surah) + ".txt", "w", encoding="utf-8")
    thing = None
    
    for i in range(1, len(containers)):
        thing = containers[i].find("span", "ayahText").string
        if thing == None:
            print("None found")
        else:
            f.write("("+str(surah)+":"+str(i)+") " + thing + "\n")

    f.write("\n\n\n\n\n\n\n\n\n\n\n")
    print("Finished Surah " + str(surah))

    
for i in range(1, 115):
    fetch_surah(i)

# fetch_surah(3)
