# PeerEval

DATA INFO
* All Data/files needed are in the data folder.
* “pre.py”- for preprocessing
* 'sentence.pickle', 'fileid.pickle', 'tags.pickle' (can be generated by RUNNING “create_data.py”) also is already available in data folder.
* dev,test,train data for task-1,2,3,4 are already available(can also be generated by RUNNING “CREATEjason” after adjusting appropriate layer variable in code)
* IAA data is inter-annotation data by the different reviewers


TO RUN
TASK-1 & TASK-2 & TASK-3 & TASK-4


TFIDF,BOW,TFIDF+CONTEXT,USE
STEP-1: Include Files 'pre.py','sentence.pickle','tags.pickle','fileid.pickle'
STEP-2: In code SET the layer variable, layer=0(for task-1), layer=1(for task-2) and so on
STEP:3 RUN


DOMAIN SPECIFIC
Follow step-1 and step-3 above


BERT,BERT+CRF
STEP-1: Add dev,test,train jsonl data(can be created using CreateJason or is also available) for appropriate layer in “/content/sequential_sentence_classification/data/CSAbstruct”
STEP-2:  In “train.sh”, ADJUST the parameters
STEP-3:  Install the requirements using: pip install -r requirements.txt
STEP-4:  RUN: scripts/train.sh tmp_output_dir

TASK-3(Summarisation)
MAJ tag as GOLD STANDARD( For unsupervised & neural baselines)
STEP-1: Include Files 'pre.py','sentence.pickle','tags.pickle','fileid.pickle'
STEP-2:  RUN


META data as GOLD STANDARD( For unsupervised & neural baselines)
STEP-1: Include File dic.pickle
STEP-2:  RUN


Note: A json file would have been created[‘ref’:gold standard review summary, ‘hyp’: automatically generated summary]


CALCULATION OF ROGUE SCORE
STEP-1: Include the json file created by above code
STEP-2: RUN

