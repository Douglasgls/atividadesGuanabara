import math
from math import sqrt


cat1 = float(input('cateto1: '))

cat2 = float(input('cateto2: '))


# formula = hip**2 = cat1 **2 + cat2 **2 

hipotenusa = cat1**2 + cat2**2


valor_final = math.sqrt(hipotenusa)



print(f'{valor_final} valor da Hipotenusa')
