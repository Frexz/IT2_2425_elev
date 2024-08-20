tall = 13

# Her brukes ':' etter tall-variabelen for å formatere.

# Skriv ut tallet binært
print(f'Tallet {tall} er {tall:b} binært.')

# Skriv ut tallet hexadesimalt
print(f'Tallet {tall} er {tall:x} hexadesimalt.')

verdier = [1.1, 22.22, 333.333]

for tall in verdier:
    # Utskriften har 10 symboler (tallene pluss mellomrom).
    # Tallet etter '.' angir hvor mange desimaler tallet skrives ut med.
    print(f'{tall:10.2f}')

# Runder av tall
tall = 1/3
print(round(tall, 2)) # 0.33