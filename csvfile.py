#Write a Python program to read a CSV file and display its contents.
import csv


# Specify the path to your CSV file
file_path = 'D:/Machine Learning/Book1.csv'

try:
    # Open and read the CSV file
    with open(file_path, mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Read and print each row
        for row in csvreader:
            print(row)
except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


"""Output:
['Age', 'Premium']
['25', '18000']
['30', '32000']
['35', '40000']
['40', '47000']
['45', '55000']"""
