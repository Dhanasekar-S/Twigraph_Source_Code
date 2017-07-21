from os import listdir
from os.path import isfile, join
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import re
import fileinput

numbers=['0','1','2','3','4','5','6','7','8','9']
files_in_dir = [f for f in listdir('E:\politics\Politics') if isfile(join('E:\politics\Politics', f))]
path = "E:\politics\Politics\\"
data = ""
stop = set(stopwords.words('english'))
eset = {'you', 'we', 'it', 'get'}
line1=[]
for file in files_in_dir:
    data = ""
    with open(path + file, 'r+', encoding="utf8") as f:
        for line in f:
            nuts=str(line1).lower().split()
            line1 = [i for i in nuts if i not in stop]
            line1 = [i for i in nuts if
                    not str(i).__contains__("http") and not str(i).__contains__("rt") ]
            line1 = [i for i in nuts  if not any(substring in i for substring in numbers)]
            line1 = [re.sub(r'\b\w{1,5}\b', '', i) for i in nuts]
            data += str(line1)
            f.write(line.replace(str(line),data))
f.close()
for i in files_in_dir:
    print(i)
