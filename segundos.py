entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = entrada // 86400
horas = (entrada % 86400) // 3600
minutos = ((entrada % 86400) % 3600) // 60
segundos = ((entrada % 86400) % 60) % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")