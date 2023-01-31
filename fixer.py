import os, shutil

files = os.listdir("questions_json")
num_files = len(files)

for f in files:
    if os.path.isdir("questions_json/" + f):
        shutil.rmtree("questions_json/" + f)
    else if not(".json" in f):
        os.remove("questions_json/" + f)
