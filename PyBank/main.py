import csv
import os

# Function to read and process PyBank data
def analyze_pybank(csvfile):
    # Check if the file exists
    if not os.path.exists(csvfile):
        print(f"Error: File '{csvfile}' not found.")
        return
    
    # Initialize variables
    total_months = 0
    net_total = 0
    greatest_increase = {"amount": 0}
    greatest_decrease = {"amount": 0}
    previous_profit = None
    profit_changes = []

    # Read CSV file
    with open(csvfile, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)  # Store the header row
        
        for row in reader:
            # Calculate total months
            total_months += 1
            
            # Calculate net total amount of Profit/Losses
            profit_loss = int(row[1])
            net_total += profit_loss
            
            # Track profit changes
            if previous_profit is not None:
                change = profit_loss - previous_profit
                profit_changes.append(change)
                
                # Track greatest increase and decrease
                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = row[0]
                elif change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = row[0]
            
            previous_profit = profit_loss
    
    # Calculate average change
    average_change = sum(profit_changes) / len(profit_changes) if len(profit_changes) > 0 else 0
    
    # Prepare results
    results = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
        f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
    )
    
    # Print results to terminal
    print(results)
    
    # Write results to text file
    with open("financial_analysis.txt", 'w') as output_file:
        output_file.write(results)

# Main execution
if __name__ == "__main__":
    # Specify the correct path to budget_data.csv
    csv_path = 'C:/Users/Jean/Documents/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv'
    
    # Call analyze_pybank function with the correct path
    analyze_pybank(csv_path)
