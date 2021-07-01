import json
from rouge import Rouge

# Load some sentences
with open('TextRank_MAJ.json') as f:
  data = json.load(f)

hyps, refs = map(list, zip(*[[d['hyp'], d['ref']] for d in data]))
rouge = Rouge()
#scores = rouge.get_scores(hyps, refs)
scores = rouge.get_scores(hyps, refs, avg=True)
print(scores)
