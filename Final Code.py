import csv
def read_data():
    data = [] # initialize an empty list to store data
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row) # append each row to the data list
    return data

def mytotal():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    return total

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('sales.csv')

# Create a bar chart of monthly sales and expenditures
ax = df.plot(kind='bar', x='month', y=['sales', 'expenditure'], color=['blue', 'red'])

# Set the x-axis label to be the months
ax.set_xlabel('Month')

# Set the y-axis label to be the Euros
ax.set_ylabel('Euros')

# Add a title
ax.set_title('Monthly Sales and Expenditures')

# Show the plot
plt.show()

def myMax():
    data = read_data()
  # Assume first number in list is largest
  # initially and assign it to variable "max"
    max_row = data[0]
  # Now traverse through the list and compare
  # each number with "max" value. Whichever is
  # largest assign that value to "max'.
    for row in data:
        if int(row['sales']) > int(max_row["sales"]):
            max_row = row

  # after complete traversing the list
  # return the "max" value
    return max_row

print("Largest element is:", myMax())

def mymin():
    data = read_data()
  # Assume first number in list is largest
  # initially and assign it to variable "max"
    min_row = data[0]
  # Now traverse through the list and compare
  # each number with "max" value. Whichever is
  # largest assign that value to "max'.
    for row in data:
        if int(row['sales']) < int(min_row['sales']):
            min_row = row

  # after complete traversing the list
  # return the "max" value
    return min_row

print("Smallest element is:", mymin())

def average():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    average_sales = total / len(sales)
    return average_sales

print ("The average is : ", average())

sales_list = []
with open('sales.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip the header line
    for row in reader:
        sales_list.append(float(row[2]))

print(sales_list)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_change = []
monthly_change_sentences = []

for i in range(1, len(sales_list)):
    change = (sales_list[i] - sales_list[i-1]) / sales_list[i-1] * 100
    monthly_change.append(round(change,2)) # keep two decimals

for i in range(len(monthly_change)):
    monthly_change_sentences.append(f"{month_names[i+1]} between {month_names[i]} changes as {monthly_change[i]} %")

x = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y = monthly_change

plt.plot(x, y)
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.title('Percentage Changes')
plt.show()

import pandas as pd
# 1. read the data
df = pd.read_csv('sales.csv')
# 2. Collect sales for each month into a list
sales_list = df['sales'].tolist()
# 3. output the sales of all months
total_sales = sum(sales_list)
print('Total sales across all months:', total_sales)

import matplotlib.pyplot as plt
# Convert data into pivot tables to show sales and expenses by month
pivot_table = pd.pivot_table(df, values=['sales', 'expenditure'], index=['month'], aggfunc=sum)
# Plotting stacked bars of sales and expenditures
pivot_table.plot(kind='bar', stacked=True)
# add title and labels
plt.title('Sales and Expenditure by Month')
plt.xlabel('Month')
plt.ylabel('Amount')
# Visualisation
plt.show()

# Combine the "year" and "month" columns into one date column
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'], format='%Y-%b')
# sort the data by date
df = df.sort_values(by='date')
# Set the date column as an index column
df = df.set_index('date')
# Plotting a line graph of sales and expenditure
df[['sales', 'expenditure']].plot()
# add title and labels
plt.title('Sales and Expenditure Trend')
plt.xlabel('Date')
plt.ylabel('Amount')
# vistualisation
plt.show()


list1 = [mytotal(),'','','','','','','','','','']
list2 = [myMax()["month"],'','','','','','','','','','']
list3 = [mymin()["month"],'','','','','','','','','','']
list4 = [average(),'','','','','','','','','','']
list5 = monthly_change_sentences
col1 = "Total Sales"
col2 = "Largest Sales Month"
col3 = "Lowest Sales Month"
col4 = "Sale Average"
col5 = "Monthly Percentage changes"

data = pd.DataFrame({col1:list1,col2:list2,col3:list3,col4:list4,col5:list5})
data.to_excel('sales report 2018.xlsx', sheet_name='2018 Sales', index=False)