# 📊 Resumo do Projeto - Análise de Viabilidade de Máquinas Pesadas

## 📋 Informações do Projeto

**Período analisado:** Jun-Dez 2025 (7 meses)  
**Investimento total:** R$ 2.940.690  
**Equipamentos:** 6 máquinas pesadas  
**Objetivo:** Avaliar viabilidade da aquisição vs aluguel e projetar custos operacionais para 2026

---

## 🐍 1. Tratamento e Análise de Dados com Python

### 1.1 Bibliotecas Utilizadas
- **pandas 3.0.0** - Manipulação e análise de dados
- **matplotlib 3.10.8** - Visualizações gráficas
- **seaborn 0.13.2** - Gráficos estatísticos avançados
- **openpyxl 3.1.5** - Leitura de arquivos Excel

### 1.2 Fonte de Dados
**Arquivo:** `ProjetoCusto_MaquinasPesadas.xlsx`  
**Planilhas processadas:**
1. **Frota** - Especificações e valores de aquisição dos equipamentos
2. **Custo Manutenção** - Custos mensais de materiais e serviços (Jun-Dez 2025)
3. **Custo Diesel** - Consumo e custos de combustível por equipamento
4. **Disponibilidade** - Percentual de disponibilidade operacional mensal

### 1.3 Transformações Realizadas

#### Scripts Python desenvolvidos:

**a) `analisar_dados.py`** - Análise exploratória inicial
- Leitura de todas as planilhas
- Verificação de tipos de dados e valores nulos
- Estatísticas descritivas básicas
- Identificação de outliers

**b) `analise_completa.py`** - Análise detalhada
- Cálculo de totais mensais por categoria de custo
- Agregação de custos operacionais (Materiais + Serviços + Diesel)
- Cálculo de médias mensais e anuais
- Análise de disponibilidade por equipamento
- Identificação de equipamentos críticos

**c) `gerar_relatorio.py`** - Geração de relatórios
- Criação de visualizações com matplotlib/seaborn
- Gráficos de evolução temporal de custos
- Análise de composição de custos (pizza)
- Comparativo de disponibilidade por equipamento

### 1.4 Principais Achados da Análise Python

**Custos Operacionais 2025 (Jun-Dez):**
- **Total:** R$ 448.470
- **Média mensal:** R$ 64.040
- **Composição:**
  - Materiais: R$ 190.113 (42,41%)
  - Diesel: R$ 164.000 (36,54%)
  - Serviços: R$ 94.357 (21,05%)

**Disponibilidade Operacional:**
- **Média geral:** 88,09%
- **Melhor equipamento:** Caminhão Munck (98,6%)
- **Equipamento crítico:** Varredeira (70,9%)
- **Gap para meta de 95%:** -6,91%
- **Tendência:** +6,26% de melhoria (ago→dez 2025)

**Projeções Calculadas:**
- Custo anual 2026 (12 meses × média): R$ 768.480
- Meses para atingir meta de 95%: 7 meses
- Economia potencial com otimização de 10%: R$ 77 mil/ano

---

## 📊 2. Desenvolvimento do Dashboard em Power BI

### 2.1 Modelagem de Dados

**Tabelas importadas:**
- `Frota` (6 linhas)
- `Custo Manutenção` (7 meses × equipamentos)
- `Custo Diesel` (7 meses × equipamentos)
- `Disponibilidade` (7 meses × 5 equipamentos)

**Tabela criada:**
- `Calendario_2026` - Datas de Jan-Dez 2026 para projeções
- `Projecao_2026` - Tabela estática com projeções mensais de custos e disponibilidade

**Relacionamentos:**
- Tabela Calendário conectada a tabelas de custos via Data
- Frota conectada a todas as tabelas via Equipamento

### 2.2 Medidas DAX Criadas (15+ medidas)

**Medidas Financeiras:**
```dax
Investimento_Total = SUM(Frota[Valor de aquisição])

Custo_Op_Total = 
    SUM('Custo Manutenção'[Custo Materiais]) + 
    SUM('Custo Manutenção'[Custo Serviços]) + 
    SUM('Custo Diesel'[Custo Total/Mês])

Custo_Op_Medio = DIVIDE([Custo_Op_Total], 7, 0)

Cenario_Otimista = [Custo_Op_Medio] * 0.90
Cenario_Realista = [Custo_Op_Medio]
Cenario_Pessimista = [Custo_Op_Medio] * 1.15
```

**Medidas Operacionais:**
```dax
Disponibilidade_Geral = 
    DIVIDE(
        AVERAGE(Disponibilidade[Escavadeira]) +
        AVERAGE(Disponibilidade[Pá Carregadeira]) +
        AVERAGE(Disponibilidade[Varredeira]) +
        AVERAGE(Disponibilidade[Caminhão Munck]) +
        AVERAGE(Disponibilidade[Caminhão Pipa 1/2]),
        5
    )

Gap_Meta = ([Disponibilidade_Geral] - 0.95) * 100

Tendencia_Crescimento = 
    // Calculado como (Dez - Ago) / Ago
    // +6,26% de melhoria
```

### 2.3 Estrutura do Dashboard (4 Páginas)

#### **Página 1: Visão Executiva**
**KPIs (4 Cards):**
- Investimento Total: R$ 2,94 Mi
- Custo Operacional Médio: R$ 64 Mil/mês
- Disponibilidade Geral: 88,1%
- Meta: 95%

**Visuais (3):**
- Gráfico de Linhas: Evolução de Custos Operacionais (Jun-Dez 2025)
  - 3 linhas: Materiais, Serviços, Diesel
- Gráfico de Rosca: Composição dos Custos
  - 3 fatias: Materiais (42%), Diesel (37%), Serviços (21%)
- Gauge: Disponibilidade vs Meta
  - Atual: 88,1% | Meta: 95%

---

#### **Página 2: Detalhes por Equipamento**
**Visuais (4):**
- Tabela: Frota Completa
  - Colunas: Função, Marca/Modelo, Valor de Aquisição
  - Total: R$ 2.940.690
- Matriz: Custos de Manutenção Mensal
  - Linhas: Meses | Colunas: Materiais, Serviços
  - Totais dinâmicos
- Gráfico de Colunas: Consumo de Diesel Mensal
  - Eixo X: Meses | Eixo Y: Custo em R$
- Gráfico de Barras Horizontais: Disponibilidade por Equipamento
  - Linha de meta em 95%
  - Cores condicionais (vermelho < 95%, verde ≥ 95%)

---

#### **Página 3: Disponibilidade Operacional - Análise Detalhada**
**KPIs (3 Cards):**
- Acima da Meta (95%): 2 equipamentos
- Gap x Meta: -6,91%
- Melhor Performance: Ambulância 100% *(dados de dezembro)*

**Visuais (2):**
- Gráfico de Linhas: Evolução Mensal por Equipamento
  - 5 linhas (um por equipamento)
  - Linha de meta pontilhada em 95%
  - Período: Jul-Dez 2025
- Área de Texto: Indicador de Tendência
  - Crescimento: 89,80% ↗
  - Mostra melhoria de +6,26% em 5 meses

---

#### **Página 4: Projeções e Análise de Cenários**
**KPIs (3 Cards):**
- Custo Operacional Projetado 2026: R$ 788 Mil
- Meses para atingir Meta de Disponibilidade (95%): 7
- Economia Potencial: R$ 77 Mil

**Visuais (3):**
- Gráfico de Linhas: Projeção de Custos Operacionais 2026
  - Eixo X: Jan-Dez 2026
  - Eixo Y: Custo mensal (R$ 64k → R$ 67k)
  - Crescimento: 5% ao ano
  - Total anual: R$ 788 mil

- Gráfico de Linhas: Projeção de Disponibilidade 2026
  - Eixo X: Jan-Dez 2026
  - Eixo Y: Disponibilidade (89,8% → 100%)
  - Linha de meta em 95%
  - Atinge meta em Jul/2026 (mês 7)

- Gráfico de Colunas: Análise de Cenários - Custo Mensal Médio
  - Cenário Otimista: R$ 58 Mil (-10%)
  - Cenário Realista: R$ 64 Mil (atual)
  - Cenário Pessimista: R$ 74 Mil (+15%)

**Painel de Insights (Texto):**
```
🔴 CRÍTICO: Varredeira em 70,9% - Muito abaixo da meta de 95%
✅ DESTAQUE: Ambulância com 100% - Acima da meta
✅ DESTAQUE: Caminhão Munck com 98% - Acima da meta
🔵 POSITIVO: Disponibilidade subindo de 83,5% para 89,8%
💰 CUSTO: R$ 788 mil anuais operacionais
📅 PREVISÃO: 7 meses para atingir meta de 95%
💡 ECONOMIA: R$ 77 mil potenciais com otimização de 10%
```

### 2.4 Formatações e Recursos Visuais

**Formatação de valores:**
- Moeda: R$ com sufixo "Mil" ou "Mi" (milhões)
- Percentuais: 2 casas decimais
- Cores temáticas:
  - Verde: Valores positivos/acima da meta
  - Vermelho: Valores críticos/abaixo da meta
  - Azul: Valores neutros/realistas

**Interatividade:**
- Navegação entre páginas via botões
- Filtros por mês e equipamento
- Tooltips personalizados com detalhes
- Drill-through para detalhamento

---

## 📈 3. Principais Insights e Resultados

### 3.1 Análise de Custos
✅ **Custo médio mensal:** R$ 64.040 (base 2025)  
✅ **Projeção anual 2026:** R$ 788 mil (com crescimento 5%)  
✅ **Composição equilibrada:** 42% materiais, 37% diesel, 21% serviços  
⚠️ **Pico em set/2025:** R$ 78 mil (necessita investigação)

### 3.2 Análise de Disponibilidade
✅ **Média geral:** 88,09%  
⚠️ **Gap para meta:** -6,91% (faltam 6,91 pontos percentuais)  
✅ **Tendência positiva:** +6,26% de melhoria em 5 meses  
✅ **Prazo para meta:** 7 meses (Jul/2026)  
🏆 **Melhor equipamento:** Caminhão Munck (98,6%)  
🚨 **Equipamento crítico:** Varredeira (70,9% - 24,1% abaixo da meta)

### 3.3 Projeções 2026
✅ **Custo mensal evolui:** Jan R$ 64k → Dez R$ 67k  
✅ **Disponibilidade evolui:** Jan 89,8% → Dez 100%  
✅ **Meta de 95% atingida em:** Julho/2026  
✅ **Economia potencial:** R$ 77 mil/ano (com otimização 10%)

### 3.4 Cenários Simulados
🟢 **Otimista (-10%):** R$ 58 mil/mês = R$ 696 mil/ano  
🔵 **Realista (atual):** R$ 64 mil/mês = R$ 788 mil/ano  
🔴 **Pessimista (+15%):** R$ 74 mil/mês = R$ 888 mil/ano

---

## 🎓 4. Competências Técnicas Demonstradas

### Python & Análise de Dados
✅ Manipulação de dados com pandas  
✅ Análise exploratória (EDA)  
✅ Visualizações com matplotlib/seaborn  
✅ Leitura e processamento de arquivos Excel  
✅ Cálculos estatísticos e agregações  

### Power BI & Business Intelligence
✅ Modelagem de dados relacionais  
✅ Criação de medidas DAX complexas (15+)  
✅ Transformação de dados com Power Query  
✅ Design de dashboards interativos (4 páginas, 25+ visuais)  
✅ Visualizações avançadas e formatação condicional  
✅ Storytelling com dados  

### Análise de Negócios
✅ Análise de viabilidade financeira (CapEx)  
✅ Monitoramento de custos operacionais (OpEx)  
✅ KPIs de manutenção e disponibilidade  
✅ Projeções e cenários de negócio  
✅ Identificação de oportunidades de economia  

---

## 📊 5. Dados Finais Consolidados

### Equipamentos Analisados
| Equipamento | Marca/Modelo | Valor | Disponibilidade 2025 |
|-------------|--------------|-------|---------------------|
| Escavadeira | Hyundai R140 LC-9SB | R$ 470.000 | 93,1% |
| Pá Carregadeira | Caterpillar 924K | R$ 550.000 | 88,0% |
| Caminhão Munck | Volkswagen 24250 | R$ 550.000 | **98,6%** 🏆 |
| Varredeira | Volvo VM 220 | R$ 910.800 | **70,9%** 🚨 |
| Caminhão Pipa | Mercedes Atego 1719 | R$ 339.890 | 89,9% |
| Basculante | SR / 3Eixos | R$ 120.000 | - |
| **TOTAL** | | **R$ 2.940.690** | **88,09%** |

### Custos Operacionais 2025 (Jun-Dez)
| Categoria | Valor | % do Total |
|-----------|-------|-----------|
| Materiais | R$ 190.113 | 42,41% |
| Diesel | R$ 164.000 | 36,54% |
| Serviços | R$ 94.357 | 21,05% |
| **TOTAL** | **R$ 448.470** | **100%** |
| **Média Mensal** | **R$ 64.040** | - |

### Projeções 2026
| Métrica | Valor |
|---------|-------|
| Custo Operacional Projetado | R$ 788 mil |
| Crescimento Anual | 5% |
| Custo Mensal Jan/2026 | R$ 64.040 |
| Custo Mensal Dez/2026 | R$ 66.997 |
| Disponibilidade Jan/2026 | 89,8% |
| Disponibilidade Dez/2026 | 100% |
| Mês de atingimento da meta 95% | Julho (mês 7) |
| Economia potencial (otimização 10%) | R$ 77 mil/ano |

---

## 🏆 6. Conclusões e Recomendações

### Conclusões
1. **Viabilidade Confirmada:** Investimento de R$ 2,94 Mi com custo operacional controlável (~R$ 788k/ano)
2. **Performance Satisfatória:** Disponibilidade média de 88% com tendência crescente
3. **Meta Atingível:** Projeção de atingir 95% em 7 meses com a tendência atual
4. **Custo Previsível:** Padrão de custos estável com média de R$ 64k/mês

### Recomendações Estratégicas
🚨 **Ação Imediata:** Investigar e corrigir baixa disponibilidade da Varredeira (70,9%)  
📊 **Benchmark:** Replicar boas práticas do Caminhão Munck (98,6%) aos demais equipamentos  
💰 **Economia:** Implementar plano de otimização de 10% nos custos (potencial R$ 77k/ano)  
📈 **Monitoramento:** Acompanhar tendência mensal para garantir atingimento da meta em Jul/2026  
🔍 **Investigação:** Analisar pico de custos em Set/2025 (R$ 78k) para evitar recorrência

---

**Dashboard desenvolvido em:** Power BI Desktop  
**Análises realizadas em:** Python 3.12  
**Período do projeto:** Fevereiro 2026  
**Status:** ✅ Concluído
