import scraper
import pandas as pd
import EDA
import skills
import  agent_class

##-------------------------- Scrapping data  ---------------------------------------##
# scraper.login('username@gmail.com','password7@')
# print('login done')

# all_links =  scraper.get_links(40)
# print('links scraped done')

# all_data = pd.DataFrame(scraper.get_job_info(all_links))
# print('data scraped done')

# all_data.to_json('all_data.json')

all_data = pd.read_json(r'C:\Users\DEEPAK VERMA\Desktop\ml project\all_data.json')
##-------------------------- Performing EDA ---------------------------------------##

all_data = EDA.eda_full(all_data)
print('EDA part done')

##--------------------------Adding Skills -----------------------------------------##

all_data = skills.skills_apply(all_data)
print('Skills Added done')

##-------------------------- Adding job_class -------------------------------------##

all_data = agent_class.job_class(all_data)
print('agent part done')

##----------------------- dropping unnecessary column -----------------------------##

all_data.drop(columns = ['applicants_1', 'applicants_2', 'active', 'location', 'Clean_skills', 'job_description'], inplace = True)
print('dropping done')

##------------------------- save final data into csv ------------------------------##
# 
all_data.to_csv('C:/Users/DEEPAK VERMA/Desktop/ml project/final_all_data.csv')

