import pandas as pd
df = pd.read_csv(r'C:\Users\DEEPAK VERMA\Desktop\ml project\final_all_data.csv')

def skill_job(skills, df):
    try:
        data = df[df['skills'].str.lower().str.contains(skills.lower())]
        Most_common_level = data.groupby(['level']).size()[:1].reset_index()['level'][0]
        Most_common_industry = data.groupby(['industry']).size()[:1].reset_index()['industry'][0]
        Most_common_comp_class = data.groupby(['job_class']).size()[:1].reset_index()['job_class'][0]
        Total_Number_jobs = len(data)
        return {'mcel': Most_common_level, 'mci': Most_common_industry, 'mccc': Most_common_comp_class, 'tn': Total_Number_jobs}
    except:
        return {'placeholder': 'No! Job opening for the given skill'}
    
def skill_details(skills, df):
    data = df[df['skills'].str.lower().str.contains(skills.lower())]
    jobs = data.T.to_dict().values()
    return jobs


def job_job(job_title, df):
    try:
        data = df[df['job_title'].str.lower().str.contains(job_title.lower())]
        Most_common_level = data.groupby(['level']).size()[:1].reset_index()['level'][0]
        Most_common_industry = data.groupby(['industry']).size()[:1].reset_index()['industry'][0]
        Most_common_comp_class = data.groupby(['job_class']).size()[:1].reset_index()['job_class'][0]
        Total_Number_jobs = len(data)
        return {'mcel': Most_common_level, 'mci': Most_common_industry, 'mccc': Most_common_comp_class, 'tn': Total_Number_jobs}
    except:
        return {'placeholder': 'No! Job opening for the given Job title'}
    
def job_details(job_title, df):
    data = df[df['job_title'].str.lower().str.contains(job_title.lower())]
    jobs = data.T.to_dict().values()
    return jobs

