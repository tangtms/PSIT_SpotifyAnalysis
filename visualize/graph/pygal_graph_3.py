import pygal
from pygal.style import Style

gauge = pygal.SolidGauge(
    colors=('#1ed65f', '#1ed65f', '#42a5f5', '#42a5f5', '#42a5f5', '#296d8b', '#296d8b', '#296d8b', '#1ed65f', '#ff7043', '#ff7043', '#ff7043'), half_pie=True, inner_radius=0.70,
    style=pygal.style.styles['default'](value_font_size=10), legend_at_bottom=True, height=500)
gauge.title = 'Artist of the month (In Steams)'

steam_formatter = lambda x: '{:.10g}'.format(x)
gauge.value_formatter = steam_formatter

gauge.add('Sep-2017 ', [{'value': 1015354, 'max_value': 11855136, 'label': 'BTS'}])
gauge.add('Oct-2017', [{'value': 749997, 'max_value': 11792422, 'label': 'BTS'}])
gauge.add('Nov-2017', [{'value': 623141, 'max_value': 12623657, 'label': 'Ed Sheeran'}])
gauge.add('Dec-2017', [{'value': 1003178, 'max_value': 18617400, 'label': 'Ed Sheeran'}])
gauge.add('Jan-2017', [{'value': 681125, 'max_value': 15666801, 'label': 'Ed Sheeran'}])
gauge.add('Feb-2018', [{'value': 947799, 'max_value': 17376363, 'label': 'The Toys'}])
gauge.add('March-2018', [{'value': 930720, 'max_value': 22343773, 'label': 'The Toys'}])
gauge.add('April-2018', [{'value': 845147, 'max_value': 19096768, 'label': 'The Toys'}])
gauge.add('May-2018', [{'value': 870979, 'max_value': 20504672, 'label': 'BTS'}])
gauge.add('June-2018', [{'value': 1523603, 'max_value': 28945824, 'label': 'BLACKPINK'}])
gauge.add('Jul-2018', [{'value': 1860023, 'max_value': 25741811, 'label': 'BLACKPINK'}])
gauge.add('Aug-2018', [{'value': 1967870, 'max_value': 33877021, 'label': 'BLACKPINK'}])

gauge.render_to_file('./visualize/graph/graph_3.svg')
