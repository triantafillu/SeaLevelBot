import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress


def draw_plot(year):
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df['Year'] = pd.DatetimeIndex(df['Date']).year

    # Data frame with the only columns we need
    df1 = df[['Year', 'CSIRO Adjusted Sea Level']].copy()

    # Create line plot from the original data
    sns.set_theme(color_codes=True)
    sns.lineplot(x='Year', y='CSIRO Adjusted Sea Level', data=df1, label = "sea level plot")

    # Create the distribution for the years in future (1880-year)
    years_extended_1 = np.arange(1880, year, 1)

    # Create first line of best fit
    slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = linregress(df1.iloc[:, 0], df1.iloc[:, 1])
    first_line = [slope_1 * i + intercept_1 for i in years_extended_1]

    # Plot the first line
    plt.plot(years_extended_1, first_line, 'lightcoral', label='regression line (from 1880)')

    # Create second data frame (select years 2000-year)
    df2 = df1[df1['Year'] > 1999].copy()

    # Create the distribution for the years in future (2000-year)
    years_extended_2 = np.arange(2000, year, 1)

    # Create second line of best fit
    slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = linregress(df2.iloc[:, 0], df2.iloc[:, 1])
    second_line = [slope_2 * i + intercept_2 for i in years_extended_2]

    # Plot the second line
    plt.plot(years_extended_2, second_line, 'orange', label='regression line (from 2000)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    #Legend
    plt.legend(loc = 'lower right')

    # Save plot and return
    plt.savefig('sea_level_plot.png')
    plt.clf()

    #Code used to display the sea level
    if(year<=2013):
        level = round(df1.iloc[year-1880, 1],2)
    else:
        level = round(second_line[-1],2)

    #Replacement for the markdown
    str_level = str(level).replace(".", "\.", 1)
    str_level = str(str_level).replace("-", "\-", 1)

    return str_level
