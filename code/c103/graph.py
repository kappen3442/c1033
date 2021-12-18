import pandas as pd
import plotly.express as px

df=pd.read_csv('line_chart.csv')
#figure=px.bar(df,x="Year",y="Per capita income")
#figure=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
figure=px.line(df,x="Year",y="Per capita income",color="Country")
figure.show()