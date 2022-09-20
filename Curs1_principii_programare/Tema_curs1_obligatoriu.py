# EXERCITUL 1
# O variabila este o cutie in care putem pune spre pastrare anumite lucruri
# O zona de memorie careia ii dam un nume si care poate depozita anumite valori/date

# EXERCITUL 2
nume = "Adrian"
nr_bon_ordine = 23
pi = 3.14159
sunt_din_vrancea = True

# EXERCITIUL 3
print(type(nume))
print(type(nr_bon_ordine))
print(type(pi))
print(type(sunt_din_vrancea))

# EXERCITIUL 4
pi = round(pi)
print(type(pi))

# EXERCITIUL 5
print(f"Salut! Numele meu este {nume}. Am bonul de ordine cu numaru {nr_bon_ordine}."
      f" Imi place constanta {pi} si este {sunt_din_vrancea} faptul ca sunt din Vrancea.")

# EXERCITIUL 6
nume = input("Te rog sa introduci numele tau mai jos:\n")
prenume = input("Te rog sa introduci prenumele tau mai jos\n")
full_name = nume + prenume
length_full_name = len(full_name) - full_name.count(' ')
# asa rezolvam problema cu userul care poate are 2 sau mai multe prenume separate de spatiu
print(f"Numele tau complet are {length_full_name} caractere")

# EXERCITIUL 7
lungime_dreptunghi = int(input("Te rog sa introduci lungimea dreptunghiului:\n"))
latime_dreptunghi = int(input("Te rog sa introduci latimea dreptunghiului:\n"))
arie_dreptunghi = lungime_dreptunghi * latime_dreptunghi
print(f'Aria dreptunghiului este {arie_dreptunghi}.')

# EXERCITIUL 8 si 9
string_dat = "Coral is either the stupidest animal or the smartest rock"
string_dat = string_dat.split()  # daca nu este splitat va numara 3 deoarece il pune si pe cel din either
the_count = string_dat.count("the")
print(the_count)
# am afalt ca merge si varianta cu spatiu inainte " the " fara sa mai fac split

# EXERCITIUL 10
assert string_dat.isnumeric() == True  # fara true, e conditie care se evalueaza ca True or False
print("Stringul contine doar numere")
