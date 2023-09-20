# Importing the pandas library to work with DataFrames
import pandas as pd

# Reading a CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\DEEPAK VERMA\Desktop\ml project\final_all_data.csv')

# Function to retrieve statistics and information about jobs related to a specific skill
def skill_job(skills, df):
    try:
        # Filtering the DataFrame to find jobs containing the specified skill
        data = df[df['skills'].str.lower().str.contains(skills.lower())]
        
        # Finding the most common job level, industry, and job class related to the skill
        Most_common_level = data.groupby(['level']).size()[:1].reset_index()['level'][0]
        Most_common_industry = data.groupby(['industry']).size()[:1].reset_index()['industry'][0]
        Most_common_comp_class = data.groupby(['job_class']).size()[:1].reset_index()['job_class'][0]
        
        # Calculating the total number of jobs related to the skill
        Total_Number_jobs = len(data)
        
        # Returning the results as a dictionary
        return {'mcel': Most_common_level, 'mci': Most_common_industry, 'mccc': Most_common_comp_class, 'tn': Total_Number_jobs}
    except:
        # Handling exceptions if no jobs are found for the given skill
        return {'placeholder': 'No! Job opening for the given skill'}
    
# Function to retrieve details of jobs related to a specific skill
def skill_details(skills, df):
    # Filtering the DataFrame to find jobs containing the specified skill
    data = df[df['skills'].str.lower().str.contains(skills.lower())]
    
    # Converting the filtered data to a list of dictionaries (job details)
    jobs = data.T.to_dict().values()
    
    # Returning the list of job details
    return jobs

# Function to retrieve statistics and information about jobs related to a specific job title
def job_job(job_title, df):
    try:
        # Filtering the DataFrame to find jobs containing the specified job title
        data = df[df['job_title'].str.lower().str.contains(job_title.lower())]
        
        # Finding the most common job level, industry, and job class related to the job title
        Most_common_level = data.groupby(['level']).size()[:1].reset_index()['level'][0]
        Most_common_industry = data.groupby(['industry']).size()[:1].reset_index()['industry'][0]
        Most_common_comp_class = data.groupby(['job_class']).size()[:1].reset_index()['job_class'][0]
        
        # Calculating the total number of jobs related to the job title
        Total_Number_jobs = len(data)
        
        # Returning the results as a dictionary
        return {'mcel': Most_common_level, 'mci': Most_common_industry, 'mccc': Most_common_comp_class, 'tn': Total_Number_jobs}
    except:
        # Handling exceptions if no jobs are found for the given job title
        return {'placeholder': 'No! Job opening for the given Job title'}

# Function to retrieve details of jobs related to a specific job title
def job_details(job_title, df):
    # Filtering the DataFrame to find jobs containing the specified job title
    data = df[df['job_title'].str.lower().str.contains(job_title.lower())]
    
    # Converting the filtered data to a list of dictionaries (job details)
    jobs = data.T.to_dict().values()
    
    # Returning the list of job details
    return jobs

