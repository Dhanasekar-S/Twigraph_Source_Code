import Get_Data as twitterdata
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial

#corpus=["all is well","best of luck","best of luck","best of all"]
corpus = twitterdata.get_data()
n_of_articles = corpus.__len__()
vectorizer = TfidfVectorizer(min_df=1)
vectorizer.__init__(norm=u'l1', smooth_idf=False)

X = vectorizer.fit_transform(corpus)
# print (dict(zip(vectorizer.get_feature_names(), idf)))

feature_names = vectorizer.get_feature_names()
scores_relative_to_comparing = []
ss = []
doc = 1
feature_index = X[doc, :].nonzero()[1]

writer = open('idf.txt', 'w', encoding="utf8")
for i in range(vectorizer.idf_.__len__()):
    writer.write(str(vectorizer.idf_[i]))
    writer.write(" ")
    writer.write(str(feature_names[i]))
    writer.write("\n")
writer.close()

c = twitterdata.files_in_dir
cc=0
# for i in range(vectorizer.idf_.__len__()):
#     print(feature_names[i])
#     print(vectorizer.idf_[i])

for tt in range(n_of_articles):
    writer = open('query_' + str(c[cc]), 'w', encoding="utf8")
    tfidf_scores = zip(feature_index, [X[tt, x] for x in feature_index])
    ss = []
    for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
        # print(w, s)
        ss.append(s)
        writer.write(w)
        writer.write(" ")
        writer.write(str(s))
        writer.write("\n")
    cc += 1
    scores_relative_to_comparing.append(ss)
writer.close()

writer = open('distance.txt', 'w', encoding="utf8")

# for i in scores_relative_to_comparing:
#     print(i)
#     print("\n\n")
c = 0
writer.write("The file contains distance and similarity of the query profile and corpus consecutively \n")
for i in range(n_of_articles):
    result = 1 - (spatial.distance.cosine(scores_relative_to_comparing[doc], scores_relative_to_comparing[i]))
    print("Similarity between document "+str(twitterdata.files_in_dir[doc][:-11])+ " and " + str(twitterdata.files_in_dir[c][:-11]))
    print(result)
    writer.write("Between document "+str(twitterdata.files_in_dir[doc][:-11])+ " and " + str(twitterdata.files_in_dir[c][:-11]) + " ")
    writer.write(str(1 - result) + " ")
    writer.write(str(result))
    writer.write("\n")
    c += 1
writer.close()


def get_scores():
    return scores_relative_to_comparing
