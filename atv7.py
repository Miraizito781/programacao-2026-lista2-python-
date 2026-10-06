temp = 80.0
umid = 10.0
TEMP_REF = 70.0
UMID_REF = 20.0
queimada = (temp >= TEMP_REF) and (umid <= UMID_REF)
print("A temperatura e a umidade atual são favoráveis para ocorrer uma queimada? ", queimada)
