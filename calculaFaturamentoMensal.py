
SP = 6783643
RJ = 3667866
MG = 2922988
ES = 2716548
Outros = 1984953

faturamento = 0
total_percentual = 100

def calculaPercentualSp():
    faturamento = SP+RJ+MG+ES+Outros
    calculaSp = "Percentual de SP: " , (SP * total_percentual) / faturamento
    return calculaSp
def calculaPercentualRj():
    faturamento = SP+RJ+MG+ES+Outros
    calculaRj = "Percentual de RJ: " , (RJ * total_percentual) / faturamento
    return calculaRj
def calculaPercentualMg():
    faturamento = SP+RJ+MG+ES+Outros
    calculaMg = "Percentual de MG: " , (MG * total_percentual) / faturamento
    return calculaMg
def calculaPercentualEs():
    faturamento = SP+RJ+MG+ES+Outros
    calculaEs = "Percentual de ES: " , (ES * total_percentual) / faturamento
    return calculaEs
def calculaPercentualOutros():
    faturamento = SP+RJ+MG+ES+Outros
    calculaOutros = "Percentual de Outros: " , (Outros * total_percentual) / faturamento
    return calculaOutros
  
#print(calculaPercentualRj())
print(calculaPercentualEs())