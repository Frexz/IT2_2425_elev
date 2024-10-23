def harm_gjsn(verdier):
    sum_invers = 0
    for verdi in verdier:
        sum_invers += 1/verdi
    return round(len(verdier) / sum_invers, 1)

# Test
assert harm_gjsn([50, 100]) == 66.7
assert harm_gjsn([5, 15, 25]) == 9.8

print("Testen er bestått!")