import pygal
from pygal.style import Style
custom_style = Style(
  colors=('#1ed65f', '#181717'), opacity='.85', opacity_hover='.95')

pie_chart = pygal.Pie(style=custom_style, inner_radius=.4, legend_at_bottom=True)
pie_chart.title = 'Thai music/ International music ratio (in %)'

steam_formatter = lambda x: '{:.10g}%'.format(x)
pie_chart.value_formatter = steam_formatter

pie_chart.add('Thai Music', 40.481)
pie_chart.add('International Music', 59.518)

pie_chart.render_to_file('./visualize/graph/graph_1.svg')