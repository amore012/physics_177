import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
x = np.random.randn(500)
data = Data([
    Histogram(
        x=x
        )
    ])
plot_url = py.plot(data, filename='test')