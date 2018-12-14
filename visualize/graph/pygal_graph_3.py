import pygal

line_chart = pygal.Line()
line_chart.title = 'Stream count monthly'
line_chart.x_labels = map(str, range(10, 20))
line_chart.add('Stream',  [3688394, 3121660, 3944840, 4530976, 4582436, 5134192, 5708459, 5732742, 6545542, 7545336, 7659390, 8636828, 9434273])
line_chart.render()

line_chart.render_to_file('./visualize/graph/graph_2.svg')
