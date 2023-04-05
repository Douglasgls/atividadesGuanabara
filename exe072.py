T_num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

num = int(input('digite um num: '))


while True:
    if num >20 or num <0:
        num = int(input('digite um num entre 0 e 20: '))
    else:
        break

print(f'voce digitou {num} em estenso é {T_num[num]}')