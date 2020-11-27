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
policy_stance = []
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
    policy.append(data['Policy'][0])
    newspaper.append(data['Source'])
    if len(data['About'])!=0:
        about.append(data['About'][0])
    else:
        about.append("")
    if "Policy_stance" in data.keys():
        policy_stance.append(data['Policy_stance'][0])
    else:
        policy_stance.append("")
    if "By" in data.keys():
        by.append(data['By'][0])
    else:
        by.append("")
        j = j + 1
print(i,j)
df = pd.DataFrame({'Policy':policy,'NewsPaper Name':newspaper,'article_id':a_id,'by':by,'about':about,'ideology score':score,'Policy Stance':policy_stance})
writer = pd.ExcelWriter('output3.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1',index=False)
writer.save()
#print(i)
#print(type(l),type(l[0]),l[0])


