import csv
import statistics


# Function to load data from a CSV file
def load_csv(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')  # Set delimiter to ';'
        for row in reader:
            data.append(row)
    return data


# Function to calculate basic statistics for a given column in the data
def calculate_statistics(data, column_name):
    try:
        column_data = [float(row[column_name]) for row in data if row[column_name]]
        avg = statistics.mean(column_data)
        median = statistics.median(column_data)
        min_value = min(column_data)
        max_value = max(column_data)
        return {"Average": avg, "Median": median, "Min": min_value, "Max": max_value}
    except ValueError:
        print(f"Error: The column '{column_name}' contains non-numeric data.")
        return None


# Function to display analysis results
def display_results(statistics):
    print("Basic Statistics:")
    for key, value in statistics.items():
        print(f"{key}: {value}")


# Main function to run the program
def main():
    filename = input("Enter the name of the CSV file (with extension): ")
    data = load_csv(filename)
    if not data:
        print("Error: No data found in the file.")
        return

    # Display column names to help the user
    available_columns = list(data[0].keys())
    print("\nAvailable columns:", available_columns)

    # Choose column for statistics
    column_name = input("Enter the column name to analyze: ")

    # Check if column name is valid
    if column_name not in available_columns:
        print("Error: Invalid column name entered. Program will now terminate.")
        return

    stats = calculate_statistics(data, column_name)
    if stats:
        print("\nStatistics calculated successfully.")
        display_results(stats)

    # Wait for the user to press any key before closing
    input("\nPress any key to close the program.")


# Run the program
if __name__ == "__main__":
    main()
