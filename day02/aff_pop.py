from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    """
    Converts population string to a numeric value.
    
    Handles values with 'M' (millions) or 'k' (thousands) suffixes.
    """
    if isinstance(pop_str, str):
        if pop_str.endswith("M"):
            return float(pop_str[:-1]) * 1e6
        elif pop_str.endswith("k"):
            return float(pop_str[:-1]) * 1e3
        else:
            return float(pop_str)
    return float(pop_str)


def main():
    """
    Loads and processes population data, then plots population trends
    for three countries.
    """
    # Load the dataset
    data = load("population_total.csv")
    
    if data is None:
        print("Error: Could not load the dataset.")
        return

    # Define the countries to compare
    country1 = "Germany"
    country2 = "France"
    country3 = "Hungary"

    # Extract data for the selected countries
    country1_data = data[data['country'] == country1].iloc[:, 1:]
    country2_data = data[data['country'] == country2].iloc[:, 1:]
    country3_data = data[data['country'] == country3].iloc[:, 1:]
    years = country1_data.columns.astype(int)

    # Convert population data to numeric values
    country1_pop = [preprocess_population(pop) for pop in country1_data.values.flatten()]
    country2_pop = [preprocess_population(pop) for pop in country2_data.values.flatten()]
    country3_pop = [preprocess_population(pop) for pop in country3_data.values.flatten()]

    # Plot the data
    plt.plot(years, country1_pop, label=country1)
    plt.plot(years, country2_pop, label=country2)
    plt.plot(years, country3_pop, label=country3)

    # Add title, labels, and legend
    plt.title("Population Comparison")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
