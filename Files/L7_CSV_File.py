# CSV Docs Comma-Separated Values (CSV) is a text file format where individual values are separated by commas.
# file is an example of a text file that imposes a structure on its data. CSV stands for Comma-Separated Values, and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format

with open('logger.csv') as log_csv_file:
  print(log_csv_file.read()) 

