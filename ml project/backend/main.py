# Importing necessary modules and functions
import scraper
import pandas as pd
import EDA
import skills
import agent_class

##-------------------------- Scrapping data  ---------------------------------------##

# Uncomment and use the following lines to log in and scrape data if needed
# scraper.login('username@gmail.com','password7@')
# print('login done')

# Scraping job links (40 in this case)
# all_links =  scraper.get_links(40)
# print('links scraped done')

# Scraping job information using the collected links
# all_data = pd.DataFrame(scraper.get_job_info(all_links))
# print('data scraped done')

# Saving the scraped data as a JSON file
# all_data.to_json('all_data.json')

# Reading the previously scraped data from a JSON file
all_data = pd.read_json(r'C:\Users\DEEPAK VERMA\Desktop\ml project\all_data.json')

##-------------------------- Performing EDA ---------------------------------------##

# Applying exploratory data analysis (EDA) to the scraped data
all_data = EDA.eda_full(all_data)
print('EDA part done')

##-------------------------- Adding Skills -----------------------------------------##

# Applying a function to add skills-related information to the data
all_data = skills.skills_apply(all_data)
print('Skills Added done')

##-------------------------- Adding job_class -------------------------------------##

# Applying a function to classify jobs into classes
all_data = agent_class.job_class(all_data)
print('agent part done')

##----------------------- Dropping unnecessary columns -----------------------------##

# Removing unnecessary columns from the data
all_data.drop(columns=['applicants_1', 'applicants_2', 'active', 'location', 'Clean_skills', 'job_description'], inplace=True)
print('dropping done')

##------------------------- Save final data into CSV ------------------------------##

# Saving the final processed data into a CSV file
all_data.to_csv('C:/Users/DEEPAK VERMA/Desktop/ml project/final_all_data.csv')
