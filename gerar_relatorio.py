import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Carregar dados
arquivo = r'D:\Users\diego.b.silva\Desktop\Projeto_MaquinasPesadas\ProjetoCusto_MaquinasPesadas.xlsx'

df_manutencao = pd.read_excel(arquivo, sheet_name='Custo Manutenção')
df_diesel = pd.read_excel(arquivo, sheet_name='Custo Diesel')
df_disponibilidade = pd.read_excel(arquivo, sheet_name='Disponibilidade')
df_frota = pd.read_excel(arquivo, sheet_name='Frota')

print("="*100)
print("RELATORIO DE ANALISE - PROJETO MAQUINAS PESADAS")
print("="*100)

# 1. INVESTIMENTO
print("\n" + "="*100)
print("1. INVESTIMENTO EM AQUISICAO")
print("="*100)

investimento_total = df_frota['Valor de aquisição'].sum()
print(f"\nInvestimento Total: R$ {investimento_total:,.2f}")

print("\nDetalhamento por Equipamento:")
equipamentos_adquiridos = df_frota[df_frota['Valor de aquisição'].notna()].copy()
for idx, row in equipamentos_adquiridos.iterrows():
    print(f"  {row['Função']:20s} - {row['Marca / Modelo']:40s} = R$ {row['Valor de aquisição']:,.2f}")

# 2. CUSTOS OPERACIONAIS
print("\n" + "="*100)
print("2. CUSTOS OPERACIONAIS (Jun-Dez 2026)")
print("="*100)

df_custos = df_manutencao.copy()
df_custos['Custo_Manutencao_Total'] = df_custos['Custo Materiais'].fillna(0) + df_custos['Custo Serviços'].fillna(0)
df_custos = df_custos.merge(df_diesel[['Data', 'Custo Total/Mês']], on='Data', how='left')
df_custos.rename(columns={'Custo Total/Mês': 'Custo_Diesel'}, inplace=True)
df_custos['Custo_Diesel'] = df_custos['Custo_Diesel'].fillna(0)
df_custos['Custo_Total_Mensal'] = df_custos['Custo_Manutencao_Total'] + df_custos['Custo_Diesel']

df_custos_validos = df_custos[df_custos['Custo_Total_Mensal'] > 0].copy()

print(f"\nPeriodo de Analise: {df_custos_validos['Mês'].min()} a {df_custos_validos['Mês'].max()}")
print(f"Meses com Dados: {len(df_custos_validos)}")

print("\nResumo de Custos:")
print(f"  Custo Materiais Total:   R$ {df_custos_validos['Custo Materiais'].sum():,.2f}")
print(f"  Custo Servicos Total:    R$ {df_custos_validos['Custo Serviços'].sum():,.2f}")
print(f"  Custo Diesel Total:      R$ {df_custos_validos['Custo_Diesel'].sum():,.2f}")
print(f"  Custo Operacional Total: R$ {df_custos_validos['Custo_Total_Mensal'].sum():,.2f}")

print("\nMedias Mensais:")
custo_mensal_medio = df_custos_validos['Custo_Total_Mensal'].mean()
print(f"  Custo Materiais Medio:   R$ {df_custos_validos['Custo Materiais'].mean():,.2f}/mes")
print(f"  Custo Servicos Medio:    R$ {df_custos_validos['Custo Serviços'].mean():,.2f}/mes")
print(f"  Custo Diesel Medio:      R$ {df_custos_validos['Custo_Diesel'].mean():,.2f}/mes")
print(f"  Custo Operacional Medio: R$ {custo_mensal_medio:,.2f}/mes")

total_custos = df_custos_validos['Custo_Total_Mensal'].sum()
perc_materiais = (df_custos_validos['Custo Materiais'].sum() / total_custos) * 100
perc_servicos = (df_custos_validos['Custo Serviços'].sum() / total_custos) * 100
perc_diesel = (df_custos_validos['Custo_Diesel'].sum() / total_custos) * 100

print("\nComposicao dos Custos:")
print(f"  Materiais: {perc_materiais:.1f}%")
print(f"  Servicos:  {perc_servicos:.1f}%")
print(f"  Diesel:    {perc_diesel:.1f}%")

# 3. DISPONIBILIDADE
print("\n" + "="*100)
print("3. DISPONIBILIDADE OPERACIONAL")
print("="*100)

equipamentos = ['Escavadeira', 'Pá Carregadeira', 'Varredeira', 'Caminhão Munck', 'Caminhão Pipa 1/2']
df_disp_validos = df_disponibilidade[df_disponibilidade['Escavadeira'].notna()].copy()

print(f"\nPeriodo: {df_disp_validos['Mês'].min()} a {df_disp_validos['Mês'].max()}")
print(f"Meta de Disponibilidade: {df_disp_validos['Meta'].iloc[0]*100:.0f}%")

print("\nDisponibilidade Media por Equipamento:")
print("-"*70)

meta = df_disp_validos['Meta'].iloc[0]
for equip in equipamentos:
    media = df_disp_validos[equip].mean()
    status = "Atingiu" if media >= meta else "Abaixo"
    print(f"{equip:25s} | {media*100:>14.1f}% | {status:>12s}")

disp_geral = df_disp_validos[equipamentos].mean().mean()
print(f"\nDISPONIBILIDADE GERAL: {disp_geral*100:.1f}%")

# 4. PROJECOES
print("\n" + "="*100)
print("4. PROJECAO DE CUSTOS")
print("="*100)

custo_12_meses = custo_mensal_medio * 12
custo_5_anos_oper = custo_mensal_medio * 60
custo_5_anos_total = investimento_total + custo_5_anos_oper

print(f"\nProjecao 12 Meses:")
print(f"  Custo Operacional:           R$ {custo_12_meses:,.2f}")

print(f"\nProjecao 5 Anos:")
print(f"  Investimento Inicial:        R$ {investimento_total:,.2f}")
print(f"  Custos Operacionais:         R$ {custo_5_anos_oper:,.2f}")
print(f"  CUSTO TOTAL 5 ANOS:          R$ {custo_5_anos_total:,.2f}")

# 5. SIMULACAO ALUGUEL
print("\n" + "="*100)
print("5. SIMULACAO: AQUISICAO vs ALUGUEL")
print("="*100)

custo_aluguel_mensal = investimento_total * 0.03
custo_aluguel_5anos = custo_aluguel_mensal * 60
valor_residual = investimento_total * 0.30
economia_5anos = custo_aluguel_5anos - (custo_5_anos_total - valor_residual)
roi_percentual = (economia_5anos / investimento_total) * 100

print(f"\nCusto Aluguel Estimado (3% a.m.): R$ {custo_aluguel_mensal:,.2f}/mes")
print(f"\nComparacao 5 Anos:")
print(f"  AQUISICAO:")
print(f"    - Investimento:            R$ {investimento_total:,.2f}")
print(f"    - Operacao 60 meses:       R$ {custo_5_anos_oper:,.2f}")
print(f"    - Valor Residual (30%):   -R$ {valor_residual:,.2f}")
print(f"    - Total Liquido:           R$ {custo_5_anos_total - valor_residual:,.2f}")
print(f"\n  ALUGUEL (ESTIMADO):")
print(f"    - 60 meses:                R$ {custo_aluguel_5anos:,.2f}")
print(f"\n  ECONOMIA COM AQUISICAO:      R$ {economia_5anos:,.2f}")
print(f"  ROI:                         {roi_percentual:.1f}%")

if economia_5anos > 0:
    payback_meses = investimento_total / (custo_aluguel_mensal - custo_mensal_medio)
    print(f"  Payback Estimado:            {payback_meses:.1f} meses ({payback_meses/12:.1f} anos)")

print("\n" + "="*100)
print("ANALISE CONCLUIDA!")
print("="*100)
