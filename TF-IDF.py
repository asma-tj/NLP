import locale
import codecs
from collections import Counter
import re
import string
import numpy as np
from nltk.stem.lancaster import LancasterStemmer
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

stopwords = []
text = []
line = []
finall = []
symbols = ['!', '\ ', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
           '[', ']', '^', '_', '`', '{', '|', '}', '~']


def read(name):
    out = []
    with  open("{}.txt".format(name), 'r', encoding="utf-8") as f:
        for item in f:
            out.append(item.strip())
    return out


def tokenizer(line):
    urlpattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    sitepattern = re.compile(r'www?(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

    emailpattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    Punctuationspattern = re.compile(r'[^\w]')
    idpattern = re.compile(r'@[a-zA-Z0-9_.]+')
    numberpattern = re.compile(r'[0-9]')
    url = re.findall(urlpattern, line)
    if url:
        for item in url:
            line = line.replace(item, '')
    site = re.findall(sitepattern, line)
    if site:
        for item in site:
            line = line.replace(item, '')

    email = re.findall(emailpattern, line)
    if email:
        for item in email:
            line = line.replace(item, '')

    Id = re.findall(idpattern, line)
    if Id:
        for item in Id:
            line = line.replace(item, '')

    number = re.findall(numberpattern, line)
    if number:
        for item in number:
            line = line.replace(item, '')

    Punctuations = re.findall(Punctuationspattern, line)
    if Punctuations:
        for item in Punctuations:
            line = line.replace(item, ' ')

    return line.strip()


def computeIDF(documents):
    import math
    N = 11

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / (float(val) + 1))
    return idfDict


def computeTF(wordDict, myall):
    tfDict = {}
    bagOfWordsCount = len(myall)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict


def computeTFIDF(tf, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf


st = LancasterStemmer()
text = read('my data set')
stopwords = read('stopwords')
words = []
myall = [[]] * 11
doc = []
# IIIIIDDDDDFFFFF
filename = ['Text1', 'Text2', 'Text3', 'Text4', 'Text5', 'Text6', 'Text7', 'Text8', 'Text9', 'Text10', 'Text11']
for i in range(len(filename)):
    documents = read(filename[i])
    for lines in documents:
        words = tokenizer(lines)
        line = words.split()
        for word in line:
            stemword = st.stem(word)
            if stemword not in stopwords:
                if len(stemword) > 2:
                    myall[i] = myall[i] + [stemword]

for i in range(11):
    for k in myall[i]:
        if k not in doc:
            doc.append(k)

num = [0] * 11
for i in range(11):
    numOfWord = {}
    numOfWord = dict.fromkeys(doc, 0)
    for word in myall[i]:
        numOfWord[word] += 1
    num[i] = numOfWord
IDF = computeIDF(num)

for i in IDF:
    print(i, IDF[i])
# TTTTTTTTFFFFFFFF
for i in range(11):
    TF = computeTF(num[i], myall[i])
for n in TF:
    print(n, TF[n])
TFIDF = computeTFIDF(TF, IDF)


