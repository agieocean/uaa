import requests, json, os, time, signal
from bs4 import BeautifulSoup

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
# Number of pages to scrape from each question
#pageNum = 5
questions = []
for category in os.listdir("archive/missing"):
    with open("archive/missing/" + category, "r") as f:
        questions = json.loads(f.read())
    for question in questions:
        if question == "#":
            break
        #time.sleep(5)
        print(category + "/" + question + ", scraping")
        try:
            r = requests.get("https://answers.unity.com/" + question, timeout=10)
        except Exception as e:
            print(e)
            continue
        #soup = BeautifulSoup(r.text, "html.parser")
        #reshtml = soup.find("div", {"class", "post-container question-container"})
        if os.path.exists("archive/questions/" + question.split("/")[2]) != True:
            os.makedirs("archive/questions/" + question.split("/")[2])
        with open("archive/questions/" + question.split("/")[2] + "/page.1.html", "w") as f:
            f.write(str(r.text))
        it = 2
        catchallBreak = False
        while not catchallBreak:
            print("Scraping more pages for: " + category + "/" + question)
            try:
                r = requests.get("https://answers.unity.com/" + question + "?page=" + str(it), timeout=10)
                with timeout(seconds=20):
                    if BeautifulSoup(
                        r.text, "html.parser"
                        ).find(
                            "div", {"class": "widget widget-nopad answer-list"}
                            ).find(
                            "div", {"class", "widget-content"}).find("div"):
                        with open("archive/questions/" + question.split("/")[2] + "/page." + str(it) + ".html", "w") as f:
                            f.write(str(r.text))
                        it += 1
                    else:
                        catchallBreak = True
                        break
                    if it > 10:
                        catchallBreak = True
            except Exception as e:
                print(e)
                break
