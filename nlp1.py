import spacy
import csv
from spacy.matcher import PhraseMatcher
# Import the Matcher

file = open(r'C:\Users\Shela\Downloads\All_Indian_Trains.csv')
csvreader = csv.reader(file)
header = next(csvreader)
starts = []
for i in csvreader:
    starts.append(i[3])
# print(starts)
# Load a pipeline and create the nlp object
def NLP_SQL(text):

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    matcher = PhraseMatcher(nlp.vocab)
    patterns = list(set((nlp.pipe(starts))))

    matcher.add("Cities", patterns)



    matches = matcher(doc)
    matched_span = [doc[start:end] for match_id, start, end in matches]
    starts_at = matched_span[0]
    ends_at = matched_span[-1]

    sql = "SELECT * FROM TRAINS WHERE START = '{}' AND ENDS = '{}'".format(starts_at,ends_at)
    print(sql)
    return sql








# NLP_SQL("List trains available from New Delhi to Aurangabad.")