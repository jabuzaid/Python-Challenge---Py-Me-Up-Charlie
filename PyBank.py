import os
import csv 

# Initializing the variable
total_sales_change = 0
greatest_increase = 0
greatest_decrease = 0

# setting up the path of the diretly
file_path = os.path.join('budget_data.csv')

# readindg the rows of the csv file  
with open(file_path) as file_handler:
     data_lines = csv.reader(file_handler,delimiter=',')

# skipping header row
     first_row =next(data_lines)
     
# assigning the first montrh sales
     prev = int(next(data_lines)[1])
     months_counter = 1
     total_sales = prev

# creating a for loop to read the data rows
     for row in data_lines:
          month = row[0]
          sale = int(row[1])
          change = sale - prev
          total_sales = total_sales + sale
          prev = sale

# calculating The total net amount of "Profit/Losses" over the entire perio
          total_sales_change = total_sales_change + change

# calculating the total number of months included in the dataset
          months_counter = months_counter + 1
     
# calculating the greatest monthly increase
          if change > greatest_increase:
               greatest_increase = change
               greatest_month = month


# calculating the greatest monthly decrease 
          if change < greatest_decrease:
               greatest_decrease = change
               lowest_month = month

# calculating the average change in "Profit/Losses" between months over the entire period
average_change = round(total_sales_change/(months_counter-1), 2)

# writing/creating a text file for the results
text_file = open("Finanatial_Analysis_result.txt", "w") 
print(" Financial Analysis", file = text_file)
print(" ----------------------------", file = text_file)
print("Total Months:  " + str(months_counter), file = text_file)
print("Total: $" + str(total_sales), file = text_file)
print("Average  Change: $" + str(average_change), file = text_file)
print("Greatest Increase in Profits: " + str(greatest_month) + "   ($" + str(greatest_increase) + ")", file = text_file)
print("Greatest Decrease in Profits: " + str(lowest_month) + "   ($" + str(greatest_decrease) + ")", file = text_file)
