<h1>Build a heat map of unemployment rate in USA</h1>
<p>You can easily build a heat map of US counties. The output file in svg format. You can change data, colors, distribution groups.</p>
<h2>Settings</h2>

* to change colors: edit _colors_ list
* to change groups: add or delete conditions in _for p in paths:_ loop

* _unemployment09.csv_ used for data, 9nth colomn for unemployment rate, 2 and 3 column for FIPS id
* _counties.svg_ used for the base map of USA counties (src: https://commons.wikimedia.org/wiki/File:USA_Counties_with_FIPS_and_names.svg)

<h2>Installation</h2>

* clone or download _heat_map_python_ repo
* navigate to repo using terminal

<h3>Install the requirements</h3>

* install the requirements using pip install -r _requirements.txt_.
  * make sure you use Python 3.
  * you may want to use a virtual environment for this.

<h2>Usage</h2>

* run _python color_map.py_
