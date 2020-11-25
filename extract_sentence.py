import pymongo
import pandas as pd
import xlsxwriter
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["media-db"]
all_collection = db.list_collection_names()
col = db["by_about"]
x = col.find()
score = []
article_id = []
policy = []
about = []
newspaper = []
by = []
a_id = []
i = 0
j = 0
for data in x:
    if "Class" in data.keys():
        score.append(data['Class'])
    else:
        score.append(-1)
        i = i+1
    a_id.append(data['ArticleID'])
    policy.append(data['Policy'])
    newspaper.append(data['Source'])
    about.append(data['About'])
    if "By" in data.keys():
        by.append(data['By'])
    else:
        by.append("")
        j = j + 1
print(i,j)
df = pd.DataFrame({'Policy':policy,'NewsPaper Name':newspaper,'article_id':a_id,'by':by,'about':about,'ideology score':score})
writer = pd.ExcelWriter('output.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1',index=False)
writer.save()
#print(i)
#print(type(l),type(l[0]),l[0])


