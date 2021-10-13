'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  ePrim=1
  if n==1 or n==0:
    return False

  for i in range(2,n//2+1):
    if n%i==0:
      ePrim = 0
      return False

  if ePrim:
    return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  p=1
  for i in lst:
    p = p*i
  return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while x!=y:
    if x>y:
      x=x-y
    else:
      y=y-x
  return y
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  r=x%y
  while r>0:
    x=y
    y=r
    r=x%y
  return y

def read_list():
  given = input("Dati numere separate prin virgula:")
  int_list = given.split(',')
  list = []
  for int_lst in int_list:
    list.append(int(int_lst))
  return list


def print_menu():
  print('0.Exit.')
  print('1.Citirea unei liste:')
  print('2.Numar prim:')
  print('3.Produsul a n numere:')
  print('4.Cmmdc_v1:')
  print('5.Cmmdc_v2:')
  
def main():
  # interfata de tip consola aici
  lst = []
  while True:
    print_menu()
    op = input("Alegeti o optiune: ")
    if op == '1':
      lst = read_list()
    if op == '2':
      n = int(input("n = "))
      print(is_prime(n))
    if op == '3':
      print(get_product(lst))
    if op == '4':
      x = int(input("x="))
      y = int(input("y="))
      print(get_cmmdc_v1(x, y))
    if op == '5':
      x = int(input("x="))
      y = int(input("y="))
      print(get_cmmdc_v2(x, y))
    if op == '0':
      break

if __name__ == '__main__':
  main()
