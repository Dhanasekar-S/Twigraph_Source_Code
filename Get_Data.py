from os import listdir
from os.path import isfile, join
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import re

numbers=['0','1','2','3','4','5','6','7','8','9']
files_in_dir = [f for f in listdir('E:\politics\Politics') if isfile(join('E:\politics\Politics', f))]
path = "E:\politics\Politics\\"
each_profile_data = []
data = ""
stop = set(stopwords.words('english'))
eset = {'you', 'we', 'it', 'get'}
for file in files_in_dir:
    data = ""
    with open(path + file, 'r', encoding="utf8") as f:
        for line in f:
            line = [i for i in str(line).lower().split() if i not in stop]
            line = [i for i in str(line).lower().split() if not str(i).__contains__("you")]
            line = [i for i in str(line).lower().split() if
                    not str(i).__contains__("http") and not str(i).__contains__("rt") ]
            line = [i for i in str(line).lower().split()  if not any(substring in i for substring in numbers)]
            line = [re.sub(r'\b\w{1,5}\b', '', i) for i in str(line).lower().split()]
            data += str(line)
    each_profile_data.append(data)

for i in files_in_dir:
    print(i)
# stemmer = SnowballStemmer("english")
# eachprofiledata1=[]
# for i in each_profile_data:
#     data1=""
#     data1+=str(i)
#     singles = [stemmer.stem(plural.strip()) for plural in data1.split(" ")]
#     data1+=str(singles)
#     eachprofiledata1.append(data1)
#
# print(stemmer.stem("apologizing"))
def get_data():
    return each_profile_data
    # count=0
    # for i in each_profile_data:
    #     print(i)
    #     print("over \n")
    #     print(count)
    #     count+=1
