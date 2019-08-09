<h1>Build a heat map of unemployment rate in USA</h1>
<p>You can easily build a heat map of US counties. The output file in svg format. You can change data, colors, distribution groups.</p>
<h2>Settings</h2>

* to change colors: edit 'colors' list
* to change groups: add or delete conditions in 'for p in paths:' loop

* 'unemployment09.csv' used for data, 9nth colomn for unemployment rate, 2 and 3 column for FIPS id
* 'counties.svg' used for the base map of USA counties (src: https://commons.wikimedia.org/wiki/File:USA_Counties_with_FIPS_and_names.svg)

<h2>Usage</h2>

* clone or download heat_map_python repo
* navigate to repo using terminal
* run 'python color_map.py'
