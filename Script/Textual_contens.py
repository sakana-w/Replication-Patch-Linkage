import nltk.stem
import csv
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import word_tokenize,sent_tokenize
from nltk import SnowballStemmer
from gensim import corpora,models,similarities
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
import pandas
porter=nltk.PorterStemmer()
st = LancasterStemmer()
st.stem('stemmed')
colnames = ['changeid', 'title','message']
data_test = pandas.read_excel('testing_data',names=colnames)
data_train = pandas.read_excel('training_data',names=colnames)
dic1 = {}
stemmer = PorterStemmer()
with open('Pair_match','r') as csvfile:
    read = csv.reader (csvfile, delimiter=',')
    for row in read:
        pa = int(row[0])
        pb = int(row[1])
        dic1[pa] = pb
        
    
all_doc = data_train.title.tolist()
all_doc_reviewid = data_train.changeid.tolist()
all_test = data_test.title.tolist()
all_test_reviewid = data_test.changeid.tolist()
all_doc_list = []
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
s = nltk.stem.SnowballStemmer('english')
for doc in all_doc:
    doc_token = [word for word in nltk.word_tokenize(doc)]
    doc_stop = [w for w in doc_token if(w.lower() not in stopwords.words('english'))]
    doc_punctuations = [w for w in doc_stop if w not in english_punctuations]  
    doc_stemmed=[porter.stem(t) for t in doc_punctuations]
    all_doc_list.append(doc_stemmed)    
    
dictionary = corpora.Dictionary(all_doc_list)
dictionary.keys()
dictionary.token2id
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
tfidf = models.TfidfModel(corpus)  
count = 0
acc=[]
score = []
position = []
output= []
dict_result = {};
for test in all_test:
        doc_test_token = [word for word in nltk.word_tokenize(test)]
        doc_test_stop = [w for w in doc_test_token if(w.lower() not in stopwords.words('english'))]
        doc_test_punctuations = [w for w in doc_test_stop if w not in english_punctuations]
        doc_test_stemmed=[porter.stem(t) for t in doc_test_punctuations]

        doc_test_vec = dictionary.doc2bow(doc_test_stemmed)
        tfidf[doc_test_vec]
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
        sim = index[tfidf[doc_test_vec]]
        sim = sorted(enumerate(sim), key=lambda item: -item[1])
        top1=sim[0][0]
        top2=sim[1][0]
        top3=sim[2][0]
        top4=sim[3][0]
        top5=sim[4][0]
        top6=sim[5][0]
        top7=sim[6][0]
        top8=sim[7][0]
        top9=sim[8][0]
        top10=sim[9][0]
        merged_review_reviewid1 = all_doc_reviewid[top1]
        merged_review_reviewid2 = all_doc_reviewid[top2]
        merged_review_reviewid3 = all_doc_reviewid[top3]
        merged_review_reviewid4 = all_doc_reviewid[top4]
        merged_review_reviewid5 = all_doc_reviewid[top5]
        merged_review_reviewid6 = all_doc_reviewid[top6]
        merged_review_reviewid7 = all_doc_reviewid[top7]
        merged_review_reviewid8 = all_doc_reviewid[top8]
        merged_review_reviewid9 = all_doc_reviewid[top9]
        merged_review_reviewid10 = all_doc_reviewid[top10]
    
        abandoned_review_reviewid = all_test_reviewid[count]

        if (dic1[abandoned_review_reviewid] == merged_review_reviewid1):
            acc.append(1)
            score.append(1)
            output.append(abandoned_review_reviewid)
            position.append(1)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid2):
            acc.append(1)
            score.append(1/2)
            output.append(abandoned_review_reviewid)
            position.append(2)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid3):
            acc.append(1)
            score.append(1/3)
            output.append(abandoned_review_reviewid)
            position.append(3)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid4):
            acc.append(1)
            score.append(1/4)
            output.append(abandoned_review_reviewid)
            position.append(4)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid5):
            acc.append(1)
            score.append(1/5)
            output.append(abandoned_review_reviewid)
            position.append(5)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid6):
            acc.append(1)
            score.append(1/6)
            output.append(abandoned_review_reviewid)
            position.append(6)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid7):
            acc.append(1)
            score.append(1/7)
            output.append(abandoned_review_reviewid)
            position.append(7)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid8):
            acc.append(1)
            score.append(1/8)
            output.append(abandoned_review_reviewid)
            position.append(8)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid9):
            acc.append(1)
            score.append(1/9)
            output.append(abandoned_review_reviewid)
            position.append(9)
        elif (dic1[abandoned_review_reviewid] == merged_review_reviewid10):
            acc.append(1)
            score.append(1/10)
            output.append(abandoned_review_reviewid)
            position.append(10)
        else: 
            acc.append(0)
            score.append(0)
            output.append(abandoned_review_reviewid)
            position.append(0)
        count = count +1

#MRR=sum(score) / len(acc)       

position = dict(zip(output, position))

with open("", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in position.items():
       writer.writerow([key, value])
