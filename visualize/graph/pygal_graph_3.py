import pygal

gauge = pygal.SolidGauge(
    half_pie=True, inner_radius=0.70,
    style=pygal.style.styles['default'](value_font_size=10))
gauge.title = 'Artist of the month (In Steams)'

steam_formatter = lambda x: '{:.10g}'.format(x)
gauge.value_formatter = steam_formatter

gauge.add('Sep-2017 BTS', [{'value': 1015354, 'max_value': 11855136}])
gauge.add('Oct-2017 BTS', [{'value': 749997, 'max_value': 11792422}])
gauge.add('Nov-2017 Ed Sheeran', [{'value': 623141, 'max_value': 12623657}])
gauge.add('Dec-2017 Ed Sheeran', [{'value': 1003178, 'max_value': 18617400}])
gauge.add('Jan-2017 Ed Sheeran', [{'value': 681125, 'max_value': 15666801}])
gauge.add('Feb-2018 The Toys', [{'value': 947799, 'max_value': 17376363}])
gauge.add('March-2018 The Toys', [{'value': 930720, 'max_value': 22343773}])
gauge.add('April-2018 The Toys', [{'value': 845147, 'max_value': 19096768}])
gauge.add('May-2018 BTS', [{'value': 870979, 'max_value': 20504672}])
gauge.add('June-2018 BLACKPINK', [{'value': 1523603, 'max_value': 28945824}])
gauge.add('Jul-2018 BLACKPINK', [{'value': 1860023, 'max_value': 25741811}])
gauge.add('Aug-2018 BLACKPINK', [{'value': 1967870, 'max_value': 33877021}])

gauge.render_to_file('./visualize/graph/graph_3.svg')
