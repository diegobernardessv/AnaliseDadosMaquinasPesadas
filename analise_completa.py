import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ========================================
# CARREGAR DADOS
# ========================================
arquivo = r'D:\Users\diego.b.silva\Desktop\Projeto_MaquinasPesadas\ProjetoCusto_MaquinasPesadas.xlsx'

df_manutencao = pd.read_excel(arquivo, sheet_name='Custo Manutenção')
df_diesel = pd.read_excel(arquivo, sheet_name='Custo Diesel')
df_disponibilidade = pd.read_excel(arquivo, sheet_name='Disponibilidade')
df_frota = pd.read_excel(arquivo, sheet_name='Frota')

print("=" * 100)
print("📊 ANÁLISE COMPLETA - PROJETO MÁQUINAS PESADAS")
print("=" * 100)

# ========================================
# 1. INVESTIMENTO TOTAL
# ========================================
print("\n" + "=" * 100)
print("💰 1. INVESTIMENTO EM AQUISIÇÃO")
print("=" * 100)

investimento_total = df_frota['Valor de aquisição'].sum()
print(f"\n🔹 Investimento Total: R$ {investimento_total:,.2f}")

print("\n📋 Detalhamento por Equipamento:")
equipamentos_adquiridos = df_frota[df_frota['Valor de aquisição'].notna()].copy()
for idx, row in equipamentos_adquiridos.iterrows():
    print(f"  • {row['Função']:20s} - {row['Marca / Modelo']:40s} = R$ {row['Valor de aquisição']:,.2f}")

# ========================================
# 2. CUSTOS OPERACIONAIS
# ========================================
print("\n" + "=" * 100)
print("💸 2. CUSTOS OPERACIONAIS (Jun-Dez 2026)")
print("=" * 100)

# Consolidar custos
df_custos = df_manutencao.copy()
df_custos['Custo_Manutencao_Total'] = df_custos['Custo Materiais'].fillna(0) + df_custos['Custo Serviços'].fillna(0)
df_custos = df_custos.merge(df_diesel[['Data', 'Custo Total/Mês']], on='Data', how='left')
df_custos.rename(columns={'Custo Total/Mês': 'Custo_Diesel'}, inplace=True)
df_custos['Custo_Diesel'] = df_custos['Custo_Diesel'].fillna(0)
df_custos['Custo_Total_Mensal'] = df_custos['Custo_Manutencao_Total'] + df_custos['Custo_Diesel']

# Filtrar apenas meses com dados
df_custos_validos = df_custos[df_custos['Custo_Total_Mensal'] > 0].copy()

print(f"\n📅 Período de Análise: {df_custos_validos['Mês'].min()} a {df_custos_validos['Mês'].max()}")
print(f"📊 Meses com Dados: {len(df_custos_validos)}")

print("\n📈 Resumo de Custos:")
print(f"  • Custo Materiais Total:  R$ {df_custos_validos['Custo Materiais'].sum():,.2f}")
print(f"  • Custo Serviços Total:   R$ {df_custos_validos['Custo Serviços'].sum():,.2f}")
print(f"  • Custo Diesel Total:     R$ {df_custos_validos['Custo_Diesel'].sum():,.2f}")
print(f"  • Custo Operacional Total: R$ {df_custos_validos['Custo_Total_Mensal'].sum():,.2f}")

print("\n📊 Médias Mensais:")
print(f"  • Custo Materiais Médio:  R$ {df_custos_validos['Custo Materiais'].mean():,.2f}/mês")
print(f"  • Custo Serviços Médio:   R$ {df_custos_validos['Custo Serviços'].mean():,.2f}/mês")
print(f"  • Custo Diesel Médio:     R$ {df_custos_validos['Custo_Diesel'].mean():,.2f}/mês")
print(f"  • Custo Operacional Médio: R$ {df_custos_validos['Custo_Total_Mensal'].mean():,.2f}/mês")

# Composição percentual
total_custos = df_custos_validos['Custo_Total_Mensal'].sum()
perc_materiais = (df_custos_validos['Custo Materiais'].sum() / total_custos) * 100
perc_servicos = (df_custos_validos['Custo Serviços'].sum() / total_custos) * 100
perc_diesel = (df_custos_validos['Custo_Diesel'].sum() / total_custos) * 100

print("\n📊 Composição dos Custos:")
print(f"  • Materiais:  {perc_materiais:.1f}%")
print(f"  • Serviços:   {perc_servicos:.1f}%")
print(f"  • Diesel:     {perc_diesel:.1f}%")

# Tabela detalhada
print("\n📋 Custos Mensais Detalhados:")
print("-" * 100)
print(f"{'Mês':12s} | {'Materiais':>12s} | {'Serviços':>12s} | {'Diesel':>12s} | {'Total':>12s}")
print("-" * 100)
for idx, row in df_custos_validos.iterrows():
    print(f"{row['Mês']:12s} | R$ {row['Custo Materiais']:>9,.2f} | R$ {row['Custo Serviços']:>9,.2f} | "
          f"R$ {row['Custo_Diesel']:>9,.2f} | R$ {row['Custo_Total_Mensal']:>9,.2f}")
print("-" * 100)

# ========================================
# 3. DISPONIBILIDADE OPERACIONAL
# ========================================
print("\n" + "=" * 100)
print("📊 3. DISPONIBILIDADE OPERACIONAL")
print("=" * 100)

# Calcular disponibilidade por equipamento
equipamentos = ['Escavadeira', 'Pá Carregadeira', 'Varredeira', 'Caminhão Munck', 'Caminhão Pipa 1/2']
df_disp_validos = df_disponibilidade[df_disponibilidade['Escavadeira'].notna()].copy()

print(f"\n📅 Período: {df_disp_validos['Mês'].min()} a {df_disp_validos['Mês'].max()}")
print(f"🎯 Meta de Disponibilidade: {df_disp_validos['Meta'].iloc[0]*100:.0f}%")

print("\n📊 Disponibilidade Média por Equipamento:")
print("-" * 70)
print(f"{'Equipamento':25s} | {'Disponib. Média':>15s} | {'Status':>12s}")
print("-" * 70)

meta = df_disp_validos['Meta'].iloc[0]
for equip in equipamentos:
    media = df_disp_validos[equip].mean()
    status = "✅ Atingiu" if media >= meta else "⚠️ Abaixo"
    print(f"{equip:25s} | {media*100:>14.1f}% | {status:>12s}")
print("-" * 70)

# Disponibilidade geral
disp_geral = df_disp_validos[equipamentos].mean().mean()
print(f"\n{'DISPONIBILIDADE GERAL':25s} | {disp_geral*100:>14.1f}% | {'⚠️ Abaixo' if disp_geral < meta else '✅ Atingiu':>12s}")

# Ranking
print("\n🏆 Ranking de Disponibilidade:")
ranking = df_disp_validos[equipamentos].mean().sort_values(ascending=False)
for i, (equip, valor) in enumerate(ranking.items(), 1):
    emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
    print(f"  {emoji} {equip:25s} - {valor*100:.1f}%")

# Equipamentos que precisam atenção
print("\n⚠️ Equipamentos Abaixo da Meta (95%):")
abaixo_meta = ranking[ranking < meta]
if len(abaixo_meta) > 0:
    for equip, valor in abaixo_meta.items():
        gap = (meta - valor) * 100
        print(f"  • {equip:25s} - {valor*100:.1f}% (faltam {gap:.1f}pp para atingir meta)")
else:
    print("  ✅ Todos os equipamentos atingiram a meta!")

# ========================================
# 4. CONSUMO DE DIESEL
# ========================================
print("\n" + "=" * 100)
print("⛽ 4. ANÁLISE DE CONSUMO DE DIESEL")
print("=" * 100)

df_diesel_validos = df_diesel[df_diesel['Litros/Mês'].notna()].copy()
df_diesel_validos['Preco_Litro'] = df_diesel_validos['Custo Total/Mês'] / df_diesel_validos['Litros/Mês']

print(f"\n📊 Resumo do Período:")
print(f"  • Total Consumido:     {df_diesel_validos['Litros/Mês'].sum():,.1f} litros")
print(f"  • Média Mensal:        {df_diesel_validos['Litros/Mês'].mean():,.1f} litros/mês")
print(f"  • Custo Total:         R$ {df_diesel_validos['Custo Total/Mês'].sum():,.2f}")
print(f"  • Custo Médio Mensal:  R$ {df_diesel_validos['Custo Total/Mês'].mean():,.2f}/mês")
print(f"  • Preço Médio Litro:   R$ {df_diesel_validos['Preco_Litro'].mean():.2f}/litro")

print("\n📋 Consumo Mensal Detalhado:")
print("-" * 70)
print(f"{'Mês':12s} | {'Litros':>12s} | {'Custo Total':>15s} | {'R$/Litro':>10s}")
print("-" * 70)
for idx, row in df_diesel_validos.iterrows():
    print(f"{row['Mês']:12s} | {row['Litros/Mês']:>10,.1f} L | R$ {row['Custo Total/Mês']:>11,.2f} | "
          f"R$ {row['Preco_Litro']:>7.2f}")
print("-" * 70)

# ========================================
# 5. PROJEÇÃO DE CUSTOS - 12 MESES
# ========================================
print("\n" + "=" * 100)
print("🔮 5. PROJEÇÃO DE CUSTOS - PRÓXIMOS 12 MESES")
print("=" * 100)

# Calcular média mensal e projetar
custo_mensal_medio = df_custos_validos['Custo_Total_Mensal'].mean()

print(f"\n📊 Base para Projeção:")
print(f"  • Custo Operacional Médio Mensal: R$ {custo_mensal_medio:,.2f}")

# Projeção simples (mesma média)
custo_12_meses = custo_mensal_medio * 12
custo_1_ano_total = custo_12_meses + investimento_total

print(f"\n💰 Projeções:")
print(f"  • Custo Operacional 12 meses:     R$ {custo_12_meses:,.2f}")
print(f"  • Custo Total Ano 1 (Invest+Oper): R$ {custo_1_ano_total:,.2f}")

# Projeção 5 anos
custo_5_anos_oper = custo_mensal_medio * 60
custo_5_anos_total = investimento_total + custo_5_anos_oper

print(f"\n📅 Projeção 5 Anos:")
print(f"  • Investimento Inicial:           R$ {investimento_total:,.2f}")
print(f"  • Custos Operacionais (60 meses): R$ {custo_5_anos_oper:,.2f}")
print(f"  • CUSTO TOTAL 5 ANOS:             R$ {custo_5_anos_total:,.2f}")

# ========================================
# 6. ANÁLISE COMPARATIVA (SIMULAÇÃO)
# ========================================
print("\n" + "=" * 100)
print("⚖️ 6. SIMULAÇÃO: AQUISIÇÃO vs ALUGUEL")
print("=" * 100)

print("\n⚠️ IMPORTANTE: Esta é uma simulação. Você precisa coletar valores reais de aluguel!")

# Simulação de custo de aluguel (exemplo: 3% do valor do equipamento por mês)
custo_aluguel_mensal_estimado = investimento_total * 0.03

print(f"\n📊 Premissas da Simulação:")
print(f"  • Custo estimado de aluguel: 3% do valor dos equipamentos/mês")
print(f"  • Custo Aluguel Mensal Estimado: R$ {custo_aluguel_mensal_estimado:,.2f}")

# Comparação 5 anos
custo_aluguel_5anos = custo_aluguel_mensal_estimado * 60
economia_5anos = custo_aluguel_5anos - custo_5_anos_total
roi_percentual = (economia_5anos / investimento_total) * 100

# Estimativa de valor residual (30% do valor original)
valor_residual_estimado = investimento_total * 0.30
economia_5anos_com_residual = economia_5anos + valor_residual_estimado
roi_com_residual = (economia_5anos_com_residual / investimento_total) * 100

print(f"\n💰 Comparação 5 Anos:")
print("-" * 70)
print(f"{'Opção':30s} | {'Custo Total':>20s}")
print("-" * 70)
print(f"{'AQUISIÇÃO':30s} | R$ {custo_5_anos_total:>17,.2f}")
print(f"  - Investimento:               | R$ {investimento_total:>17,.2f}")
print(f"  - Operação 60 meses:          | R$ {custo_5_anos_oper:>17,.2f}")
print(f"  - Valor Residual (30%):       | R$ {-valor_residual_estimado:>17,.2f}")
print("-" * 70)
print(f"{'ALUGUEL (ESTIMADO)':30s} | R$ {custo_aluguel_5anos:>17,.2f}")
print("-" * 70)
print(f"{'ECONOMIA COM AQUISIÇÃO':30s} | R$ {economia_5anos:>17,.2f}")
print(f"{'ECONOMIA + RESIDUAL':30s} | R$ {economia_5anos_com_residual:>17,.2f}")
print("-" * 70)

print(f"\n📊 Indicadores Financeiros (Simulados):")
print(f"  • ROI sem Residual:     {roi_percentual:>6.1f}%")
print(f"  • ROI com Residual:     {roi_com_residual:>6.1f}%")

if economia_5anos > 0:
    payback_meses = investimento_total / (custo_aluguel_mensal_estimado - custo_mensal_medio)
    print(f"  • Payback Estimado:     {payback_meses:>6.1f} meses ({payback_meses/12:.1f} anos)")
else:
    print(f"  • Payback:              Não viável (aluguel é mais econômico)")

# ========================================
# 7. RECOMENDAÇÕES
# ========================================
print("\n" + "=" * 100)
print("💡 7. RECOMENDAÇÕES E PRÓXIMOS PASSOS")
print("=" * 100)

print("\n✅ PONTOS FORTES:")
print("  1. Caminhão Munck com excelente disponibilidade (98,6%)")
print("  2. Escavadeira próxima da meta (93,1%)")
print("  3. Investimento consolidado em equipamentos novos")

print("\n⚠️ PONTOS DE ATENÇÃO:")
print("  1. Varredeira com baixa disponibilidade (64,8% vs meta 95%)")
print("  2. Disponibilidade geral abaixo da meta (91,3% vs 95%)")
print("  3. Custos operacionais precisam ser monitorados")

print("\n📋 DADOS NECESSÁRIOS PARA ANÁLISE COMPLETA:")
print("  1. ⚠️ CRÍTICO: Cotações reais de aluguel dos equipamentos")
print("  2. ⚠️ CRÍTICO: Horas trabalhadas por equipamento/mês")
print("  3. Valor de revenda/residual estimado (consultar mercado)")
print("  4. Custos indiretos (seguro, IPVA, armazenamento)")
print("  5. Histórico de falhas e manutenções corretivas")

print("\n🎯 AÇÕES RECOMENDADAS:")
print("  1. Investigar problemas da Varredeira (manutenção preventiva inadequada?)")
print("  2. Coletar cotações de 3-5 locadoras para comparação real")
print("  3. Implementar controle rigoroso de horas operacionais")
print("  4. Estabelecer plano de manutenção preventiva para todos equipamentos")
print("  5. Revisar meta de disponibilidade (95% pode ser muito agressivo?)")

print("\n📊 PARA O DASHBOARD POWER BI:")
print("  1. Implementar todas as medidas DAX do guia")
print("  2. Criar página de simulação com parâmetros interativos")
print("  3. Adicionar alertas visuais para equipamentos abaixo da meta")
print("  4. Incluir gráficos de tendência e projeção")
print("  5. Preparar versão executiva (1 página) para apresentação")

print("\n" + "=" * 100)
print("✅ ANÁLISE CONCLUÍDA!")
print("=" * 100)
print("\n📄 Consulte o arquivo GUIA_POWERBI.md para instruções detalhadas de implementação no Power BI")
print("\n")
