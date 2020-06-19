
import csv;

def path2List(fileString):
	return fileString.split("/");

def LCP(f1,f2):
	f1 = path2List(f1);
	f2 = path2List(f2);
	common_path = 0;
	min_length = min(len(f1),len(f2));
	for i in range(min_length):
		if f1[i] == f2[i]:
			common_path += 1;
		else:
			break;
	return common_path;

def LCSuff(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	common_path = 0
	r = list(range(min(len(f1),len(f2))))
	r.reverse()
	for i in r:
		if f1[i] == f2[i]:
			common_path += 1
		else:
			break
	return common_path
    
def LCSubstr(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	common_path = 0
	if len( set(f1) & set(f2)) > 0:
		mat = [[0 for x in range(len(f2)+1)] for x in range(len(f1)+1)]
		for i in range(len(f1)+1):
			for j in range(len(f2)+1):
				if i == 0 or j == 0:
					mat[i][j] = 0
				elif f1[i-1] == f2[j-1]:
					mat[i][j] = mat[i-1][j-1] + 1
					common_path = max(common_path,mat[i][j])
				else:
					mat[i][j] = 0
	return common_path

def filePathSimilarity(fn,fp):
    return LCP(fn,fp) / max(len(fn),len(fp));

def LCSubseq(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	if len( set(f1) & set(f2)) > 0:
		L = [[0 for x in range(len(f2)+1)] for x in range(len(f1)+1)]
		for i in range(len(f1)+1):
			for j in range(len(f2)+1):
				if i == 0 or j == 0:
					L[i][j] = 0
				elif f1[i-1] == f2[j-1]:
					L[i][j] = L[i-1][j-1] + 1
				else:
					L[i][j] = max(L[i-1][j], L[i][j-1])
		common_path = L[len(f1)][len(f2)]
	else:
		common_path = 0
	return common_path

def sort_by_value(d):
    items = d.items();
    backitem = [[v[1],v[0]] for v in items];
    backitem.sort(reverse = True);
    return [[backitem[i][1],backitem[i][0]] for i in range(0,len(backitem))];

test = list(csv.reader(open('')));
train = list(csv.reader(open('')));
checklist = list(csv.reader(open('')))
test.pop(0);
train.pop(0)

dict_a = {};
dict_m = {};

dict_result = {};

for row_a in test:
    if row_a[0] not in dict_a:
        dict_a[row_a[0]] = [];
    dict_a[row_a[0]].append(row_a[1]);

for row_m in train:
    if row_m[0] not in dict_m:
        dict_m[row_m[0]] = [];
    dict_m[row_m[0]].append(row_m[1]);

for key,value in dict_a.items():
    
    score_m = {};

    for key_m,value_m in dict_m.items():
        sc = 0;
        
        for file in value:
            for file_m in value_m:
                sc = sc + filePathSimilarity(file,file_m);

        sc = sc / (len(value) * len(value_m));
        score_m[key_m] = sc;
    
    result = sort_by_value(score_m);
    dict_result[key] = [];
    for i in range(0,10):
        dict_result[key].append(result[i][0]);
count = []  

hit_information = []
count = []
recall = {}
score = []
hit = []
position = []
for row in checklist:
    if row[0] in dict_result:
        if row[1] in dict_result[row[0]][0]:
            score.append(1)
            position.append(1)
            hit.append(row[0])
            count.append(1)
        elif row[1] in dict_result[row[0]][1]:
             score.append(1/2)
             position.append(2)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][2]:
             score.append(1/3)
             position.append(3)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][3]:
             score.append(1/4)
             position.append(4)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][4]:
             score.append(1/5)
             position.append(5)
             hit.append(row[0]) 
             count.append(1)
        elif row[1] in dict_result[row[0]][5]:
             score.append(1/6)
             position.append(6)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][6]:
             score.append(1/7)
             position.append(7)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][7]:
             score.append(1/8)
             position.append(8)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][8]:
             score.append(1/9)
             position.append(9)
             hit.append(row[0])
             count.append(1)
        elif row[1] in dict_result[row[0]][9]:
             score.append(1/10)
             position.append(10)
             hit.append(row[0])
             count.append(1)
        else:
            score.append(0)
            position.append(0)
            hit.append(row[0])
            count.append(0)

recall = dict(zip(hit, position))
print (sum(count))

import collections

counter=collections.Counter(position)
print(counter)

with open("", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in recall.items():
       writer.writerow([key, value])
