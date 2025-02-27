import os

file_path = "/All My Website using Next.js code/"

content = os.listdir(file_path)
for item in content:
    print(item)
