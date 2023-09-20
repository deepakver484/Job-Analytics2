# Job-Analytics2
In today's dynamic and competitive job market, staying informed and making informed career decisions is crucial. Project Job-Analytics is a cutting-edge initiative designed to empower job seekers, professionals, and employers with comprehensive insights into the ever-evolving world of employment. This innovative project harnesses the power of data analytics, machine learning, and real-time job market data to provide users with valuable information and trends that can shape their career trajectories and hiring strategies.


## OBJECTIVE
The primary objective of this project is to gather data from LinkedIn profiles and leverage data analytics techniques to generate meaningful insights. Additionally, we aim to create a user-friendly web page that serves as a centralized platform for users to access and explore these insights seamlessly. This project will enable users to extract valuable information from LinkedIn profiles efficiently and provide a convenient interface for accessing these insights, enhancing their overall user experience.


## TOOLS USED
<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/deepakver484/assets/blob/main/icons8-microsoft-sql-server.svg" title="SqlServer" alt="SqlServer" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/flask/flask-original-wordmark.svg" title="Flask" alt="Flask" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original-wordmark.svg" title="Pandas" alt="Pandas" width="40" height="40"/>&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"  title="Sklearn" alt="Sklearn" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" title="SqlAlchemy" alt="SqlAlchemy" width="40" height="40"/>&nbsp;
  <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/>
  <img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original-wordmark.svg"  title="Vscode" alt="Vscode" width="40" height="40"/>&nbsp;
  <img src="https://github.com/deepakver484/assets/blob/main/icons8-tableau-software.svg"  title="Tableau" alt="Tableau" width="40" height="40"/>&nbsp;
  <img src="https://github.com/deepakver484/assets/blob/main/machine-learning-01-svgrepo-com.svg" title="MachineLearning" alt="MachineLearning" width="50" height="50"/>&nbsp;
  <img src="https://github.com/deepakver484/assets/blob/main/icons8-excel.svg"  title="Excel" alt="Excel" width="50" height="50"/>&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Matplotlib" width="50" height="50"/>
<!--   <img src="https://github.com/deepakver484/assets/blob/main/icons8-excel.svg"  title="Excel" alt="Excel" width="50" height="50"/>&nbsp; -->
  <div>


##  <img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="48" height="48"> **User's Manual**
| **Files/Folder** | **Description** |
| ---------------- | --------------- |
| **[AppInfo](https://github.com/deepakver484/Job-Analytics2/tree/main/ml%20project)** | This folder containing all the files of web app |
| **[Dashboard & PPT](https://github.com/deepakver484/Job-Analytics2/tree/main/ml%20project/Dashboard%20%26%20PPT)** | This folder contains Dashboard and PPT for the Project |
| **[Data](https://github.com/deepakver484/Job-Analytics2/tree/main/ml%20project/Data)** | This folder contains all the data files used in the project |
| **[Backend](https://github.com/deepakver484/Job-Analytics2/tree/main/ml%20project/backend)** | This folder contains all the files related to backend file (scraper, machine learning model, EDA files) |
| **[Static](https://github.com/deepakver484/Job-Analytics2/tree/main/ml%20project/static)** | This folder contains all the static files used in the web app |
| **[Templates](https://github.com/deepakver484/Job-Analytics2/tree/main/ml%20project/templates)** | this folder contains all the html files used in the web app |

# Project Workflow :
<div>
  <img src="https://github.com/deepakver484/assets/blob/main/Project%20Flow.jpg"  title="Flow" alt="Flow" width="100%" />&nbsp;
 
</div>
<details>
  <summary><a href="https://github.com/deepakver484/Job-Analytics2/blob/main/ml%20project/backend/scraper.py"><strong>Scraper.py</strong></a></summary>

**login(username, passward) :-**

The provided function, login, automates the process of logging in to the LinkedIn website using Selenium WebDriver in Python. It opens a Chrome browser, navigates to the LinkedIn Jobs page, enters the provided username and password, and clicks the login button. After a successful login, it prints a confirmation message with the username.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/fe6054da-0640-49c2-a235-e2e5232a087b)


**page_link()**

This function collects and returns a list of job links by searching through a list of job listings on a web page. It identifies the job links by locating anchor tags (<a>) within the job listings, extracts the href attribute containing the link, and appends these links to a list. Additionally, it scrolls down the page to load additional job listings and introduces brief delays between each action to ensure smooth execution. Finally, it returns the list of job links found on the page.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/d2cec544-ca0c-4ddc-b7c1-5effce911257)


**get_links(page_number)**

This function takes an input page_number and collects links from a sequence of pages, starting from the first page and continuing through the specified number of pages. It iterates through these pages by clicking on page number buttons, waiting for page content to load, and then aggregating the links obtained from each page using the page_link function. It prints a message indicating the progress of link extraction on each page. Finally, it returns a consolidated list of links from all the visited pages.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/dcc6d289-88f6-40fd-8e1d-8b81e637935e)


**job_info(link)**

This function takes a link to a job listing page, navigates to that page using a WebDriver, and then scrapes valuable information. It starts by clicking a "See More" button to expand the job listing content. It then attempts to extract details such as the job's location, title, company name, industry, employee count, followers count, job involvement, and more. Additionally, it captures information about the job's description, workplace type, application status, and posting date.
Finally, this function compiles all the extracted information into a dictionary format and returns it. This dictionary includes key-value pairs representing various job-related attributes, making it easy to organize and utilize this data for further analysis or processing.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/0d0f0eaa-03f6-4ecb-9451-f8016d7fdd6b)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/a40d7a1e-f1c0-4ae7-a670-ddf3d783b6ba)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/58c63767-5bd5-4d9e-bfce-e90da78f49cf)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/9035342c-5f0f-4972-863e-f36f317b5935)

**get_job_info(link_list)**

This function takes a list of job listing links, link_list, as input. It then iterates through each link, using the job_info function to extract detailed information about each job listing. The extracted information is organized into dictionaries, and these dictionaries are appended to a data list. Each dictionary contains various attributes related to the job, such as company name, job title, location, industry, and more.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/1f5da080-ba57-462f-b6c3-150a7a40ebd2)
</details>
<details>
  <summary><a href="https://github.com/deepakver484/Job-Analytics2/blob/main/ml%20project/backend/EDA.py"><strong>EDA.py</strong></a></summary>

**city(all_data)** :- This function clean the city column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/2a9b7e1b-2644-4358-bebb-274db19e4888)


**country(all_data)** :- This function clean the country column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/5b71cc53-bffb-4d6d-a8be-f4fd9adca009)


**state_find(x)** :- this function will take city as input and return state of that city.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/96241812-25c2-4080-9164-426632686371)


**state(all_data)** :- This function will clean the state column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/b04e2aec-5389-4dd9-a613-1157bc5776d3)


**loc(all_data)** :- This function will use above three function and convert one location column into different column and clean as well.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/82f1e92e-6bb7-49cd-9e5c-fdcf64143924)


**job(all_data)** :- This function will clean the job column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/a25466ee-c833-482e-a7a3-a32362f02091)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/172999ee-70c7-4cd8-b06c-6cfc95ddd8bc)


**involve(st) & invol(all_data)** :- Both function will work together to clean the Involve column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/cb33a121-e227-4be6-af89-523ed045c06f)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/f7f296df-cc75-494b-867b-31582cc29587)



**work(all_data)** :- This function will clean the work column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/8245adeb-2178-4374-877c-e395e94bed02)


**find_avg(st) & emp(all_data)** Both function will work together to clean the employee column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/2fc58932-dc7a-4396-a2fb-4981b4aba3fd)


**fol(all_data)** :- This function will clean the follower count column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/b3c38784-9e6f-45e0-9403-1c86a29de67a)


**industry(all_data)** :- This function will clean the indusctry column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/d31eeb3a-77eb-4881-abbd-3c869e9e98f8)


**app(all_data)** :- This function will clean the applicants column of the data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/1df81be9-1494-4228-b919-1c869694947a)


**eda_full(dataframe)** :- This function will take the raw data and use all the above function of the eda and return cleaned data.
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/ce76c3b6-3736-4607-82a0-a98bedaf7a72)

</details>

<details>
  <summary><a href="https://github.com/deepakver484/Job-Analytics2/edit/main/ml%20project/backend/skills.py"><strong>Skills.py</strong></a></summary>

  ![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/08a20a74-7ee1-48cd-8c47-3d9972f72a9b)

</details>

## Insights
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/5c17566a-c25e-46a4-94b7-775b1f89df44)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/28991083-d842-46b2-823b-4ec8cc818566)
![image](https://github.com/deepakver484/Job-Analytics2/assets/83640385/d28f6903-69d7-40e0-a082-e04e32ca60bd)













