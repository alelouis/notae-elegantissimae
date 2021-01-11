def symbol(d_map, n):
    symb = '<g transform="translate(25,0)" stroke="black" stroke-linecap="round" stroke-width="4">'
    tho, r = n//1000, n%1000
    hun, r = r//100, r%100
    ten, r = r//10, r%10
    unit = r
    if unit != 0:
        symb += f'<g transform="scale (1, 1)" transform-origin="50">\
        {d_map[unit-1]}</g>'
    if ten != 0:
        symb += f'<g transform="scale (-1, 1)" transform-origin="50">\
        {d_map[ten-1]}</g>'
    if hun != 0:
        symb += f'<g transform="scale (1, -1)" transform-origin="50">\
        {d_map[hun-1]}</g>'
    if tho != 0:
        symb += f'<g transform="scale (-1, -1)" transform-origin="50">\
        {d_map[tho-1]}</g>'
    symb += '</g>'
    return symb