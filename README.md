# Automatic Patch Linkage Detection in Code Review Using Textual Content and File Location Features

#### Dong Wang, Raula Gaikovina Kula, Takashi Ishio and Kenichi Matsumoto
#### *Nara Institute of Science and Technology, Japan*

## Abstract
Context: Contemporary code review tools are a popular choice for software quality assurance. Using these tools, reviewers are able to post a \textit{linkage} between two patches during a review discussion. Large development teams that use a review-then-commit model risk being unaware of these linkages.

Objective: Our objective is to first explore how patch linkage impacts the review process. We then propose and evaluate models that detect patch linkage based on realistic time intervals.

Method: First, we carry out an exploratory study on three open source projects to conduct linkage impact analysis using 942 manually classified linkages. 
Second, we propose two techniques using textual and file location similarity to build detection models and evaluate their performance.

Results: The study provides evidence that the latency of the linkage notification exists. We show that a patch with the Alternative Solution linkage (i.e., patches that implement similar functionality) undergoes a quicker review and avoids additional revisions when compared to other linkage types after the team has been notified. In terms of our models, results from the detection model experiments show promising recall rates, especially for the Alternative Solution linkage (from 32\% to 95\%), but precision has room for improvement.

Conclusion:Patch linkage detection is promising, with likely improvements if the practice of posting linkages becomes more prevalent. From our implications, this paper lays the groundwork for future research on how to increase patch linkage awareness to facilitate efficient reviews.

## Replication Description
The repository includes (a) 942 manually coded patch linkage with various properties (\Exploratory Study) and (b) experiment datasets and scripts that reproduce our detection model (\Empirical Evaluation, \Script).

For each folder, it includes text file to describe the details of each file.

Due to the limited size of raw data, it can be downloaded here: [Dropbox](https://www.dropbox.com/sh/o19sdx9p7t985pj/AAAzoWHO6eyWMNsk6tw5rhJua?dl=0) including the whole sql data for AOSP, OpenStack, and Qt.

## Acknowledge
This work is supported by Japanese Society for the Promotion of Science (JSPS) KAKENHI Grant Numbers18H04094, 20K19774 and 17H00731.
