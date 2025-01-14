from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(value):
    """
    Converts population or GDP string values to numeric.
    Handles values with 'M' (millions) or 'k' (thousands) suffixes.
    """
    if isinstance(value, str):
        if value.endswith("M"):
            return float(value[:-1]) * 1e6
        elif value.endswith("k"):
            return float(value[:-1]) * 1e3
        else:
            return float(value)
    return float(value)


def main():
    """
    Loads data, processes it, and plots life expectancy against GDP
    for all countries in the year 1900.
    """
    # Load the datasets
    life_expectancy_data = load("life_expectancy_years.csv")
    gdp_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if life_expectancy_data is None or gdp_data is None:
        print("Error: Could not load one or both datasets.")
        return

    # Extract data for the year 1900
    life_expectancy_1900 = life_expectancy_data[["country", "1900"]]
    gdp_1900 = gdp_data[["country", "1900"]]

    # Merge the datasets on the 'country' column
    merged_data = life_expectancy_1900.merge(gdp_1900, on="country", how="inner", suffixes=("_life", "_gdp"))

    # Preprocess the values in both columns
    merged_data["1900_life"] = merged_data["1900_life"].apply(preprocess_population)
    merged_data["1900_gdp"] = merged_data["1900_gdp"].apply(preprocess_population)

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data["1900_gdp"], merged_data["1900_life"], alpha=0.7)
    plt.title("Life Expectancy vs GDP (Year 1900)")
    plt.xlabel("GDP per Capita (PPP, inflation-adjusted)")
    plt.ylabel("Life Expectancy (years)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
