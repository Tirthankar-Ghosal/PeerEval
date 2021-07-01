import os
import json
import re
import ast 
path='meta_data'
#path='sample'
meta_data=[]
review_id=[]
for file_n in os.listdir(path):
    if not file_n.startswith('.'):  
        with open(path+'/'+file_n, "r+") as f:
            data = json.loads(f.read())
            meta_data.append(data['comment'])
            print(data['comment'])
            review_id.append(data['review_id'])
            print(data['review_id'])
            f.close()