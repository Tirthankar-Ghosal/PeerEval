import os

commonFilePath= "/Users//nlp/project/commonfile.txt" #put file path
commonFile= open(commonFilePath, "w+")
commonLines = []
rel_path = '/Users//nlp/project/datasets/'  #put file path
tags=[]
fileId=[]
sentences=[]
sentencesOk=[]
fileIdOk=[]
tagsOk=[]
def processFile(file,fileName):
    lines = file.read().strip().split(']]')
    lines = lines[0:-1]
    global num_rows
    num_row = len(lines)
    for i in range(0,num_row):
        #lines[i]=fileName+lines[i]
        lines[i]=lines[i]+']]'
        divided=lines[i].split('[[')
        if(len(divided)==2):
            divided[1]='[['+divided[1]
            tags.append(divided[1])
            fileId.append(fileName)
            sentences.append(divided[0])

def readFile(fileName):
    singleFile = open(rel_path+ fileName, encoding='utf-8')
    processFile(singleFile,fileName)
    #commonLines.append(processFile(singleFile,fileName))
    #print(commonLines)
    #commonFile.write(str(commonLines))



def readFiles(path):
    for file in os.listdir(path):
        if not file.startswith('.'):
            readFile(file)
    commonFile.close()

readFiles(rel_path)
num_rows=len(sentences)
def seperate_tags():
    for i in range(0,num_rows):
        tag=tags[i]
        tag=tag.replace(' ','')
        tag=tag[1:-1]
        tag=tag.upper()
        sep_tag=tag.split('],[')
        if(len(sep_tag)==4):
            sep_tag[0]=sep_tag[0].replace('[','')
            sep_tag[3]=sep_tag[3].replace(']','')
            sentencesOk.append(sentences[i])
            fileIdOk.append(fileId[i])
            tagsOk.append(sep_tag)
seperate_tags()

import pickle

pickle_out = open("/Users//nlp/project/sentence.pickle","wb")
pickle.dump(sentencesOk, pickle_out)
pickle_out.close()

pickle_out = open("/Users//nlp/project/fileid.pickle","wb")
pickle.dump(fileIdOk, pickle_out)
pickle_out.close()

pickle_out = open("/Users//nlp/project/tags.pickle","wb")
pickle.dump(tagsOk, pickle_out)
pickle_out.close()