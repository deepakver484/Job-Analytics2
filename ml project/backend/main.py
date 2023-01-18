import scraper
import pandas as pd
import EDA
import skills
import  agent_class

##-------------------------- Scrapping data  ---------------------------------------##
# scraper.login('sintcaddesigning@gmail.com','Note7@484')


# all_links =  scraper.get_links(1)

# all_data = pd.DataFrame(scraper.get_job_info(all_links))


all_data = pd.read_json(r'C:\Users\DEEPAK VERMA\Desktop\ml project\backend\all_data.json')
##-------------------------- Performing EDA ---------------------------------------##

all_data = EDA.eda_full(all_data)

##--------------------------Adding Skills -----------------------------------------##

all_data = skills.skills_apply(all_data)

##-------------------------- Adding job_class -------------------------------------##

all_data = agent_class.job_class(all_data)

##----------------------- dropping unnecessary column -----------------------------##

all_data.drop(columns = ['applicants_1', 'applicants_2', 'active', 'location', 'Clean_skills', 'job_description'], inplace = True)

##------------------------- save final data into csv ------------------------------##

all_data.to_csv('C:/Users/DEEPAK VERMA/Desktop/ml project/final_all_data.csv')
    
