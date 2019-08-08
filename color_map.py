import csv
from bs4 import BeautifulSoup

unemployment = {}
min_value = 100; max_value = 0 #
reader = csv.reader(open('unemployment09.csv'), delimiter=",")
for row in reader:
    try:
        full_fips = row[1] + row[2]
        rate = float(row[8].strip())
        unemployment[full_fips] = rate
       # print(unemployment)
    except:
        pass

svg = open('counties.svg', 'r').read()
#content.replace('FIPS_', '')
soup = BeautifulSoup(svg, 'html.parser') #selfClosingTags=['defs', 'sodipodi:namedview'])
#soup = BeautifulSoup(svg, selfClosingTags=['defs', 'sodipodi:namedview'])  #BeautifulSoup(markup, "lxml-xml") BeautifulSoup(markup, "xml")

paths = soup.findAll('path')
#print(paths['id'][5:])
#pam='FIPS_'
#paths['id'] = replace_with('')
#print(paths)
colors = ["#eff3ff", "#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c"]

path_style = """font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"""
#paths['id'][5:]
for p in paths:
 #   print(p['id'])
    if p['id'] not in ["State_Lines", "separator"]:
        # pass
        try:
            rate = unemployment[p['id'][5:]]
            #print(rate)
            #print(unemployment[p])
        except:
            #print("it's a mistake")
            continue
        #print(p['id'])

        if rate > 10:
            color_class = 5
        elif rate > 8:
            color_class = 4
        elif rate > 6:
         color_class = 3
        elif rate > 4:
            color_class = 2
        elif rate > 2:
            color_class = 1
        else:
            color_class = 0

        color = colors[color_class]
        p['style'] = path_style + color
        #print(p)

output = soup.prettify()
open('output.svg', 'w').write(output)
#print(soup.prettify())
