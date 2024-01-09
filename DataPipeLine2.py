import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
print(df)

print(df.info())

def is_numeric(value):
    return isinstance(value, (int, float))

#-------------Data Cleaning-------------------#
df = df[df['distance'].apply(is_numeric) & ~df['distance'].isna()]  #filter the df column 'distance' by numeric values
df = df[df['reportedZip'] != 0] #filter df 'reporterzip' to only rows wich reported.1 and not 0. (binary)
df.rename(columns={'dollars': 'KWH_Price [ILS]'}, inplace=True) #rename the dollar column to Kwh_price and set values of 0.6007
df['KWH_Price [ILS]'] = 0.6007


# Drop unnecessary columns
df.drop(columns=['weekday', 'managerVehicle', 'reportedZip'], inplace=True)

print(df)



# Convert columns to their proper types
# Function to convert and validate data types
def convert_and_validate(column_name, dtype):
    try:
        df[column_name] = df[column_name].astype(dtype)
    except Exception:
        for index, value in df[column_name].items():
            try:
                dtype(value)
            except Exception:
                raise Exception(f"Invalid data type in column '{column_name}', row {index}, value '{value}', it should be'{dtype}'")


# for index, data_frame_item in tqdm(df.iterrows(), total=df.shape[0], desc="Loading Data", ncols=100):
#     data_list = data_frame_item
#     print(data_list)

# Convert and validate each column's data type
convert_and_validate('sessionId', int)
convert_and_validate('kwhTotal', float)
convert_and_validate('KWH_Price [ILS]', float)
convert_and_validate('created', object)
convert_and_validate('ended',object)
convert_and_validate('startTime', int)
convert_and_validate('endTime', int)
convert_and_validate('chargeTimeHrs', float)
#convert_and_validate('weekday', str)
convert_and_validate('platform', str)
convert_and_validate('distance', float)
convert_and_validate('userId', int)
convert_and_validate('stationId', int)
convert_and_validate('locationId', int)
#convert_and_validate('managerVehicle', int)
convert_and_validate('facilityType', int)
convert_and_validate('Mon', int)
convert_and_validate('Tues', int)
convert_and_validate('Wed', int)
convert_and_validate('Thurs', int)
convert_and_validate('Fri', int)
convert_and_validate('Sat', int)
convert_and_validate('Sun', int)
#convert_and_validate('reportedZip', int)

#create new columns of month and day, and target columns
df['date'] = pd.DataFrame(df['created'].str.split(' ', expand=True)[0])
df['Month'] = pd.DataFrame(df['date'].str.split('-', expand=True)[1])
df['Day']= pd.DataFrame(df['date'].str.split('-', expand=True)[2])
df['final_price'] = df['KWH_Price [ILS]']*df['kwhTotal']*df['chargeTimeHrs']


# Calculate the logarithm of 'final_price' with base e
def custom_log(value, base):
    return math.log(value, base)
base_value = math.e
df['ln_final_price'] = df['final_price'].apply(lambda x: custom_log(x, base_value))

# df['ln_final_price'] = df['final_price'] * df['final_price'].apply(math.log)

#drop the columns we dont need
df.drop(columns=['date','created','ended'], inplace=True)

#----- Print the updated DataFrame --------

#print(df)
total_null_percentage = round(((df.isnull().sum().sum() / (df.shape[0])) * 100),2)
print(f"Total percentage of all null values: {total_null_percentage}%")



#-------------------------Area Graph with barplot-----------------#
# Group the data by months
monthly_data = df.groupby('Month')['final_price'].mean().reset_index()
fig, ax1 = plt.subplots(figsize=(12, 6))

sns.barplot(data=monthly_data, x='Month', y='final_price', palette='viridis', ax=ax1)
ax1.set_xlabel('Month')
ax1.set_ylabel('Average Final Price')
ax1.set_title('Average Final Price by Month (Bar Chart)')

# Add data labels
for index, row in monthly_data.iterrows():
    ax1.text(index, row['final_price'], f'{row["final_price"]:.2f}', ha='center', va='bottom', fontsize=10)

# Create a second y-axis for the area chart
ax2 = ax1.twinx()

# Area chart
ax2.fill_between(monthly_data['Month'], 0, monthly_data['final_price'], color='blue', alpha=0.3)
ax2.set_ylabel('Average Final Price (Area graph)', color='blue')
plt.xticks(rotation=45)
plt.show()

#-------------------------Line Graph with barplot-----------------#

monthly_data1 = df.groupby('Month')['final_price'].mean().reset_index()
fig1, axis1 = plt.subplots(figsize=(12, 6))
# Bar chart
sns.barplot(data=monthly_data, x='Month', y='final_price', palette='viridis', ax=axis1)
axis1.set_xlabel('Month')
axis1.set_ylabel('Average Final Price')
axis1.set_title('Average Final Price by Month (Bar Chart)')
# Add data labels
for index, row in monthly_data1.iterrows():
    axis1.text(index, row['final_price'], f'{row["final_price"]:.2f}', ha='center', va='bottom', fontsize=10)

# Create a second y-axis for the line chart (right y-axis)
ax2 = axis1.twinx()

# Line chart
sns.lineplot(data=monthly_data1, x='Month', y='final_price', color='red', marker='o', ax=ax2)
ax2.set_ylabel('Average Final Price (Line Chart)', color='red')
plt.xticks(rotation=45)
plt.show()







