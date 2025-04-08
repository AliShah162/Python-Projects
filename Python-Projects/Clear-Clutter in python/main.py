import os
files=os.listdir()
files.remove("main.py")
# print(files)

def IfNotExists(folder):
 if not os.path.exists(folder):
  os.makedirs(folder)

def move(folderName,files):
 for file in files:
  os.replace(file,f"{folderName}/{file}")

IfNotExists("Media")
IfNotExists("Docs")
IfNotExists("Images")
IfNotExists("Others")
imgexts=[".png",".jpg","jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgexts]
print(images)

docsexts=[".txt",".docx","doc","pdf"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docsexts]
print(docs)

mediaexts=[".mp4",".mkv","mp5"]
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaexts]
print(medias)

others=[]
for file in files:
 ext=os.path.splitext(file)[1].lower()
 if (ext not in imgexts) and (ext not in docsexts) and (ext not in mediaexts) and os.path.isfile(file):
  others.append(file)
print(others)  

move("Media",medias)
move("Docs",docs)
move("Images",images)
move("Others",others)