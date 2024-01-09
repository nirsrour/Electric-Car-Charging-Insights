# Electric-Car-Charging-Insights
This project aims to analyze and extract insights from EV's charging data. Analyzing key factors to gain insights for electric vehicle drivers.
# Background
Diving into the world of electric vehicle (EV) charging, this project explores a dataset (taken from Kaggle) filled with essential details like how long charging sessions last, energy used, and the costs involved. The main goal is to uncover trends and patterns that can help make smart decisions about EV infrastructure and pricing. Think of it like peeling back layers to reveal the interesting stories behind how people charge their electric vehicles and what it costs them.

# Project Objectives
--Clean and preprocess the charging data.

--Validate and convert data types for accurate analysis.

--Explore monthly trends in charging behavior.

--Visualize the charging data clearly using the most appropriate method.
# Project Challenge
--Dealing with a large and diverse dataset with missing values.

--Converting and validating diverse data types.

--Creating meaningful visualizations from the dataset.

--Creating accurate predictive models to estimate costs.

--Extracting actionable insights from complex data.

--Addressing these challenges is crucial to ensure accurate insights into charging patterns and costs.

# Initial insights
--Data set contains thousands of charging sessions, some of the columns had missing, invalid, or inconsistent values.

--Different data types, such as int, float, object, and bool.

--The data needed to be cleaned and prepared, such as filtering, renaming, dropping, and converting the data.

--Data also needed to be validated, such as checking and correcting the data types of each column.

--The data set contains mostly nominal and ordinal values, which can be challenging for certain machine learning algorithms.
# Solutions
--The project addresses challenges by filtering and cleaning the dataset, standardizing data types, and creating insightful visualizations.

--Non-numeric values in the 'distance' column are filtered out, and currency values are converted to the local currency.

--Data types are validated and converted, enabling meaningful analysis. 

--Visualizations, including bar and line charts, provide a clear representation of monthly charging trends.

# Data preprocessing and Methods
--Imported the data from a CSV file and printed the basic information and summary statistics of the data using the pandas library

--Filtered the distance column by numeric values and removed the null values

--Filtered the reportedZip column by non-zero values

--Renamed the dollars column to KWH_Price [ILS] and assigned a fixed value of 0.6007

--Dropped the weekday, managerVehicle, and reportedZip columns as they were not relevant or useful for the analysis.

--Wrote a custom function to convert and validate the data types of each column.

--Calculated and compared the key metrics of EV charging, such as the number, frequency, duration, distance, and cost of charging sessions using descriptive statistics and aggregation methods.

--Identified and analyzed the variables that affect the EV charging behavior and consumption, such as the time, location, vehicle type, and price using correlation analysis and hypothesis testing.

--Visualized and communicated the findings and insights from the data analysis using plots, charts, and tables using the matplotlib and seaborn librariesIrrelevant data, such as the "RANK" column and null values, were removed.

# Excel Uses
--VLOOKUP Utilization: Leveraging Excel's function, the currency column was standardized, ensuring a consistent representation in the local currency and facilitating a more coherent analysis.

--Pivot Tables for Aggregation: Pivot Tables were instrumental in aggregating and summarizing the dataset, providing a concise overview of monthly charging trends and aiding in the identification of patterns.

--Histograms for Distribution Analysis: The creation of histograms added a visual layer to the analysis, offering insights into the distribution of charging behaviors and highlighting potential concentration points or outliers.

--Graphs for Visual Representation: Diverse Excel graphs, including bar charts and line charts, were employed to visually represent the average final price by month. These graphical representations enhanced the interpretability of trends and patterns within the dataset, fostering a more intuitive understanding of electric vehicle charging dynamics.


# Results
The project's results offer clear insights into electric vehicle charging behaviors:

--Monthly Trends: 

Visualizations depict varying average final prices, highlighting monthly charging patterns.

--Data Cleaning Impact: 

Rigorous cleaning led to a well-structured dataset, crucial for accurate analysis.

--Informed Decision-Making: 
The combination of Python analysis and Excel visualization equips stakeholders for strategic decisions in EV infrastructure and pricing.

--User-Friendly Graphs: 
Graphical representations enhance accessibility, aiding in the interpretation of charging dynamics.


These outcomes collectively contribute to a more comprehensive understanding of the dataset, paving the way for informed decision-making in the electric vehicle domain.
