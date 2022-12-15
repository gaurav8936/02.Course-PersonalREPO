import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# These commands below set some options for pandas and to have matplotlib show the charts in the notebook
pd.set_option('display.max_rows', 1000)
pd.options.display.float_format = '{:,.2f}'.format

# Load the data
# We have this defaulted to the folder OUTSIDE of your repo - please change it as needed
contrib = pd.read_csv('2016_ca_primary_cleaned.csv', index_col=False, parse_dates=['contb_receipt_dt'])

x = contrib['contb_receipt_amt']

n = len(x)
r = np.max(x) - np.min(x)
width = r // np.sqrt(n)
bins = []
i = int(np.min(x))
while i < np.max(x):
    bins.append(i)
    i += width


fig = plt.figure()
plt.hist(x,bins=bins,range=range(0, 25))
fig.suptitle('Histogram of contb_receipt_amt', fontsize=14)
plt.xlabel('Bins', fontsize=10)
plt.ylabel('Contribution', fontsize=10)
#plt.show()

#1b
fig = plt.figure()
plt.hist(x,bins=bins,range=range(0, 25))
fig.suptitle('Histogram of contb_receipt_amt', fontsize=14)
plt.xlabel('Bins', fontsize=10)
plt.ylabel('Contribution', fontsize=10)
# plt.show()


#1c

# data_sanders = contrib[contrib['cand_nm'].str.contains('Sanders')]
# grouped_sanders = data_sanders.groupby('contb_receipt_dt').sum('contb_receipt_amt')
# print(contrib.columns)
# min_date = min(grouped_sanders['contb_receipt_dt'])
# max_date = max(grouped_sanders['contb_receipt_dt'])
# delta = (max_date-min_date).days
# times = pd.date_range(min_date, periods=delta, freq='D')
# yvalues = range(times.size)df = pd.DataFrame(yvalues, grouped_sanders['contb_receipt_amt'].values)
#
# fig, ax = plt.subplots(1)
# fig.autofmt_xdate()
# ax.axvline(pd.to_datetime('2023-01-23'), color='r', linestyle='--', lw=2)
# ax = df.plot(ax=ax, title='Random Forest Regressor Performance')
# plt.show()

# ax = contrib['c.plot(ax=ax, title='Random Forest Regressor Performance')
# plt.show()


#2a

# Let's investigate the donations to the candidates. (5 points)
#
# 2a. Present a table that shows the number of donations to each candidate sorted by number of donations.**
#
# When presenting data as a table, it is often best to sort the data in a meaningful way. This makes it easier for your reader to examine what you've done and to glean insights. From now on, all tables that you present in this assignment (and course) should be sorted.
# Hint: Use the groupby method. Groupby is explained in Unit 13: async 13.3 & 13.5
# Hint: Use the sort_values method to sort the data so that candidates with the largest number of donations appear on top.
# Which candidate received the largest number/count of contributions (variable 'contb_receipt_amt')?


print(contrib.columns)
donations = contrib.groupby(['cand_nm'])['contb_receipt_amt'].count().sort_values(ascending=False)
print(donations)

# Sanders, Bernard             379284

#2b Now, present a table that shows the total value of donations to each candidate sorted by total value of the donations. (5 points)

donations_values = contrib.groupby(['cand_nm'])['contb_receipt_amt'].sum().sort_values(ascending=False)
print(donations_values)

# Clinton, Hillary Rodham     38,969,122.68

# 2c
merged_data = pd.merge(donations.to_frame(),donations_values.to_frame(),left_index=True, right_index=True)
print(merged_data)

# 2d
merged_data['Average_Donation'] = merged_data['contb_receipt_amt_y'] / merged_data['contb_receipt_amt_x']
print(merged_data['Average_Donation'])

#2e
df = merged_data.drop('contb_receipt_amt_x',axis=1)
df.columns = df.columns.str.replace('contb_receipt_amt_y', 'Total_Value')
df.plot(kind="bar", title="test")
# Rotate the x-labels by 30 degrees, and keep the text aligned horizontally
plt.xticks(rotation=30, horizontalalignment="center")
plt.title("Total donations (sum and average) per Candidate")
plt.xlabel("Candidate")
plt.ylabel("Total Donations")
# plt.show()

#3a
value = 'Clinton'
clinton= contrib[contrib['cand_nm'].str.contains('Clinton')]
occupations = clinton['contbr_occupation'].value_counts()
print(occupations.head())

'''
RETIRED                  35767
ATTORNEY                  7514
INFORMATION REQUESTED     4991
TEACHER                   3848
HOMEMAKER                 3522
'''

#3b
def get_donors(df):
    """This function takes a dataframe that contains a variable named contbr_occupation.
    It outputs a Series containing the counts for the 5 most common values of that
    variable."""

    # 3b YOUR CODE HERE
    occupations = clinton['contbr_occupation'].value_counts()
    return occupations.head()

#3c
values = ['Clinton','Sanders','Trump']
for value in values:
    subset = contrib[contrib['cand_nm'].str.contains(value)]
    print(get_donors(subset))