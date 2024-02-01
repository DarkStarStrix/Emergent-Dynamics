import numpy as np
import plotly.graph_objects as go

# Parameters
num_individuals, time_steps, chaos_strength, interaction_strength = 1000, 100, 0.1, 0.5

# Initialize individual elements and properties arrays
microscale = np.random.rand(num_individuals)
mesoscale = np.zeros(time_steps)
macroscale = np.zeros(time_steps)

# Simulation
for t in range(1, time_steps):
    microscale += chaos_strength * (np.random.rand(num_individuals) - 0.5)
    mesoscale[t] = np.mean(microscale) + interaction_strength * (np.random.rand() - 0.5)
    macroscale[t] = np.mean(mesoscale[:t]) + interaction_strength * (np.random.rand() - 0.5)

# Create line plots
x = np.arange(time_steps)

fig_micro = go.Figure(data=go.Scatter(x=x, y=microscale, mode='lines'))
fig_micro.update_layout(title='Microscale (Individual Elements)', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig_meso = go.Figure(data=go.Scatter(x=x, y=mesoscale, mode='lines'))
fig_meso.update_layout(title='Mesoscale (Aggregated Properties)', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig_macro = go.Figure(data=go.Scatter(x=x, y=macroscale, mode='lines'))
fig_macro.update_layout(title='Macroscale (Emergent System)', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig_micro.show()
fig_meso.show()
fig_macro.show()

# Create histograms
fig = go.Figure()
fig.add_trace(go.Histogram(x=microscale, name='Microscale', opacity=0.75, nbinsx=50))
fig.add_trace(go.Histogram(x=mesoscale, name='Mesoscale', opacity=0.75, nbinsx=50))
fig.add_trace(go.Histogram(x=macroscale, name='Macroscale', opacity=0.75, nbinsx=50))

# Overlay histograms
fig.update_layout(barmode='overlay', title_text='Histogram Comparison', xaxis_title='Value', yaxis_title='Count')

fig.show()
