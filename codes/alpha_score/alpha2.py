import os
import nltk
from nltk.metrics import agreement
from nltk.metrics.agreement import AnnotationTask
from nltk.metrics import masi_distance
from statistics import mean

def processFile(f,sentences, tags):
    lines = f.strip().split(']]')
    lines = lines[0:-1]
    num_row = len(lines)
    for i in range(0,num_row):
        #lines[i]=fileName+lines[i]
        lines[i]=lines[i]+']]'
        divided=lines[i].split('[[')
        if(len(divided)==2):
            divided[1]='[['+divided[1]
            tags.append(divided[1])
            sentences.append(divided[0])

def seperate_tags(tags,tagsOk):
    for i in range(0,len(tags)):
        tag = tags[i]
        tag=tag.replace(' ','')
        tag=tag[1:-1]
        sep_tag=tag.split('],[')
        if(len(sep_tag)==2): #change
            t1=[]
            sep_tag[0]=sep_tag[0].replace('[','')
            sep_tag[1]=sep_tag[1].replace(']','')
            s1=sep_tag[0].split(',')
            for item in s1:
                for x in item.split('-'):
                    t1.append(x)

            s2=sep_tag[1].split(',')
            for item in s2:
                for x in item.split('-'):
                    t1.append(x)

            tagsOk.append(t1)
            

def calculate_alpha(tags1,tags2):
    tagsOk1=[]
    tagsOk2=[]
    task_data=[]
    seperate_tags(tags1,tagsOk1)
    seperate_tags(tags2,tagsOk2)
    if(len(tagsOk1) == 0):
        print("empty")
    for i in range(0,len(tagsOk1)):
        task_data.append(('coder1','Item'+str(i),frozenset(tagsOk1[i])))
        task_data.append(('coder2','Item'+str(i),frozenset(tagsOk2[i])))

    task = AnnotationTask(distance = masi_distance)

    task.load_array(task_data)

    return(task.alpha())

    


file1=[]
path1= #put path of annotator 1
path2= #put path of annotator 2
for file_n in os.listdir(path1):
    if file_n.endswith('.txt'):
        file1.append(file_n)

alpha=[]
for file_n in os.listdir(path2):
    if file_n.endswith('.txt'):
        if file_n in file1:
            with open(path1+'/'+file_n, 'r') as f1:
                data1= f1.read()
            
            with open(path2+'/'+file_n, 'r') as f2:
                data2= f2.read()
            
            sentences1=[]
            sentences2=[]
            tags1=[]
            tags2=[]
            processFile(data1,sentences1, tags1)
            processFile(data2,sentences2, tags2)
            if(len(sentences1) == len(sentences2)):
                alpha.append(calculate_alpha(tags1,tags2))

print(mean(alpha))