liste = [1, 2.3, 4.56, 7.890, 12.34, 567.890]

for tall in liste:
    # Formatere tall med width=5 og precision=1 gjør akkurat at tallene
    # kommer under hverandre og med 1 desimal.
    print(f'{tall:5.1f}')