from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.sampledata.periodic_table import elements
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation

# Exemplo 6

pd.set_option("display.max_columns", None)

"""
print(elements.head())
print(elements.count())
print(elements)
"""

elements.dropna(inplace = True)

"""
print(elements.head())
print(elements.count())
print(elements)
"""

color_dict = {"gas":"blue", "liquid": "orange", "solid": "gray"}

colors = []

for each_element in elements["standard state"]:
    colors.append(color_dict[each_element])

elements["size"] = elements["van der Waals radius"] / 10
elements["color"] = colors

"""
print(elements.head())
print(elements.count())
print(elements)
"""

gas = ColumnDataSource(elements[elements["standard state"] == "gas"])
liquid = ColumnDataSource(elements[elements["standard state"] == "liquid"])
solid = ColumnDataSource(elements[elements["standard state"] == "solid"])

output_file("periodic_table.html")

plot = figure()

plot.xaxis.axis_label = "Atomic radius"
plot.yaxis.axis_label = "Boiling point"

plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "color", fill_alpha = 0.13, legend_label = "Gas", source = gas)
plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "color", fill_alpha = 0.13, legend_label = "Liquid", source = liquid)
plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "color", fill_alpha = 0.13, legend_label = "Solid", source = solid)

# show(plot)


# Exemplo 9

output_file("grid_plot.html")

x = list(range(0, 11))
y = list(range(10, 21))

plot1 = figure(width = 240, height = 240, title = "Circle Glyphs")
plot1.circle(x, y, size = 13, color = "OrangeRed", alpha = 0.42)

plot2 = figure(width = 240, height = 240, title = "Triangle Glyphs")
plot2.triangle(x, y, size = 13, color = "Fuchsia", alpha = 0.42)

span_annotation = Span(location = 13, dimension = "width", line_color = "DeepPink", line_width = 3)
plot2.add_layout(span_annotation)

plot3 = figure(width = 240, height = 240, title = "Square Glyphs")
plot3.square(x, y, size = 13, color = "SeaGreen", alpha = 0.42)

box_annotation = BoxAnnotation(left = 3, right = 7, fill_color = "DeepPink", fill_alpha = 0.42)
plot3.add_layout(box_annotation)

plot = gridplot([[plot1, plot2], [None, plot3]])
show(plot)
























