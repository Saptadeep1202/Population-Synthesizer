import pandas as pd

try:
    # Read the sample data
    data = pd.read_csv(r"C:\Users\DELL\PycharmProjects\pythonProject\Data.csv")

    # Check if the expected columns are present
    expected_columns = ['Sex', 'Age_category', 'Highest_education_level']  # Fix the column name to 'Age_group'
    missing_columns = [col for col in expected_columns if col not in data.columns]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Calculate proportions of each category in the sample data
    proportions_sex = data['Sex'].value_counts(normalize=True)
    proportions_age = data['Age_category'].value_counts(normalize=True)  # Fix the column name to 'Age_category'
    proportions_education = data['Highest_education_level'].value_counts(normalize=True)

    # Target population size
    population_size = 50000

    # Calculate number of individuals needed for each category in the synthesized population
    n_sex = (proportions_sex * population_size).round().astype(int)
    n_age = (proportions_age * population_size).round().astype(int)
    n_education = (proportions_education * population_size).round().astype(int)

    # Initialize empty lists for synthesized population data
    synthesized_data = []


    # For each category, sample individuals from the sample data based on the calculated proportions
    for category, n in zip(['Sex', 'Age_category', 'Highest_education_level'], [n_sex, n_age, n_education]):
        sampled_data = data.sample(n=n, replace=True)
        synthesized_data.append(sampled_data)


    # Concatenate the lists of synthesized population data to create a DataFrame
    synthesized_population = pd.concat(synthesized_data, ignore_index=True)

    # Write synthesized population DataFrame to a .csv file
    synthesized_population.to_csv("Synthesized_Population.csv", index=False)

    # Compute frequencies for sex, age group, and highest education level categories in the synthesized population
    frequencies = synthesized_population.groupby(['Sex', 'Age_category', 'Highest_education_level']).size().reset_index(
        name='Frequency')

    # Write frequencies to a .txt file
    with open("Frequencies.txt", "w") as f:
        f.write(frequencies.to_string(index=False))

except Exception as e:
    print("An error occurred:", e)

    print("Proportions Sex:", proportions_sex)
    print("Proportions Age:", proportions_age)
    print("Proportions Education:", proportions_education)