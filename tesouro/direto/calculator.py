
# jaa1 = 0.1116
jaa = 0.1116
jaa = 0.10

days = [
    121,
    247,
    370,
    500,
    622,
    753,
    875,
    1003,
    1127,
    1254
]

price = 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(121/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(247/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(370/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(500/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(622/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(753/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(875/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(1003/252)))
price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(1127/252)))
price += 1000 * ((1.10**0.5)) * (1/((1+jaa)**(1254/252)))

print price

price = 0
for day in days[:-1]:
    price += 1000 * ((1.10**0.5)-1) * (1/((1+jaa)**(day/252)))
price += 1000 * ((1.10**0.5)) * (1/((1+jaa)**(days[-1]/252)))

print price


jsm = (1+jaa)**0.5 - 1
cupom = 1000 * jsm

print cupom
