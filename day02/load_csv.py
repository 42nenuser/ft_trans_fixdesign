import pandas as pd

def load(path: str):
    """
    Load a CSV file, display its dimensions, and return the dataset.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame or None: The loaded dataset as a DataFrame, or None if there was an error.
    """
    try:
        # Attempt to load the CSV file
        data = pd.read_csv(path)
        
        # Print dimensions of the dataset
        print(f"Loading dataset of dimensions {data.shape}")
        
        # Print a preview of the dataset
        print(data.head())
        
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: File content is invalid or not a CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

# Example tester script
if __name__ == "__main__":
    # Replace 'life_expectancy_years.csv' with your file path
    dataset = load("life_expectancy_years.csv")
