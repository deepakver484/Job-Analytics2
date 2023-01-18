import spacy
#nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#warning
import warnings 
warnings.filterwarnings('ignore')

nlp = spacy.load("en_core_web_lg")
skill_pattern_path = r"C:\Users\DEEPAK VERMA\Desktop\ml project\backend\skills_patterns.jsonl"

ruler = nlp.add_pipe("entity_ruler")
ruler.from_disk(skill_pattern_path)

def get_skills(text):
    doc = nlp(text)
    myset = []
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            subset.append(ent.text)
    myset.append(subset)
    return subset


def unique_skills(x):
    return ", ".join(list(set(x)))

def update_jd(data):
    review = re.sub(
            '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"', " ", data)
    review = review.lower()
    review = review.split()
    lm = WordNetLemmatizer()
    review = [ lm.lemmatize(word)
            for word in review
            if not word in set(stopwords.words("english"))
            ]
    review = " ".join(review)
    return review
    
def skills_apply(data):
    data["Clean_skills"] = data['job_description'].apply(update_jd)
    data["skills"] = data["Clean_skills"].str.lower().apply(get_skills)
    data["skills"] = data["skills"].apply(unique_skills)
    return data

def log_skills():
    log_text = f'''skills extracted successfully done........
    ------------------------------------------------
    '''
    return log_text
    
