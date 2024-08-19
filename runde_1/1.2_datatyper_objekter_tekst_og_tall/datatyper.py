avstand_i_km = input('Oppgi avstand i km: ')
fart_i_knop = input('Oppgi fart i knop: ')
fart_i_kmpt = fart_i_knop * 1.852
flytid = avstand_i_km / fart_i_kmpt
print(flytid)