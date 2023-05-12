                   # Sales Reports Generate For Update Rech

# The Requirements:
1.	pip3 install -r requirements.txt

# Task-1 :
● Created an Entity for the user model using AbstractBaseUser class and a custom
user manager using BaseUserManager
● And implement login and registration API with DRF

URL : 
For Registration: http://127.0.0.1:8000/users/register/

{
    "user_name",
    "email",
    "password",
    "phone_number",
    "address"
}

For Login: http://127.0.0.1:8000/users/login/

{
    "email",
    "password"
}


### Task-2 :
● Download the given SQL or CSV dataset where some sales data of a super shop
has been recorded.
● Create and migrate a model for a sales table, for the field specification check the
given dataset. You also need to import the existing data into your database.
● Create a REST API for data insertion and manipulation
● Create an API that will generate a PDF report from the given dataset. The report
should include the below information:
○ Total number of orders count per year
○ Total count of distinct customers
○ Top 3 customers who have ordered the most with their total amount of
transactions.
○ Customer Transactions per Year (from the beginning year to last year)
○ Most selling items sub-category names
○ Region basis sales performance pie chart
○ Sales performance line chart over the years


To Add sale: API
Url: http://127.0.0.1:8000/sales/saleslist/      (GET+POST)
URL: http://127.0.0.1:8000/sales/saleslist/9800/ (PUT/DELETE)


Then PDF Generate and count data show in HTML:
To show data also download PDF:
URL:  http://127.0.0.1:8000/sales/sale_report/

