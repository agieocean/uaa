from bs4 import BeautifulSoup
import json, os, multiprocessing

questionspre = os.listdir("questions")[24935+6490+973+104228+35468+34199:]
questions = []
for it, question in enumerate(questionspre):
    questions.append([it, question])
numquestions = len(questions)


def convert(question):
    print("{0}/{1}".format(question[0], str(numquestions)))
    if len([f for f in os.listdir("questions/" + question[1]) if ".json" in f]) == 0:
        for f in os.listdir("questions/" + question[1]):
            if ".html" in f:
                fpath = "questions/" + question[1] + "/" + f
                pageText = ""
                with open(fpath, "r", encoding="utf8") as f:
                    pageText = f.read()
                soup = BeautifulSoup(pageText, "html.parser")
                questionTitle = soup.find("h1", {"class": "question-title"}).text
                questionBody = soup.find("div", {"class": "question-body"}).text
                replies = []
                for reply in soup.findAll("div", {"class": "answer-body"}):
                    replies.append(reply.text)
                tags = []
                for tag in soup.find("span", {"class": "tags"}).findAll("a"):
                    tags.append(tag.text)
                if "1" in fpath.split("/")[-1] or not ("page.json" in os.listdir("questions/" + question[1])):
                    with open(fpath.split(".")[0] + ".json", "w", encoding="utf8") as f:
                        f.write(json.dumps({
                            "title": questionTitle,
                            "body": questionBody,
                            "replies": replies,
                            "tags": tags
                        }
                        ))
                else:
                    curf = {}
                    with open(fpath.split(".")[0] + ".json", "r", encoding="utf8") as f:
                        curf = json.loads(f.read())
                    curf["replies"] + replies
                    with open(fpath.split(".")[0] + ".json", "w", encoding="utf8") as f:
                        f.write(json.dumps(curf))

#convert("page.1.html")

cpu_count = multiprocessing.cpu_count()


pool = multiprocessing.Pool(cpu_count)
pool.map(convert, questions)
pool.close()
pool.join()
    