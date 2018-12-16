import pygal
from pygal.style import Style
custom_style = Style(
  colors=('#1ed65f',))

line_chart = pygal.Line(style=custom_style, legend_at_bottom=True, height=500, max_scale=10, width=650)
line_chart.title = 'Stream Count Monthly (Sep2017 - Aug2018)'
line_chart.x_labels = ["Sep-2017", "Oct-2017", "Nov-2017", "Dec-2017", "Jan-2018", "Feb-2018", "March-2018", "April-2018", "May-2018", "June-2018", "Jul-2018", "Aug-2018"]
line_chart.add('Stream',  [11855136, 11792422, 12623657, 18617400, 15666801, 17376363, 22343773, 19096768, 20504672, 28945824, 25741811, 33877021])

line_chart.render_to_file('./visualize/graph/graph_2.svg')
