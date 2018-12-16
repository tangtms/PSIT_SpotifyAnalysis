import pygal
from pygal.style import Style
custom_style = Style(
  colors=('#1ed65f', '#181717'), opacity='.85', opacity_hover='.95')

line_chart = pygal.StackedBar(style=custom_style, legend_at_bottom=True, height=500)
line_chart.title = 'Thai music and International music analysis (in %)'

steam_formatter = lambda x: '{:.10g}%'.format(x)
line_chart.value_formatter = steam_formatter

line_chart.x_labels = ["Sep-2017", "Oct-2017", "Nov-2017", "Dec-2017", "Jan-2018", "Feb-2018", "March-2018", "April-2018", "May-2018", "June-2018", "Jul-2018", "Aug-2018"]
line_chart.add('Thai Music',  [31.400, 30.481, 35.025, 41.919, 48.837, 56.790, 55.434, 40.526, 45.856, 43.367, 45.251, 45.685])
line_chart.add('International Music',  [68.599, 69.518, 64.974, 58.080, 51.162, 43.209, 44.565, 59.473, 54.143, 56.632, 54.748, 54.314])

line_chart.render_to_file('./visualize/graph/graph_6.svg')
