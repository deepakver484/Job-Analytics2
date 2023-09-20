import spacy
#nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#warning
import warnings 
warnings.filterwarnings('ignore')

# here we are loading en_Core_web_lg from spacy and providing the path of the jsonal file
nlp = spacy.load("en_core_web_lg")
skill_pattern_path = r"C:\Users\DEEPAK VERMA\Desktop\ml project\backend\skills_patterns.jsonl"

# building one pipe line called entity_rular and passing the jsonal file to i
ruler = nlp.add_pipe("entity_ruler")
ruler.from_disk(skill_pattern_path)

# Below given function will extract the skills from the job description with the help of nlp
def get_skills(text):
    doc = nlp(text)
    myset = []
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            subset.append(ent.text)
    myset.append(subset)
    return subset

# Here we remove the duplicates skills from the skills
def unique_skills(x):
    return ", ".join(list(set(x)))

# Here We are updating the jd and removine the stopwords andn memmitaize word using update_jb function
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

# In this function we will call above given all function to get our desired result
def skills_apply(data):
    data["Clean_skills"] = data['job_description'].apply(update_jd)
    data["skills"] = data["Clean_skills"].str.lower().apply(get_skills)
    data["skills"] = data["skills"].apply(unique_skills)
    data[data['skills'] == ''] = 'Not-found'
    return data


