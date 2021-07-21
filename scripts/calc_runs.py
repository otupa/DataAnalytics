

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

def calcular_porcentagens(p_valor, p_total):
    p_valor = int(p_valor[2:][:-3])
    
    if p_valor == 10:
        porcent = p_total * 0.10
        porcent = round(porcent, 2)
        return porcent

    elif p_valor <= 20:
        porcent = p_total * 0.15
        porcent = round(porcent, 2)
        return porcent

    elif p_valor >= 20:
        porcent = p_total * 0.20
        porcent = round(porcent, 2)
        return porcent

def calcular_porcentagens_desc(p_valor, p_total):

    p_valor = int(p_valor[3:][:-3])

    if p_valor == 10:
        porcent = p_total * -0.90
        porcent = round(porcent, 2)
        return porcent
    
    elif p_valor <= 20:
        porcent = p_total * -0.85
        porcent = round(porcent, 2)
        return porcent

    elif p_valor >= 20:
        porcent = p_total * -0.80
        porcent = round(porcent, 2)
        return porcent

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

def schema_pesquisa_desc():
    for valor in variaveis_precos_descontos():
        quantidade_viajens = receber_pesquisa_desc().count(valor)
        total_viajens.append(quantidade_viajens)
        mult_total = multiplicar_desc(valor, quantidade_viajens)
        viajens_moto.append(mult_total)
        porcentagem_desc = calcular_porcentagens_desc(valor, mult_total)
        lucro.append(porcentagem_desc)r 
        schema = [
            valor,
            "x "+str(quantidade_viajens)+"  =",
            "R$"+str(mult_total)+",00",
            "R$"+str(porcentagem_desc)
            ]
        lista_master.append(schema)

def schema_pesquisa_total():
    soma_total_viajens = sum(viajens_moto)
    lista_master.append([
        "Total:",
        "x "+str(sum(total_viajens)),
        "R$"+str(soma_total_viajens)+",00",
        "R$"+str(round(sum(lucro), 2))
        ])

    def main():
        schema_pesquisa()
        schema_pesquisa_desc()
        schema_pesquisa_total()
        [self.Resultado.insert("", END, values=info) for info in lista_master]
    main()
    return lista_master
