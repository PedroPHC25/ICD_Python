from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np
from bokeh.models import Range1d

grafico = figure()

output_file("grafico.html")

x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
y = [694252, 829991, 839998, 807516, 812326, 876034, 413668, 956887]

grafico.line(x, y, line_width = 3)

grafico.title.text = "Histórico da produção de uva no RS"
grafico.title.text_color = "purple"
grafico.title.text_font = "helvetica"
grafico.title.text_font_size = "20px"
grafico.title.align = "center"

grafico.xaxis.axis_label = "Ano"
grafico.yaxis.axis_label = "Produção em toneladas"
grafico.axis.axis_label_text_color = "purple"

grafico.xaxis[0].ticker.num_minor_ticks = 0
grafico.background_fill_color = "#D09DE0"
grafico.background_fill_alpha = 0.05

grafico.xaxis.minor_tick_line_color = "blue"
grafico.yaxis.minor_tick_line_color = "blue"

grafico.xaxis.major_label_text_color = "#6E2E82"
grafico.yaxis.major_label_text_color = "#6E2E82"

grafico.grid.grid_line_dash = [1, 3]

grafico.xgrid.grid_line_color = "#C565E6"
grafico.ygrid.grid_line_color = "#C565E6"

grafico.xgrid.grid_line_alpha = 0.5
grafico.ygrid.grid_line_alpha = 0.5

grafico.yaxis[0].formatter.use_scientific = False

show(grafico)