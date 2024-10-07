segundos = int(input("Informe a qtd de segundos: "))

horas = segundos // 60
resto1 = segundos % 60
minutos = resto1 // 60

if horas >= 24:
	dias = horas // 24
	horas = horas % 24
	print(dias," dias,",horas," horas,",minutos," minutos e", resto1 % 60," segundos.")
else:
	print(horas," horas,",minutos," minutos e", resto1 % 60," segundos.")
