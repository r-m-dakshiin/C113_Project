from random import random
import plotly.express as px
import pandas as pd
import statistics
import csv

df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df,y="quant_saved", color = "rem_any")
fig.show()

with open("savings_data_final.csv", newline="") as f:
    reader = csv.reader(f)
    savings_data = list(reader)
savings_data.pop(0)

import plotly.graph_objects as go

total_entries = len(savings_data)
total_people_given_reminder =  0
for data in savings_data:
    if(int(data[3]) ==  1):
        total_people_given_reminder += 1
fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y = [total_people_given_reminder, (total_entries - total_people_given_reminder)]))
fig.show()

savings_array = []
for data in savings_data:
    savings_array.append(float(data[0]))
print(f"Mean of saving- {statistics.mean(savings_array)}")
print(f"Median of saving - {statistics.median(savings_array)}")
print(f"Mode of saving - {statistics.mode(savings_array)}")


remainded_array = []
not_remainded_array = []

for data in savings_data:
    if(int(data[3]) == 1):
        remainded_array.append(float(data[0]))
    else:
        not_remainded_array.append(float(data[0]))

print(f"Mean of remainded people - {statistics.mean(remainded_array)}")
print(f"Median of remainded people - {statistics.median(remainded_array)}")
print(f"Mode of remainded people - {statistics.mode(remainded_array)}")

print(f"Mean of not remainded people- {statistics.mean(not_remainded_array)}")
print(f"Median of not remainded people - {statistics.median(not_remainded_array)}")
print(f"Mode of not remainded people - {statistics.mode(not_remainded_array)}")

std_deviation_remainded = statistics.stdev(remainded_array)
std_deviation_not_remainded = statistics.stdev(not_remainded_array)
print(f"Standard deviation of all the data : {statistics.stdev(savings_array)}")
print(f"Std deviation for Remainded people : {std_deviation_remainded}")
print(f"Std deviation for Not Remainded people : {std_deviation_not_remainded}")

import numpy as np
import seaborn as sns
age = []
savings = []
for data in savings_data:
    if float(data[5])!=0:
        age.append(float(data[5]))
        savings.append(float(data[0]))
        
correlation = np.corrcoef(age,savings)
print(f"Correlation between the age of the person and their savings : {correlation[0,1]}")

import plotly.figure_factory as ff
fig = ff.create_distplot([df["quant_saved"].tolist()], ["Savings"], show_hist=False)
fig.show()

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3-q1

print(f"Q1 - {q1}")
print(f"Q3 - {q3}")
print(f"IQR - {iqr}")

lower_whisker = q1 - 1.5*iqr
upper_whisker = q3 + 1.5*iqr

print(f"Lower whisker : {lower_whisker}")
print(f"Upper whisker : {upper_whisker}")

new_df = df[df["quant_saved"] < upper_whisker]


all_savings = new_df["quant_saved"].tolist()
print(f"Mean savings : {statistics.mean(all_savings)}")
print(f"Median savings : {statistics.median(all_savings)}")
print(f"Mode savings : {statistics.mode(all_savings)}")
print(f"Std deviation of savings : {statistics.stdev(all_savings)}")
fig = ff.create_distplot([new_df["quant_saved"].tolist()], ["Savings"], show_hist=False)
fig.show()

import random

sampling_mean_list = []

for i in range(1000):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(all_savings))
    sampling_mean_list.append(statistics.mean(temp_list))
mean_sampling = statistics.mean(sampling_mean_list)
fig = ff.create_distplot([sampling_mean_list], ["Savings(sampling)"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean_sampling, mean_sampling], y=[0, 0.1], mode="lines", name="MEAN"))
fig.show()

print(f"Standard deviation of the sampling data - {statistics.stdev(sampling_mean_list)}")