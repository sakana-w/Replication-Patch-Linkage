from requests.auth import HTTPDigestAuth
from pygerrit.rest import GerritRestAPI
import csv

auth = None
rest = GerritRestAPI(url='https://android-review.googlesource.com/', auth=auth)
with open('', 'r') as csvfile:
    reviews=[]
    read = csv.reader (csvfile, delimiter=',')
    for row in read:
        reviews.append(row[0])
            
link=[]
count = 1 
for review in reviews:
    try:
            review_info={}
            review_info["ind"]=count
            review_info["link_id"]=review
            change_owner = rest.get("/changes/"+str(review)+"/")
            if change_owner is not None:
                 owner = change_owner["owner"]["_account_id"]
            else:
                 owner = "NA"
            review_info["owner"]=owner
            change_subject = rest.get("/changes/"+str(review)+"/revisions/1/commit")
            if change_subject is not None:
                 subject = change_subject["subject"]
                 message = change_subject["message"]
            else:
                 subject = "NA"
                 message = "NA"
            review_info["subject"]=subject
            review_info["message"]=message
            filelist = rest.get("/changes/"+str(review)+"/revisions/1/files/")

            file =[]
            
            for key in filelist:
                if key is not None:
                    file.append(key)
                else:
                    file.append("NA")

            review_info["file"] = file

            link.append(review_info)
            
    except Exception:   
	    review_info["ind"]=count
	    review_info["owner"]="NA"
	    review_info["message"]="NA"
	    review_info["subject"]="NA"
	    review_info["link_id"]="NA"
	    review_info["file"]="NA"
	    link.append(review_info)
	    continue

    count = count + 1
            

csv_columns = ['ind','owner','message','subject','link_id','file']

csv_file = ""
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for li in link:
            writer.writerow(li)
except IOError:
    print("I/O error") 
             
