import datetime

avstand_i_km = float(input('Oppgi avstand i km: '))
fart_i_knop = float(input('Oppgi fart i knop: '))
fart_i_kmpt = fart_i_knop * 1.852
flytid = avstand_i_km / fart_i_kmpt

# Med +, -, *, / og int()
flytid_timer = int(flytid)
flytid_minutter = int((flytid - flytid_timer) * 60)
flytid_sekunder = int((flytid - flytid_timer - (flytid_minutter / 60)) * 3600)

print('Flytiden er på ' + str(flytid_timer) + ' timer ' + str(flytid_minutter) + 
      ' minutter og ' + str(flytid_sekunder) + ' sekunder.')

# Med divmod()
flytid_timer, rest = divmod(flytid, 1)
flytid_minutter, rest = divmod(rest * 60, 1)
flytid_sekunder, rest = divmod(rest * 60, 1)

print('Flytiden er på ' + str(flytid_timer) + ' timer ' + str(flytid_minutter) + 
      ' minutter og ' + str(flytid_sekunder) + ' sekunder.')

# Med datetime
time = datetime.timedelta(hours=flytid)

print('Flytiden er ' + str(time))