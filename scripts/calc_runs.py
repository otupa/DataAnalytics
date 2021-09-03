

def receber_pesquisa():
    lista_resultados = [
        item[3] for item in lista if item[3][:1] == "R"]
    return lista_resultados

def receber_pesquisa_desc():
    lista_descontos = [
        item[3] for item in lista if item[3][:1] == "D"]
    return lista_descontos

def variaveis_precos():
    lista_valor = [
        item for item in receber_pesquisa() if item not in lista_valor]
    lista_valor = sorted(lista_valor)
    return lista_valor

def variaveis_precos_descontos():
    lista_valor_desc = [
        item for item in receber_pesquisa_desc(
        ) if item not in lista_valor_desc]
    lista_valor_desc = sorted(lista_valor_desc)
    return lista_valor_desc

def multiplicar(valor, quantidade):
    total_mult = int(valor[2:][:-3]) * quantidade
    return total_mult

def multiplicar_desc(valor, quantidade):
    total_mult = int(valor[3:][:-3]) * quantidade
    return total_mult

def schema_pesquisa():
    for valor in variaveis_precos():
        quantidade_viajens = receber_pesquisa().count(valor)
        total_viajens.append(quantidade_viajens)
        mult_total = multiplicar(valor, quantidade_viajens)
        viajens_moto.append(mult_total)
        porcentagem = calcular_porcentagens(valor, mult_total)
        lucro.append(porcentagem)
        schema = [
            valor,                                 
            "x "+str(quantidade_viajens)+"  =",    
            "R$"+str(mult_total)+",00",            
            "R$"+str(porcentagem)                  
            ]
        lista_master.append(schema)
