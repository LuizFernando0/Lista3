+from random import randint

rnd = randint(0, 10)

print("Vou te dar 3 chances de acertar o número hein, vamos lá!")
print()

usr = int(input('Chuta um número de 0 a 10: '))

while usr > 10 or usr < 0:
  print()
  print ("Já disse que é só entre 0 e 10")
  usr = int(input('Nada. Tenta mais uma vez: '))

print("Vish, tu só tem mais duas tentativas hein...")
tr = 2

while tr > 0 and usr != rnd:
  tr = tr - 1
  print()
  usr = int(input('Errado. Tenta de novo vai, confio no seu potencial: '))

  while usr > 10 or usr < 0:
    print()
    print ("Já disse que só vale entre 0 e 10")
    usr = int(input('Última chance, vai lá: '))


if usr == rnd:
  print("Boa! Eu sabia que você iria acertar rs")
else:
  print("Que peninha")

print('O número era:', rnd)
