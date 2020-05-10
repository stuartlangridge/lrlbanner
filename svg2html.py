#!/usr/bin/env python3

from xml.dom import minidom
import json


with open("map.svg") as fp:
    dom = minidom.parseString(fp.read())
with open("names.json") as fp:
    names = json.load(fp)

l, t, r, b = [float(x) for x in dom.getElementsByTagName("svg")[0].getAttribute("viewBox").split()]
w = r - l
h = b - t
recthtml = []
for r in dom.getElementsByTagName("rect"):
    left = ((float(r.getAttribute("x")) - l) / w) * 100
    top = ((float(r.getAttribute("y")) - t) / h) * 100
    width = (float(r.getAttribute("width")) / w) * 100
    height = (float(r.getAttribute("height")) / h) * 100
    id = r.getAttribute("id").replace("rect", "")
    html = '''<a href="{}" draggable="false" style="top: {:0.2f}%; left: {:0.2f}%; width: {:0.2f}%; height: {:0.2f}%"
        id="{}" data-name="{}"></a>'''.format(names.get(id, {}).get("url", "#"),
            top, left, width, height, id,
            names.get(id, {}).get("name", "???"))
    recthtml.append(html)

namehtml = []
byname = sorted([(names[id]["name"], id) for id in names], key=lambda x:x[0].lower())
for name, id in byname:
    namehtml.append('<a href="#{}" data-id="{}">{}</a>'.format(id, id, name))

out = """<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LugRadio Live 2009 banner</title>
<link href="lrl.css" rel="stylesheet">
</head><body>
<header>
    <p><strong>The LugRadio Live 2009 banner!</strong> Help Stuart annotate this list!
    If you know any of the names who aren't listed here,
    reply to this tweet with the location (the number you get when mousing over a name).
</header>
<article>
<figure>
    <img src="banner.jpg" draggable="false">
    <div>
        {}
    </div>
</figure>
</article>
<footer>Names already identified: {}</footer>
<script src="lrl.js"></script>
</body></html>""".format("\n".join(recthtml), ", ".join(namehtml))
with open("lrlbanner.html", encoding="utf-8", mode="w") as fp:
    fp.write(out)
