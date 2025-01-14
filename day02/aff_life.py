import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

def plot_country_life_expectancy(data, country):
    """
    Plot the life expectancy of a given country over time using Seaborn.

    Parameters:
    data (pd.DataFrame): The dataset containing life expectancy data.
    country (str): The name of the country to plot.
    """
    if country not in data['country'].values:
        print(f"Error: {country} is not found in the dataset.")
        return
    
    # Extract the country's data
    country_data = data[data['country'] == country].iloc[0, 1:]
    
    # Convert data to a DataFrame for Seaborn
    years = country_data.index.astype(int)
    life_expectancy = country_data.values
    plot_data = pd.DataFrame({'Year': years, 'Life Expectancy': life_expectancy})
    
    # Set Seaborn theme
    sns.set_theme(style="whitegrid")
    
    # Plot the data
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=plot_data, x='Year', y='Life Expectancy', marker='o', label=country)
    
    # Add labels and title
    plt.title(f"Life Expectancy Over Time: {country}", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)
    plt.legend(title="Country", fontsize=10)
    plt.show()

# Example tester script
if __name__ == "__main__":
    # Load the dataset
    dataset = load("life_expectancy_years.csv")
    
    # Plot the data for the given country
    if dataset is not None:
        plot_country_life_expectancy(dataset, "Morocco")  # Replace "Morocco" with your campus country
