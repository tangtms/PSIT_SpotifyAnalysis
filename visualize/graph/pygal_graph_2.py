import pygal

line_chart = pygal.Line()
line_chart.title = 'Stream Count Monthly'
line_chart.x_labels = ["Sep-2017", "Oct-2017", "Nov-2017", "Dec-2017", "Jan-2018", "Feb-2018", "March-2018", "April-2018", "May-2018", "June-2018", "Jul-2018", "Aug-2018", "Sep-2018"]
line_chart.add('Stream',  [3688394, 3121660, 3944840, 4530976, 4582436, 5134192, 5708459, 5732742, 6545542, 7545336, 7659390, 8636828, 9434273])
line_chart.render()

line_chart.render_to_file('./visualize/graph/graph_2.svg')
