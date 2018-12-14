import pygal

pie_chart = pygal.Pie(inner_radius=.75)
pie_chart.title = 'Top 10 Artists of the year (in %)'
pie_chart.add('IE', 19.5)
pie_chart.add('Firefox', 36.6)
pie_chart.add('Chrome', 36.3)
pie_chart.add('Safari', 4.5)
pie_chart.add('Opera', 2.3)

line_chart.render_to_file('./visualize/graph/graph_4.svg')
