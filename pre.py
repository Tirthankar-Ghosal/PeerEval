import nltk
import re
import numpy as np
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')
from nltk.stem import PorterStemmer
nltk.download('stopwords')
nltk.download('wordnet')
porter = PorterStemmer()
from nltk.tokenize import word_tokenize, sent_tokenize 
stop_words = set(stopwords.words('english'))
nltk.download('punkt')
tag_list=[]
import pandas as pd
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
from nltk.corpus import wordnet

import pickle
#retriving 
pickle_in = open("/content/sentence.pickle","rb")
un_sentences = pickle.load(pickle_in)   #unprocessed sentences
pickle_in = open("/content/fileid.pickle","rb")
fileid = pickle.load(pickle_in)
pickle_in = open("/content/tags.pickle","rb")
tags = pickle.load(pickle_in)

num_rows = len(un_sentences)

splitted=[]
def preprocess():
  for i in range(0,num_rows):
    divided=un_sentences[i]
    divided=(re.sub(r'\\n','',divided)).strip()
    divided=(re.sub(r'[\\]','',divided))
    divided=(re.sub(r'[(),:.";?><]','',divided))
    divided=(re.sub(r'[0-9]*','',divided)).strip()
    divided=(re.sub(r" [?\([^)]-+\)]", '',divided))
    splitted.append(divided)
  return splitted

num_rows=len(preprocess())
splitted=preprocess()
print(splitted)


def normal_preprocess():
  norm=[]
  for i in range(0,num_rows):
    divided=un_sentences[i]
    divided=(re.sub(r'\\n','',divided)).strip()
    divided=(re.sub(r'[\\]','',divided))
    norm.append(divided)
  return norm

  
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 


 #lemetizing sentence
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()
def nltk2wn_tag(nltk_tag):
  if nltk_tag.startswith('J'):
    return wordnet.ADJ
  elif nltk_tag.startswith('V'):
    return wordnet.VERB
  elif nltk_tag.startswith('N'):
    return wordnet.NOUN
  elif nltk_tag.startswith('R'):
    return wordnet.ADV
  else:          
    return None

def lemmatize_sentence(sentence):
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
    wn_tagged = map(lambda x: (x[0], nltk2wn_tag(x[1])), nltk_tagged)
    res_words = []
    for word, tag in wn_tagged:
      if tag is None:            
        res_words.append(word)
      else:
        res_words.append(lemmatizer.lemmatize(word, tag))
    return " ".join(res_words)

#i=0 for normal text and i=1 for processed text
def create_sentence_list(i):
  if i is 1:
    splitted=preprocess()
  else:
    splitted=normal_preprocess()
  sentence_list=[]
  for row in range(num_rows):
    sentence_list.append(lemmatizer.lemmatize(porter.stem(splitted[row].lower())))
  #print(sentence_list)
  return sentence_list

#---------------now tag-----------------------------
def normal_tag(word):
  sep=[]
  ws=word.split(',')
  for w in ws:
    tar=(w.split('-'))[0]
    sep.append(tar.upper())
  return sep

#use create_label(0) to access tag-1, and so on 
def create_label(i):
  label=[]
  for row in range(num_rows):
    label.append(normal_tag(tags[row][i]))
  return label

def create_tag_vs_sen(j):
  labels = create_label(j)
  label_dic={}
  for i in range(0,num_rows):
    for label in labels[i]:
      if label in label_dic.keys():
        label_dic[label].append(i)   #sentences[i]
      else:
        label_dic[label]=[i]
  return label_dic

#'''

def collect_tags(i):
  return seperate_tags(i)

def create_tag_list():
  tag_list=[]
  for i in range(num_rows):
    collect_tags(i)
    #tag_list.append(collect_tags(i))
    #print(collect_tags(i))
  return tag_list





#returns stopword removed sentences in list [['authors', 'argue'], ['paper', 'due']]
def stop_word_removed_sen():
  li=create_sentence_list(1)
  removed=[]
  for l in li:
    wordsList = nltk.word_tokenize(l.lower()) 
    # removing stop words from wordList
    wordsList_new=[]
    wordsList = [w for w in wordsList if not w in stop_words]
    for word in wordsList:
      if len(word)>2:
        wordsList_new.append(word)
    removed.append(wordsList)
  return removed

def word_sen(): #for list of list of tokenized words of each and every sentences
  li=create_sentence_list(1)
  removed=[]
  for l in li:
    wordsList = nltk.word_tokenize(l) 
    # removing stop words from wordList
    wordsList_new=[]
    for word in wordsList:
      if len(word)>2:
        wordsList_new.append(word)
    removed.append(wordsList)
  return removed


#i=0 for normal i=1 for tokenized list of words of a sentences
def word_list(i):
  wor_list=[]
  if i is 0:
    lis=word_sen()
  else:
    lis=stop_word_removed_sen()
  for l in lis:
    for w in l:
      if w not in wor_list:
        wor_list.append(w)
  return wor_list

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if (token not in stop_words and len(token)>3)]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc

#The vectorize function is provided primarily for convenience, not for performance.
#The implementation is essentially a for loop.
# Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs 
# and returns a single numpy array or a tuple of numpy arrays.
corpus=create_sentence_list(1)
normalize_corpus = np.vectorize(normalize_document)
norm_corpus = normalize_corpus(corpus)
