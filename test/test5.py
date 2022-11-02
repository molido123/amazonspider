import re
text="""re.findall("/dp/([a-z-A-Z-0-9]*)","https://www.amazon.com/HP-Computer-Quad-Core-Keyboard-Bluetooth/dp/B09YXBCXS9/ref=sr_1_15?keywords=computer&qid=1667139045&qu=eyJxc2MiOiI5LjI5IiwicXNhIjoiOC40NiIsInFzcCI6IjguMTAifQ%3D%3D&sr=8-15")"""
print(re.findall("\n(\$[0-9]*.[0-9]*)", "\ndadada\nd321asdas\n$21.2\dasdasdas"))
