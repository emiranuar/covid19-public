import plotly.express as px
import pandas as pd

daily_cases = pd.read_csv('epidemic/cases_state.csv')
population = pd.read_csv('static/population.csv')

state_pop_dict = {}

for state in population.iterrows():
    if state[0] > 0:
        state_pop_dict[state[1].state] = state[1]['pop']

daily_case_pivoted = daily_cases.pivot(index='date', columns='state', values='cases_new').reset_index()

for x in state_pop_dict:
    daily_case_pivoted[x] = 100*daily_case_pivoted[x]/state_pop_dict[x]
    
fig = px.line(daily_case_pivoted, x="date", y=list(state_pop_dict.keys()))
fig.show()