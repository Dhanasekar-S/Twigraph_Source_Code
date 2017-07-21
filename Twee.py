import math
from textblob import TextBlob as tb
from scipy import spatial
import Get_Data as twitterdata


docs= twitterdata.get_data()
for i in range(docs.__len__()):
    docs[i]=tb(docs[i])

n_of_docs=docs.__len__()

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)



bloblist = [i for i in docs]

# for i, blob in enumerate(bloblist):
#     print("Top words in document {}".format(i + 1))
#     scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
#     sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#     for word, score in sorted_words[:3]:
#         print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


document4 = docs[1]
scores = {word: tfidf(word, document4, bloblist) for word in document4.words}
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for word, score in sorted_words[:10]:
 print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


d1=[]
d2=[]
d3=[]
d4=[]
for word in sorted_words[:50]:
 #print(word)
 d1.append(tfidf(word, document4, bloblist))
 d2.append(tfidf(word, docs[0], bloblist))
 d3.append(tfidf(word, docs[1], bloblist))
 d4.append(tfidf(word, docs[2], bloblist))
# dataSetI = {word: tfidf(word, document4, bloblist) for word in document4}
# dataSetII = {word: tfidf(word, document1, bloblist) for word in document4}
# datasetIII={word: tfidf(word, document2, bloblist) for word in document4}
# dataset4={word: tfidf(word, document3, bloblist) for word in document4}

print(d1,d2,d3,d4)
result = 1 - spatial.distance.cosine(d1, d2)
result1 = 1 - spatial.distance.cosine(d1, d3)
result2 = 1 - spatial.distance.cosine(d1, d4)


print(result,result1,result2)