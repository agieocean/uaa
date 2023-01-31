import requests, json
from bs4 import BeautifulSoup
for it in range(1, 55):
    r = requests.get("https://answers.unity.com/topics.html?page=" + str(it))
    soup = BeautifulSoup(r.text, "html.parser")
    tags = soup.find("div", {"id": "tagpix"})
    tagList = []
    for tag in tags.find_all("li"):
        for ltag in tag.find_all("a", href=True):
            if "topic" in ltag["href"]:
                tagList.append(ltag["href"])
    with open("archive/tags/tag_page_" + str(it) + ".json", "w") as f:
        f.write(json.dumps(tagList))
    print( str(it) + "/55")