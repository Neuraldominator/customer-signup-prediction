# Customer signup data preprocessing
Predicting the number of newly acquired customers has many interesting use cases for an energy supplier. It can be used for energy procurement on the forward market and help steer marketing campaigns. In this project, we use contract data from the past to clean the data such that it can be used for future prediction models.

## 1. Project description
- Goal of this project is to build a preprocessing pipeline in an ETL manner. Raw data is stored in ```data/raw/interview_signup.csv```. Processed data is loaded into ```data/processed/interview_signup_processed.csv```.
- The toolbox in ```src/etl.py``` provides methods to perform the preprocessing of data. 
- Challenges: what happens if raw_data will deviate in future?
    - loaded data formats change
        - new (unknown) columns
        - data types change
    - transformation logic changes

## 2. Raw data
| Column name           | Column description                                          |
| --------------------- | ----------------------------------------------------------- | 
| original_product_name | Product the customer signed up to                           |
| postcode              | Postcode of the customer (5 digits with 0-9)                |
| bundesland            | The state the customer lives                                |
| total_bonus           | The bonus amount we provided (reduces the first-year price) |
| order_date            | The date that the customer ordered the product              |

## 3. Data issues
https://github.com/kennedykwangari/Data-Cleaning-with-Python-Challenges-/blob/master/Data%20Cleaning%20Character%20Encoding.ipynb

- duplications?
- original_product_name: misspellings and unclear distinct groups (E.ON STROM, E.ON STROM 24, E.ON STROM ÖKO, E.ON STROM ÖKO 24, E.ON STROM PUR ?)
- postcode: mixture of data types, leading 0 is missing sometimes, one odd case 
- bundesland: missing values, N:1 relationship
- total_bonus: are values of 0 fine? Otherwise, this column looks good.
- order_date: should be in date format

## 4. Installation and configuration instructions 
1. Make sure python is installed on your system. (```python_version >= 3.8.10``` required)
2. Navigate into your local repo 'customer-signup-prediction'. 
3. Next, set up a virtual environment for python. The commands below will install all necessary packages and dependencies from ```requirements.txt``` into your virtual environment ```.venv```:
    - On **Linux**, run ```chmod +x create_venv.sh``` followed by ```./create_venv.sh``` 
    - On **Windows**, execute ```create_venv.bat```
4. Activate your virtual environment by running ```source .venv/bin/activate``` in a **Linux** terminal or ```call .venv\Scripts\activate.bat``` in a **Windows** terminal.

## 5. How to use the Project 
- Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.
- You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.
- Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.

## 6. Contact information
Dominik Kessler
email: dominik.kessler@eon.com
