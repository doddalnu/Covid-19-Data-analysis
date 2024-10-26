import pandas as pd
import plotly.express as px

# Load the data
final_df = pd.read_csv('./transformed_data.csv')

# Visualization 1: Scatter plot for Cumulative Cases over Time
values1 = ['India', 'United States of America', 'China']
graph1_data = final_df[final_df['Country'].isin(values1)]

fig1 = px.scatter(
    graph1_data, x='Date_reported', y='Cumulative_cases', color='Country',
    labels={'Cumulative_cases': 'Cumulative Cases'},
    title='Cumulative Cases Over Time'
)

# Save the scatter plot for Cumulative Cases over Time as an image file
fig1.write_image("scatter_plot.png")