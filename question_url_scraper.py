import requests, json, os, time
from bs4 import BeautifulSoup

topics = []
for topicGroup in sorted(os.listdir("archive/tags"))[12:]:
    with open("archive/tags/" + topicGroup, "r") as f:
        topics = json.loads(f.read())
    for topic in topics:
        print("Scraping topic: " + topic)
        questions = []
        for page in range(1, 11):
            res = requests.get("https://answers.unity.com/" + topic + "?page=" + str(page) + "&sort=viewCount&filter=all")
            soup = BeautifulSoup(res.text, "html.parser")
            try:
                for qbox in soup.find("div", {"id":"id_topic_content"}).find_all("div", {"class": "info"}):
                    questions.append(qbox.find("h4", {"class": "title"}).find("a")["href"])
            except Exception:
                print(Exception)
            print("Scraping page " + str(page))
        with open("archive/to_archive/" + topic.replace("/topics/", "").replace(".html", "") + ".json", "w") as f:
            f.write(json.dumps(questions))
        print("topic: " + topic + ", finished scraping")
        time.sleep(1)