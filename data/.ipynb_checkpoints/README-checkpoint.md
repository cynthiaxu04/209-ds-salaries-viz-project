# Drop all datasets here

### ds_salaries.csv (data from 2020 - 2022)
URL: https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries <br>

What's inside dataset<br>
<p>work_year<br>
The year during which the salary was paid. There are two types of work year values:<br>
1. 2020 - Year with a definitive amount from the past
2. 2021e - Year with an estimated amount (e.g. current year)

experience_level<br>
The experience level in the job during the year with the following possible values:<br>
1. EN - Entry-level / Junior
2. MI - Mid-level / Intermediate
3. SE - Senior-level / Expert
4. EX - Executive-level / Director

employment_type<br>
The type of employement for the role:<br>
1. PT - Part-time
2. FT - Full-time
3. CT - Contract
4. FL - Freelance

job_title<br>
The role worked in during the year. <br>
salary<br>
The total gross salary amount paid.<br>

salary_currency<br>
The currency of the salary paid as an ISO 4217 currency code.<br>

salary_in_usd<br>
The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com).<br>

employee_residence<br>
Employee's primary country of residence in during the work year as an ISO 3166 country code.<br>

remote_ratio<br>
The overall amount of work done remotely, possible values are as follows:<br>
1. 0 - No remote work (less than 20%)
2. 50 - Partially remote
3. 100 - Fully remote (more than 80%)

company_location<br>
The country of the employer's main office or contracting branch as an ISO 3166 country code.

company_size<br>
The average number of people that worked for the company during the year:
1. S - less than 50 employees (small)
2. M - 50 to 250 employees (medium)
3. L - more than 250 employees (large)

Dataset Source - ai-jobs.net Salaries

### Data Science Salary 2021 to 2023.csv
URL: https://www.kaggle.com/datasets/harishkumardatalab/data-science-salary-2021-to-2023

Data Fields:

- work_year: Representing the specific year of salary data collection.
- Experience_level: The level of work experience of the employees, categorized as EN (Entry-Level), EX (Experienced), MI (Mid-Level), SE (Senior).
- Employment_type: The type of employment, labelled as FT (Full-Time), CT (Contractor), FL (Freelancer), PT (Part-Time).
- Job_title: The job titles of the employees, such as "Applied Scientist", "Data Quality Analyst"
, etc.
- Salary: The salary figures in their respective currency formats.
- Salary_currency: The currency code representing the salary.
- Salary_in_usd: The converted salary figures in USD for uniform comparison.
- Company_location: The location of the companies, specified as country codes (e.g., "US" for the United States and "NG" for Nigeria).
- Company_size: The size of the companies, classified as "L" (Large), "M" (Medium), and "S" (Small).

### Data Science Jobs Salaries.csv (only contains data from 2020 and estimated 2021)
URL: https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

Content
- work_year: The year the salary was paid.
- experience_level: The experience level in the job during the year with the following possible values: EN Entry-level / Junior MI Mid-level / Intermediate SE Senior-level / Expert EX Executive-level / Director
- employment_type: The type of employement for the role: PT Part-time FT Full-time CT Contract FL Freelance
- job_title: The role worked in during the year.
- salary: The total gross salary amount paid.
- salary_currency: The currency of the salary paid as an ISO 4217 currency code.
- salary_in_usd: The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com).
- employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
- remote_ratio: The overall amount of work done remotely, possible values are as follows: 0 No remote work (less than 20%) 50 Partially remote 100 Fully remote (more than 80%)
- company_location: The country of the employer's main office or contracting branch as an ISO 3166 country code.
- company_size: The average number of people that worked for the company during the year: S less than 50 employees (small) M 50 to 250 employees (medium) L more than 250 employees (large)

Acknowledgements
I'd like to thank ai-jobs.net Salaries for aggregating this data!

### data_cleaned_2021.csv
URL: https://www.kaggle.com/datasets/nikhilbhathi/data-scientist-salary-us-glassdoor

scraped from glassdoor for job postings related to "Data Scientist"
