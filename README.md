# Customer signup prediction
This project is focused on predicting the number of newly acquired customers over time. It will be used for energy procurement and marketing campaigns. 

## 1. Project description
The two main components of this project are (i) building a preprocessing pipeline and (ii) prediction modeling. 

**Preprocessing:**
- Load and transform the raw data stored in ```data/raw/interview_signup.csv``` so it can be used for modeling. The processed data is stored in ```data/processed/interview_signup_processed.csv```. This is done in an ETL manner in ```notebooks/EDA.ipynb```.
- To make the transformation steps from ```notebooks/EDA.ipynb``` reusable, scalable and maintainable, a module in ```src/etl.py``` is *in development*. In ```notebooks/demo_etl_module.ipynb```, you can find a more simplified ETL pipeline (object-oriented) building on functionalities of ```src/etl.py``` (still limited features).
- CAUTION: The transformation logic in the preprocessing steps may need to be adapted if...
    - ... data formats and types change in the raw data 
    - ... new columns are added to the raw data
    - ... new inconsistencies arise 

**Modeling:** yet to be implemented. In the future, modules belong in ```src/example_model.py``` and notebooks in ```notebooks/example_model.ipynb```.

## 2. Raw data
The data is stored in csv format and comes from 2018. It contains the following columns:
| Column name           | Column description                                          |
| --------------------- | ----------------------------------------------------------- | 
| original_product_name | Product the customer signed up to                           |
| postcode              | Postcode of the customer (5 digits with 0-9)                |
| bundesland            | The state the customer lives                                |
| total_bonus           | The bonus amount we provided (reduces the first-year price) |
| order_date            | The date that the customer ordered the product              |

## 3. Data issues and open questions
**High-level issues**:
- Raw data contains duplicate rows
    - Can we savely delete duplicate data? In theory, it can happen that several customers order the same product on the same date with the same home address postcode and the same total bonus...
- Are we sure that no data are missing? For example, there are no gas products in the dataset.
- Do we need all 5 columns from the dataset for the prediction task?
- What exactely do we want to predict with the data on which granularity?
    - aggregation logics
        - Are future customer sign-ups predicted on a daily, weekly, monthly, ... basis? 
        - Are we interested in the number of new sign-ups per state, postcode or product? 
    - what is our target variable?

**Low-level issues:**
- original_product_name: 
    - ambiguous data: misspellings that might partly be caused by inappropriate character encoding in earlier data processing steps.
    - unclear distinct groups (are there 4,5,6 different product names?). The best guess is that there are 5 products: E.ON STROM, E.ON STROM 24, E.ON STROM ÖKO, E.ON STROM ÖKO 24, E.ON STROM PUR.
    - save memory by converting to categorical data type
- postcode:
    - mixture of data types and inconsistent formats
        - trailing decimal part (might come from type conversion in earlier data processing steps.)
        - leading 0 is missing sometimes
        - one odd case with additional letters.
- bundesland: 
    - inconsistent naming convention: German column name and entries
    - may be redundant information (postcode more fine-grained)
    - 10% missing values
        - strict N:1 relationship between postcode and state? -> not quite
        - infer empty bundesland from the postcode
        - fill with "unknown" or drop?
    - can we use an external data/apis to enrich our data?
    - save memory by converting to categorical data type
- total_bonus: 
    - data accuracy: data is float but contains no decimals. 
        - were decimals lost in type conversion?
        - can we assume that the currency is € consistently?
        - data type could be changed from float64 to int16 to save memory
    - outliers
        - are values of 0 possible according to business rules? 
        - there are over 500 cases where the total bonus was between 1 and 20 €. These bonuses seem very small.
        - there are 200 cases where the total bonus is larger or equal to 400 €. These bonuses seem very large.
    - more detailed analyses could look at:
        - are there cases where zeros appear frequently (e.g., on certain dates or products)?
        - is the **timeseries** of mean total_bonus stationary? Is there data drift ?
- order_date: 
    - convert to date format
        - potentially extract derived features like day-of-year, month, ...
        - add derived feature, e.g. days to last sign-up for the product in this postcode area 

## 4. Installation and configuration instructions 
1. Make sure python is installed on your system. ```python_version == 3.8.10``` required
2. Navigate into your local repo 'customer-signup-prediction'. Run ```git clone https://github.com/Neuraldominator/customer-signup-prediction.git```
3. Next, set up a virtual environment for python. The commands below will install all necessary packages and dependencies from ```requirements.txt``` into your virtual environment ```.venv```:
    - On **Mac and Linux**, run ```chmod +x create_venv.sh``` followed by ```./create_venv.sh``` 
    - On **Windows**, execute ```.\create_venv.bat```
4. Activate your virtual environment by running ```source .venv/bin/activate``` in a **Linux or Mac** terminal or ```call .venv\Scripts\activate.bat``` in a **Windows** terminal.

## 5. How to use the Project 
- Start with ```notebooks/EDA.ipynb``` and follow the preprocessing steps. The focus there is on cleaning postcodes.
- Not all necessary preprocessing steps were conducted. Feel free to collaborate on the project and reach out. 
- For more consistent usage of the preprocessing steps, the module ```etl.py``` could be further developed. 

## 6. Contact information
vorname.nachname@email.com
