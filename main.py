import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df=pd.read_csv('data.csv')
data=df['reading_time'].to_list()

mean=statistics.mean(data)
stdev=statistics.stdev(data)

print('Mean and Stdev are {}, {} respectively'.format(mean,stdev))

def mean(counter):
    data_set=[]
    for i in range (0,counter):
        rand_index=random.randint(0,len(data))
        value=data[rand_index]
        data_set.append(value)

    raw_mean=statistics.mean(data_set)
    return raw_mean


def show_fig(data):
    df=data
    mean_of_sampling_data=sum(df)/len(df)
    print('Sampling mean is--> {}'.format(mean_of_sampling_data))
    fig=ff.create_distplot([df],['mean_list'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean_of_sampling_data,mean_of_sampling_data],y=[0,0.8],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    
    for i in range (0,100):
        set_of_means=mean(30)
        mean_list.append(set_of_means)
    
    stdev=statistics.stdev(mean_list)
    print("Stdev of the Sampling Distribution is--> ",stdev)
    
    show_fig(mean_list)

setup()

