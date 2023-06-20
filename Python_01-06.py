from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np
from bokeh.models import ColumnDataSource

"""
output_file("exemplo4.html")

plot = figure(width = 640, height = 480, tools = "box_zoom, pan, reset, save, wheel_zoom")

renderer = plot.circle([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], legend_label = "Sei lá")

plot.toolbar.logo = None
plot.toolbar.autohide = True
plot.toolbar_location = "below"

plot.legend.location = "top_left"
plot.legend.background_fill_alpha = 0
plot.legend.border_line_color = None
# plot.legend.padding = 42
plot.legend.label_text_color = "cyan"
plot.legend.label_text_font = "times"

glyph_renderer = renderer.glyph

glyph_renderer.size = 42
glyph_renderer.fill_alpha = 0.13
glyph_renderer.line_color = "gold"
glyph_renderer.line_width = 2
glyph_renderer.line_dash = [7, 3]

show(plot)
"""


output_file("exemplo5.html")

raw_data = {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}

data_source = ColumnDataSource(data = raw_data)
plot = figure()

new_data = [3, 6, 9, 12, 15]

data_source.data["extra"] = new_data

data_source.patch({"x": [(0, 10)]})

plot.circle(x = "x", y = "extra", source = data_source)

show(plot)