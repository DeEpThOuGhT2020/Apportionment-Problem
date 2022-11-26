import sys
import plotly
import pandas as pd
import geojson
pd.options.mode.chained_assignment = None 
from geojson_rewind import rewind
import apportionpy.apportionment as ap

years = [2019, 2014, 2009, 2004 , 1999 , 1996 , 1991 , 1989 , 1984 , 1980 , 1977 , 1971 , 1967 ]
methods = ["hamilton","adam","webster","jefferson","huntington hill",'Seats','Quota']
to_use1 = int(sys.argv[1])
to_use2 = int(sys.argv[2])
color_range = [-10,10]

filepath = "ALL_HTMLS/"+methods[to_use1].title()+"_"+methods[to_use2].title() + '.html'

df_list = []
for yer in years:
    df_year = pd.read_csv('Final_Data/' + str(yer) + '/' + str(yer) + ' copy.csv')
    df_list.append(df_year)

i = 0
for df_ in df_list:
    df_ = df_.fillna(0)
    seats = df_.loc[len(df_.index)-1].at['Seats']
    populations = df_['Electors'][:-1]
    if(methods[to_use1]!="Seats" and methods[to_use1]!="Quota"):
        result_1 = ap.Apportion(seats=seats, populations=populations, method=methods[to_use1])
        x = result_1.fair_shares
        sum_ = sum(x)
        x.append(sum_)
        df_[methods[to_use1]] = x
    if(methods[to_use2]!="Seats" and methods[to_use2]!="Quota"):
        result_2 = ap.Apportion(seats=seats, populations=populations, method=methods[to_use2])
        x = result_2.fair_shares
        sum_ = sum(x)
        x.append(sum_)
        df_[methods[to_use2]] = x
    df_['Difference'] = df_[methods[to_use1]] - df_[methods[to_use2]]
    df_list[i] = df_
    i += 1

def hover_text(df):
    df['text'] = ""
    for ind in df.index:
        df['text'][ind] = "No. of Seats:" + str(df['Seats'][ind]) + '        '+methods[to_use1].title()+' Allocation : ' + str(df[methods[to_use1]][ind]) + '        '+methods[to_use2].title()+' Allocation : ' + str(df[methods[to_use2]][ind]) + "         Quota:" + str(df['Quota'][ind]) + "    Electors:" + str(df['Electors'][ind]) 
        
for x in df_list:
    hover_text(x)

geojson_list = []
for yer in years:
    with open('./Geojson/' + str(yer) + '.json') as f:
        gj = geojson.load(f)
        gj = rewind(gj, rfc7946=False)
    geojson_list.append(gj)

data = []
for i in range(0,len(df_list)):
    temp_data = dict(type='choropleth', 
                    locations = df_list[i]['State/UT'].astype(str),
                    z = df_list[i]['Difference'].astype(str),
                    zmin=color_range[0], zmax=color_range[1],
                    geojson = geojson_list[i],
                    featureidkey='properties.ST_NM',
                    text = df_list[i]['text'],
                    colorscale = [[0, 'rgba(214, 39, 40, 0.85)'],   
                                    [0.5, 'rgba(255, 255, 255, 0.85)'],  
                                    [1, 'rgba(6,54,21, 0.85)']]  
            )
    data.append(temp_data)
    
steps = []
for i in range(len(data)):
	step = dict(method='restyle',args=['visible', [j==i for j in range(len(data))]],label='Year {}'.format(years[i]))
	steps.append(step)

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]
layout = dict(sliders=sliders,geo = dict(fitbounds="locations", visible=False),coloraxis= dict(colorbar=dict(title=dict(font=dict(color="black"),text = "ddfbvghdfkjghfduvhfhdf gfsgfgd fsfgb",side="right"))))

fig = dict(data=data,layout=layout)

# plotly.offline.iplot(fig)
plotly.offline.plot(fig, filename=filepath,auto_open=False)