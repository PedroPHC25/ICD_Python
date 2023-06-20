from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np
from bokeh.models import Range1d

"""
df = pandas.read_csv("arquivo.csv")

x = df["col1"]
y = df["col2"]

output_file("line_plot_from_csv.html")

figure = figure()

figure.line(x, y)
# figure.circle(x, y)
# figure.triangle(x, y)

# save(figure)
show(figure)
"""
"""
2 e 3
petal length (cm)
petal width (cm)
"""


iris = datasets.load_iris()
# print(list(iris.keys()))
# print(list(iris["feature_names"]))
# print(iris.data)

x = iris.data[:, 2:3]
y = iris.data[:, 3:4]
# print(type(x))
# print(y)

x_flat = list(np.concatenate(x))
y_flat = list(np.concatenate(y))

# print(type(x_flat))
# print(x_flat)

output_file("iris.html")

figure = figure()
figure.circle(x_flat, y_flat)

# figure.plot_width = 1280
# figure.plot_height = 720

figure.background_fill_color = (255, 250, 250, 0.9)
# figure.background_fill_alpha = 0.9


figure.title.text = "Correlação comprimento-largura"
figure.title.text_color = "DeepPink"
figure.title.text_font = "fantasy"
figure.title.text_font_size = "42px"
figure.title.align = "center"

figure.xaxis.axis_label = "Petal length (cm)"
figure.yaxis.axis_label = "Petal width (cm)"
figure.xaxis.minor_tick_line_color = "green"
figure.yaxis.minor_tick_line_color = "green"
figure.xaxis.minor_tick_in = 15
figure.yaxis.minor_tick_in = 15
figure.xaxis.major_label_orientation = "vertical"
figure.yaxis.major_label_orientation = "vertical"

# figure.xaxis.visible = False
# figure.yaxis.visible = False

figure.axis.axis_label_text_color = "blue"
figure.axis.major_label_text_color = "orange"


figure.xaxis.bounds = (0, 2)
figure.yaxis.bounds = (1, 3)

figure.x_range = Range1d(start = 0, end = 10)
figure.y_range = Range1d(start = 0, end = 5)

figure.xaxis[0].ticker.desired_num_ticks = 2
figure.yaxis[0].ticker.desired_num_ticks = 2

figure.xaxis[0].ticker.num_minor_ticks = 10
figure.yaxis[0].ticker.num_minor_ticks = 10

# figure.xgrid.grid_line_color = None
# figure.ygrid.grid_line_color = None

figure.xgrid.grid_line_color = "DeepPink"
figure.ygrid.grid_line_color = "DeepPink"

# figure.xgrid.grid_line_alpha = 0.13
# figure.ygrid.grid_line_alpha = 0.42

# figure.grid.grid_line_dash = [1, 42]
figure.grid.grid_line_dash = "dashdot"


show(figure)


































