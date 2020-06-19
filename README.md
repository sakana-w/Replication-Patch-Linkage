# Automatic Patch Linkage Detection in Code Review UsingTextual Content and File Location Features

#### Dong Wang, Raula Gaikovina Kula, Takashi Ishio and Kenichi Matsumoto
#### *Nara Institute of Science and Technology, Japan*

## Abstract
Context:Contemporary code review tools are a popular choice for software quality assurance.Using these tools, reviewers are able to post alinkagebetween two patches during a reviewdiscussion. Large review teams that use a review-then-commit model risk being unaware ofthese linkages.

Objective:Our objective is to first explore how patch linkage impacts the review process. Wethen propose and evaluate models to detect patch linkage.  

Method:First, we carry out an exploratory study on three open source projects to conduct linkageimpact analysis using 942 manually classified linkages. Second, we propose two techniques us-ing textual and file location similarity to build detection models and evaluate their performance.

Results:For the exploratory study, we find evidence to support early patch linkage detection.We show that a patch with the Alternative Solution linkage (i.e., patches that implement simi-lar functionality) undergoes quicker reviews and avoids additional revisions when compared toother linkage types. Results from the experiments show promising recall rates, especially for theAlternative Solution linkage (from 44% to 79%), but precision has room for improvement (64%).

Conclusion:Our study confirms that patch linkage detection is promising, with inevitable im-provements as the practice of posting links becomes more prevalent. From our lessons learnt,this paper lays the groundwork for future research on how to increase patch awareness, whichmay facilitate efficient reviews.


## Replication Description
The repository includes (a) 942 manually coded patch linkage with variousproperties (\Exploratory Study) and (b) experiment datasets and scripts that reproduce our detection model (\Empirical Evaluation, \Script).

For each folder, it includes text file to describe the details of each file.

Due to the limited size of raw data, it can be downloaded here: [Dropbox](https://www.dropbox.com/sh/o19sdx9p7t985pj/AAAzoWHO6eyWMNsk6tw5rhJua?dl=0) including the whole sql data for AOSP, OpenStack, and Qt.

## Acknowledge
This work is supported by Japanese Society for the Promotion of Science (JSPS) KAKENHI Grant Numbers18H04094, 20K19774 and 17H00731.
