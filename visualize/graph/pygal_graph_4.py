import pygal
from pygal.style import Style
custom_style = Style(
  colors=('#eaeaea','#1ed65f', '#19a56f', '#42a5f5', '#1e88e5', '#9575cd', '#ff7043', '#ffa725', '#78909c', '#296d8b', '#294d6b'), opacity='.85', opacity_hover='.95')

pie_chart = pygal.Pie(style=custom_style, height=500, legend_at_bottom=True)
pie_chart.title = 'Top 10 Artists of the year (in Steams)'
pie_chart.add('Other Artists', 191416236)
pie_chart.add('The Toys', 8534491)
pie_chart.add('Atom Chanakan', 7194833)
pie_chart.add('BTS', 7148502)
pie_chart.add('BLACKPINK', 6810406)
pie_chart.add('Ed Sheeran', 5794695)
pie_chart.add('Room 39', 5389441)
pie_chart.add('Post Malone', 4247444)
pie_chart.add('Charlie Puth', 4206773)
pie_chart.add('Lauv', 3703832)
pie_chart.add('Lipta', 3429268)

pie_chart.render_to_file('./visualize/graph/graph_4.svg')
