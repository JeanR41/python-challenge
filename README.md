# python-challenge
Module 3 Challenge

Received help from tutoring session with Fred.
Biggest support was in helping Specify Path for csv files. Added the below to code to help locate files (showing PyBank code - similar code was used for PyPoll):

# Function to read and process PyBank data
def analyze_pybank(csvfile):
    if not os.path.exists(csvfile):
        print(f"Error: File '{csvfile}' not found.")
        return

 # Specify the correct path to budget_data.csv
    csv_path = 'C:/Users/Jean/Documents/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv'
    