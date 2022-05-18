import plotly.figure_factory as ff
import pandas as pd
import statistics 
import csv
import random 
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].to_list()
#fig = ff.create_distplot([data],['Maths Scores'],show_hist = False)
#fig.show()

#mean = statistics.mean(data)
#print('mean of population: ',mean)

standard_deviation = statistics.stdev(data)
#print('standard deviation of population is: ',standard_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)
std_deviation= statistics.stdev(mean_list)
print('standard deviation sample is : ',std_deviation)


mean = statistics.mean(mean_list)
print('mean of sampling mean: ',mean)

fig = ff.create_distplot([mean_list],['Reading_time'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = 'lines',name = 'MEAN'))
fig.show()


first_std_deviation_start,first_std_deviation_end = mean - std_deviation , mean - std_deviation
second_std_deviation_start,second_std_deviation_end = mean - (2* std_deviation), mean + (2* std_deviation)
third_std_deviation_start,third_std_deviation_end = mean - (3* std_deviation), mean + (3* std_deviation)

print('Std 1', first_std_deviation_start,first_std_deviation_end)
print('Std 2', second_std_deviation_start,second_std_deviation_end)
print('Std 3', third_std_deviation_start,third_std_deviation_end)

# plottin the graph with traces

fig = ff.create_distplot([mean_list],["reading_time"], show_hist = False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 

fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))  
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

# finding the mean of the first data and wplotting it on the plot

df = pd.read_csv('sample.csv')
data = df["reading_time"].tolist()

mean_of_sample_1 = statistics.mean(data)
print('Mean of sample 1: ', mean_of_sample_1)

fig = ff.create_distplot([mean_list], ["Hours"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[mean_of_sample_1, mean_of_sample_1], y=[0, 0.17], mode="lines", name="MEAN OF SAMPLE")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END")) 
fig.show()
