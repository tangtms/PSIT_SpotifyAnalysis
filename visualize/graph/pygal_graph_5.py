import pygal

line_chart = pygal.Line()
line_chart.title = 'Top 5 Artist Analysis (Steams)'
line_chart.x_labels = ["Sep-2017", "Oct-2017", "Nov-2017", "Dec-2017", "Jan-2018", "Feb-2018", "March-2018", "April-2018", "May-2018", "June-2018", "Jul-2018", "Aug-2018"]
line_chart.add('The Toys',  [148038, 158252, 173662, 317829, 286394, 947799, 930720, 845147, 760934, 820052, 488381, 268830])
line_chart.add('Atom Chanakan',  [122923, 104711, 223600, 685558, 662199, 691500, 927766, 688289, 705334, 748211, 639281, 746774])
line_chart.add('BTS',  [1015354, 749997, 277442, 501618, 225552, 155189, 152074, 191116, 870979, 1250168, 475615, 1228445])
line_chart.add('BLACKPINK',  [158709, 140166, 88574, 165420, 151859, 177101, 148703, 55268, 59603, 1523603, 1860023, 1967870])
line_chart.add('Ed Sheeran',  [337860, 467910, 623141, 1003178, 681125, 514297, 461016, 341300, 394812, 404430, 306635, 376767])

line_chart.render_to_file('./visualize/graph/graph_5.svg')
