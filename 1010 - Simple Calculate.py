x=input().split(" ")
y=input().split(" ")

a,b,c= x
d,e,f= y

result=(int(b)*float(c)) + (int(e)* float(f))

print('VALOR A PAGAR: R$ %.2f'%result)
