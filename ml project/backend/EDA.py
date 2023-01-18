import pandas as pd
import numpy as np


# reading indian cities table
df1 = pd.read_csv(r'C:\Users\DEEPAK VERMA\Desktop\ml project\backend\Indian Cities Database.csv')
 
# making a dictnory using upper dataframe
citystate= dict(zip(df1.City, df1.State))



def city(all_data):
    # replacing the nan of city column with the country column where country is not India to make it right
    all_data['city'] = np.where(all_data['country'] != 'India', all_data['country'], all_data['city'])
    # replacing other nan value of city column with the any becuse those jobs are remote so need to mention the city
    all_data.loc[(all_data['workplace_type'] == 'Remote') & (all_data['city'].isnull() == True), 'city'] = 'any'
    # replacing other nan value of city column with delhi where state is delhi or chandigarh
    all_data.loc[(all_data['state'] == 'Delhi') & (all_data['city'].isnull() == True), 'city'] = 'Delhi'
    all_data.loc[(all_data['state'] == 'Chandigarh') & (all_data['city'].isnull() == True), 'city'] = 'Chandigarh'
    # replace others nan with the perticuar string
    all_data.loc[all_data['city'].isnull() == True, 'city'] = 'Location as per your suitability'
    return all_data

def country(all_data):   
    #################### coutry #########################
    # change all the other city value present in country column with the India
    all_data.loc[all_data["country"] != "India", 'country'] = 'India'
    return all_data

def state_find(x):
        for st in citystate.keys():
            if st in x:
                x = citystate[st]
                break
        return x

def state(all_data):
    # defining a function which will change city name present in the state column with the right state name
    # replacing the nan of state column with the city column where city is any to make it right
    all_data['state'] = np.where((all_data['city'] == 'any')&(all_data['state'].isnull() == True), all_data['city'], all_data['state'])
    # replacing nan of state with the city name 
    all_data['state'] = np.where(all_data['state'].isnull() == True, all_data['city'], all_data['state'])
    # replacing city present in the state with the state name
    all_data['state'] = all_data["state"].apply(lambda x: state_find(x))
    return all_data

def loc(all_data):
    all_data[['country', 'state', 'city']] = all_data["location"].apply(lambda x: pd.Series(str(x).split(", ")[::-1]))
    all_data = city(all_data)
    all_data = country(all_data)
    all_data = state(all_data)
    return all_data
    
def job(all_data):
    #################### job_title #########################
    # get the job title from all the rows containing "internship in" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index('Internship')-1] if 'Internship' in x else x)
    # get the job title from all the rows containing " at" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index(' at')] if ' at' in x else x)
    # get the job title from all the rows containing "part time" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index('part time')-1] if 'part time' in x else x)
    # get the job title from all the rows containing "," keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index(',')] if ',' in x else x)
    # get the job title from all the rows containing "Payable" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index('Payable')-1] if 'Payable' in x else x)
    # get the job title from all the rows containing "(" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index('(')-1] if '(' in x else x)
    # get the job title from all the rows containing "Ground" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Airport Ground Staff" if 'Ground' in x else x)
    # get the job title from all the rows containing ":" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: x[:x.index(':')] if ':' in x else x)
    # get the job title from all the rows containing "Data Entry" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Data Entry" if 'Data Entry' in x else x)
    # get the job title from all the rows containing "Internet Assessor" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Internet Assessor" if 'Internet Assessor' in x or 'Internet Ads Assessor' in x else x)
    # get the job title from all the rows containing "Customer Support" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Customer Support" if 'Customer Support' in x else x)
    # get the job title from all the rows containing "Sales Executive" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Sales Executive" if 'Sales Executive' in x else x)
    # get the job title from all the rows containing "Lead Engineer" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Lead Engineer" if 'Lead Engineer' in x else x)
    # get the job title from all the rows containing "Process Engineer" keyword
    all_data['job_title'] = all_data['job_title'].apply(lambda x: "Process Engineer" if 'Process Engineer' in x else x)
    return all_data

#defining a function whihc will take string as a input and then return involvement accordingly
def involve(st):
    if 'Full-time' in st:
        return 'Full-time'
    elif 'Part-time' in st:
        return 'Part-time'
    elif 'Internship' in st:
        return 'Internship'
    elif 'Contract'in st:
        return 'Contract'
    else:
        return 'Not-given'
    
def invol(all_data):
    # using the upper define function and getting the right value in the column
    all_data['level'] = all_data['involvement'].apply(lambda x: str(x).split("·")[-1].strip())
    all_data['involvement'] = all_data['involvement'].apply(lambda x: involve(x)) 
    return all_data

def work(all_data):
    # when there is no workplace given i am replacing those null data with the not-given
    all_data['workplace_type'] = all_data['workplace_type'].apply(lambda x: x if x != "" else 'Not-given')
    return all_data

# define a function which will take employee count and return avg 
def find_avg(st):
    try:
        try:
            st = st.replace("+", "").split(" ")[0]
            num1, num2 = map(int, st.replace(',', '').split("-"))
            return int((num1+num2)/2)
        except:
            return int(st.replace(',', ''))
    except:
        return 'Not-given'
    
def emp(all_data):
    # using upper define function to find the average employee
    all_data['employee_count'] = all_data['employee_count'].apply(lambda x: find_avg(x))
    return all_data  

def fol(all_data):
    # this line of code will help us to find the followers_count from the scraped string
    all_data['followers_count'] = all_data['followers_count'].apply(lambda x: pd.Series(str(x).replace(" followers", '').replace(",", '')))
    # deal with it
    all_data['followers_count'] = all_data['followers_count'].apply(lambda x: x if x != "" else 'Not-given')
    return all_data

def industry(all_data):
    # this line of code will extract industry from the string of industry
    all_data['industry'] = all_data['industry'].apply(lambda x: " ".join(x.replace("employees", '').replace("on LinkedIn", '').split()[:-2])) 
    return all_data

def app(all_data):
    # replacing string present in the applicants1 column
    all_data['applicants_1'] = all_data['applicants_1'].apply(lambda x:x.replace("applicants", '').replace("applicant", '').replace("Over", '').replace(",", '').strip())
    # replacing applicants_1 coulumn's null values with the posted_date values
    all_data['applicants_1'] = np.where(all_data['applicants_1'] == '', all_data['posted_date'], all_data['applicants_1'])
    # converting all values of applicants_1 column to 0 those are in hours
    all_data['applicants_1'] = all_data['applicants_1'].apply(lambda x: 0 if 'hours' in x else x)
    # replacing unnecessery value from applicants_2
    all_data['applicants_2'] = all_data['applicants_2'].apply(lambda x:x.replace('See how you compare to ', '').replace(' applicants. Try Premium for free', '').replace(',', '').strip())
    # converting both the columns into numeric and replace other string value into nan
    all_data['applicants_2'] = pd.to_numeric(all_data['applicants_2'], errors = 'coerce')
    all_data['applicants_1'] = pd.to_numeric(all_data['applicants_1'], errors = 'coerce')
    # replacing applicants_1 nan value with the applicant_2
    all_data['applicants_1'] = np.where(all_data['applicants_1'].isnull() == True, all_data['applicants_2'], all_data['applicants_1'])
    # creating new column name applicants and populalte it with the values 
    all_data['applicants'] = all_data['applicants_1'].fillna('Not-given')
    return all_data

def eda_full(dataframe):
    # removing all the jobs those are not active now 
    all_data = dataframe[dataframe['active'] == '']
    all_data =   loc(all_data)
    all_data =   job(all_data)
    all_data = invol(all_data)
    all_data =  work(all_data)
    all_data =   emp(all_data)
    all_data =   fol(all_data)
    all_data = industry(all_data)
    all_data =  app(all_data)
    return all_data

