import pygal

line_chart = pygal.Line()
line_chart.title = 'Thai music and International music analysis (Steams)'
line_chart.x_labels = ["Sep-2017", "Oct-2017", "Nov-2017", "Dec-2017", "Jan-2018", "Feb-2018", "March-2018", "April-2018", "May-2018", "June-2018", "Jul-2018", "Aug-2018"]
line_chart.add('Thai Music',  [65, 57, 70, 82, 84, 93, 102, 78, 83, 85, 81, 88])
line_chart.add('International Music',  [207, 187, 196, 199, 172, 161, 184, 189, 181, 196, 179, 199])

line_chart.render_to_file('./visualize/graph/graph_6.svg')
