import pygal

piechart = pygal.Pie()

piechart.title='Number of Inhabitants in Neighbourhoods'

piechart.add('Muea', 102 ),
piechart.add('Fiango', 3500 ),
piechart.add('Kosala', 507),
piechart.add('Soa', 869 ),
piechart.add('Bambili', 603 ),
piechart.add('Dirty South', 5000 ),
piechart.add('Bonaberi', 2700),
piechart.add('Mokolo', 4002 ),
piechart.add('Bokwango', 1200 ),
piechart.add('Bokwai', 52)

iechart.render()
