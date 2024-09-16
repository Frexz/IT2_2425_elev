import requests

url = 'https://hotell.difi.no/download/statens-satser/utland/2019'
r = requests.get(url)

# Skriver ut Response-objektet
print(r)
# Skriver ut de 60 første bytene
print(r.content[:60])
# Skriver ut de 74 første tegnene, med beste tilpassede encoding (utf-8)
print(r.text[:74])