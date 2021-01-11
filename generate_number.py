import digits as d
import symbol as s

init = '<?xml version="1.0" standalone="no"?>\
<svg width="150" height="150" version="1.1" xmlns="http://www.w3.org/2000/svg">\
<line x1="75" x2="75" y1="2" y2="148" stroke="black" stroke-linecap="round" stroke-width="4"/>\
%s\</svg>'

d_map = [d.one(), d.two(), d.three(), d.four(), d.five(), 
        d.six(), d.seven(), d.eight(), d.nine()]

n = 1845
with open('out.svg', 'w') as f:
    f.write(init%(s.symbol(d_map, n)))