import pygal
pie_chart = pygal.Pie(inner_radius=.4)
pie_chart.title = 'Thai music/ International music ratio (in %)'

pie_chart.add('Thai Music', 40.48192771084337)
pie_chart.add('International Music', 59.51807228915663)

pie_chart.render_to_file('./visualize/pygal_pie_thai_national_ratio.svg')