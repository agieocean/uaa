import os, json


if os.path.exists("archive/missing") != True:
          os.makedirs("archive/missing")
questionStatic = os.listdir("archive/questions")
questionStaticFix = []
for question in questionStatic:
          questionStaticFix.append(str(question))
questionStatic = questionStaticFix
#print(type(questionStatic[0]))
#print(questionStatic)
for topic in os.listdir("archive/to_archive"):
          questions = []
          questionsMissing = []
          with open("archive/to_archive/" + topic, "r") as f:
                    questions = json.loads(f.read())
          questionsFix = []
          for question in questions:
                    if question != "#":
                              questionsFix.append(question)
          questions = questionsFix
          for question in questions:
                    #print(question)
                    qid = question.split("/")[2]
                    qid = str(qid)
                    #print(type(qid))
                    if (qid in questionStatic) != True:
                              questionsMissing.append(question)
                              print(qid)
                    else:
                              pass
                              #print("no")
          with open("archive/missing/" + topic, "w") as f:
                    f.write(json.dumps(questionsMissing))
