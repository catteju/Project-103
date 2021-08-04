from re import X
import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("Covid.csv")

fig = px.scatter(df, x = "date", y = "cases", title = " Covid - 19", color = "country")
fig.show()