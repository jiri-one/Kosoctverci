def mocniny(n):
    mocny_slovnik = {}
    for cislo in range(1,n+1):
        mocny_slovnik[cislo] = cislo * cislo
    return mocny_slovnik

# testy
print(mocniny(4))
print(mocniny(10))


