import os
##把所有aaa替换成bbb
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read().replace("aaa", "bbb")
            with open(path, "w") as f:
                f.write(content)