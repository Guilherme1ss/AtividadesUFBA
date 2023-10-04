segundosTotais = int(input())
horas = segundosTotais//3600
minutos = (segundosTotais%3600)//60
segundos = (segundosTotais%3600)%60
print(f'{horas}h {minutos}m {segundos}s')