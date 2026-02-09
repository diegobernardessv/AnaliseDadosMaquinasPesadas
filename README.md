# 📊 Dashboard BI - Análise de Viabilidade de Máquinas Pesadas

> Dashboard interativo em Power BI para análise de investimento de R$ 2,94 milhões em máquinas pesadas.

[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![DAX](https://img.shields.io/badge/DAX-15+-orange?style=for-the-badge)](https://dax.guide/)

---

## 🎯 Visão Geral

Projeto de Business Intelligence desenvolvido para análise de viabilidade da aquisição de 10 equipamentos (máquinas pesadas e veículos) para usina, com foco em:

- 💰 **Análise de Custos Operacionais 2025** (R$ 965k em 7 meses)
- 📈 **Monitoramento de Performance** (Meta: 95% de disponibilidade)
- 🔮 **Projeções Financeiras 2026** (R$ 2,36 Mi projetado com crescimento 5%)
- ⚠️ **Identificação de Oportunidades** de redução de custos operacionais

---

## 📸 Preview do Dashboard

### Visão Executiva
![Visão Executiva](screenshots/1_AnaliseViabilidade.png)

### Detalhes por Equipamento
![Detalhes Equipamento](screenshots/2_DetalhesPorEquipamento.png)

### Disponibilidade Operacional
![Disponibilidade](screenshots/3_DisponibilidadeOperacional.png)

### Projeções e Cenários
![Projeções](screenshots/4_ProjecoesCenarios.png)

---

## 🚀 Quick Start

### Pré-requisitos
- Power BI Desktop (versão mais recente)
- Python 3.12+ (opcional, para análises exploratórias)

### Como usar
1. **Clone ou baixe** este repositório
2. **Abra** o arquivo `ProjetoMaquinasPesadasBI.pbix` no Power BI Desktop
3. **Navegue** pelas 4 páginas do dashboard
4. **Explore** os insights e filtros interativos

### Para análise Python
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar análise
python analise_completa.py
```

---

## 📊 Estrutura do Dashboard

### 📄 **Página 1: Visão Executiva**
**KPIs Principais:**
- Investimento Total: R$ 4,38 Mi
- Custo Operacional Médio: R$ 138k/mês
- Período Analisado: Jun-Dez 2025 (7 meses)
- Total Operacional: R$ 965k

**Visuais:**
- Evolução de Custos (3 categorias: Materiais, Serviços, Diesel)
- Composição dos Custos (Rosca)
- Gauge de Disponibilidade vs Meta

---

### 📄 **Página 2: Detalhes por Equipamento**
**Conteúdo:**
- Tabela completa da frota (10 equipamentos)
- Custos mensais de Manutenção - Materiais e Serviços (Matriz detalhada)
- Consumo de Diesel mensal por equipamento (Gráfico de colunas)
- Análise de composição de custos

---

### 📄 **Página 3: Disponibilidade Operacional**
**Análise Detalhada:**
- Cards de Performance (Acima da meta, Gap, Melhor)
- Evolução mensal por equipamento (5 linhas)
- Indicador de Tendência (Crescimento: +6,26%)

**Insights:**
- 2 equipamentos acima da meta (Munck e Pipa)
- Varredeira crítica: 70,9% (necessita atenção)
- Tendência positiva: 83,54% → 89,80%

---

### 📄 **Página 4: Projeções e Cenários**
**Análises Preditivas:**
- Base 2025: R$ 965 mil (Jun-Dez, 7 meses)
- Custo Médio Mensal: R$ 138 mil/mês (base)
- Projeção 2026: R$ 2,36 Mi (12 meses com crescimento 5% anual)
- Evolução mensal: Jan R$ 138k → Dez R$ 145k
- Potencial de otimização: R$ 193 mil/ano

**Cenários Mensais:**
- 🟢 Otimista: R$ 124k/mês (-10%)
- 🔵 Realista: R$ 138-145k/mês (crescimento 5%)
- 🔴 Pessimista: R$ 159k/mês (+15%)

---

## 🔍 Principais Insights

### 🚨 Crítico
- **Varredeira Volvo VM 220** com apenas **70,9%** de disponibilidade
- **24,1% abaixo da meta** → Requer ação imediata

### ✅ Destaque
- **Caminhão Munck** com **98%** de disponibilidade
- **Acima da meta** → Benchmark de excelência

### 📈 Tendência Positiva
- Melhoria de **+6,26%** em 5 meses (ago→dez)
- De 83,54% para 89,80%
- Projeção: atingir 95% em **7 meses**

### 💰 Financeiro
- Custo real 2025 (Jun-Dez): **R$ 965 mil** (7 meses)
- Custo médio mensal: **R$ 137.849/mês**
- Projeção 2026: **R$ 2,36 milhões** (12 meses com crescimento 5%)
- Evolução mensal 2026: Jan R$ 138k → Dez R$ 145k
- Economia potencial: **R$ 193 mil/ano** (com otimização de 10%)

---

## 🛠️ Tecnologias Utilizadas

### Business Intelligence
- **Power BI Desktop** - Desenvolvimento do dashboard
- **DAX (Data Analysis Expressions)** - 15+ medidas calculadas
- **Power Query** - Transformação de dados

### Análise de Dados
- **Python 3.12**
  - Pandas 3.0.0
  - Matplotlib 3.10.8
  - Seaborn 0.13.2
  - OpenPyXL 3.1.5

### Dados
- **Microsoft Excel** - 4 planilhas integradas
- **7 meses** de dados operacionais (Jun-Dez 2025)
- **10 equipamentos** na frota total

---

## 📐 Medidas DAX Principais

```dax
// Custo Operacional Total (Jun-Dez 2025)
Custo_Op_Total = 
    SUM('Custo Manutenção'[Custo Materiais]) + 
    SUM('Custo Manutenção'[Custo Serviços]) + 
    SUM('Custo Diesel'[Custo Total/Mês])
    // Total: R$ 964.947

// Custo Médio Mensal (base 2025)
Custo_Op_Medio = DIVIDE([Custo_Op_Total], 7, 0)
    // Média: R$ 137.849/mês

// Projeção 2026 com Crescimento 5%
// Tabela Projecao_2026 com valores mensais crescentes
// Jan: R$ 137.849 → Dez: R$ 144.741
// Total anual: R$ 2,36 milhões

// Disponibilidade Geral
Disponibilidade_Geral = 
    DIVIDE(
        AVERAGE(Disponibilidade[Escavadeira]) +
        AVERAGE(Disponibilidade[Pá Carregadeira]) +
        AVERAGE(Disponibilidade[Varredeira]) +
        AVERAGE(Disponibilidade[Caminhão Munck]) +
        AVERAGE(Disponibilidade[Caminhão Pipa 1/2]),
        5
    )

// Gap para Meta
Gap_Meta = ([Disponibilidade_Geral] - 0.95) * 100

// Cenários
Cenario_Otimista = [Custo_Op_Medio] * 0.90
Cenario_Realista = [Custo_Op_Medio]
Cenario_Pessimista = [Custo_Op_Medio] * 1.15
```

---

## 📊 Dados do Projeto

### Equipamentos Analisados
| # | Equipamento | Marca/Modelo | Valor |
|---|-------------|--------------|-------|
| 1 | Pipa | M. Benz Atego 1719 | R$ 455.000 |
| 2 | Pipa | Ford Cargo 1619 | R$ 350.000 |
| 3 | Automóvel | Peugeot 206 1.4 FX | R$ 22.000 |
| 4 | Garra Hidráulica | M. Benz L 2635 6x4 | R$ 240.000 |
| 5 | Basculante | SR 3Eixos | R$ 250.000 |
| 6 | Emergência | Fiat Ducato Maxx Cargo 2,8 | R$ 236.000 |
| 7 | Escavadeira | Hyundai R140 LC-9SB | R$ 540.000 |
| 8 | Carregadeira | Caterpillar 924K | R$ 500.000 |
| 9 | Munck | Volkswagen 24250 6x2 | R$ 650.000 |
| 10 | Varredeira | Volvo VM 220 | R$ 1.135.000 |
| **TOTAL** | | | **R$ 4.378.000** |

### Composição de Custos (7 meses - Jun a Dez 2025)
- 🟠 **Diesel:** R$ 453.237 (46,97%)
- 🟢 **Materiais:** R$ 291.808 (30,24%)
- 🔵 **Serviços:** R$ 219.902 (22,79%)
- **TOTAL:** R$ 964.947

---

## 🎓 Habilidades Demonstradas

### Técnicas
- ✅ Modelagem de dados relacionais
- ✅ Criação de medidas DAX complexas
- ✅ Visualização de dados avançada
- ✅ Análise exploratória com Python
- ✅ Transformação de dados (Power Query)

### Analíticas
- ✅ Análise de viabilidade financeira
- ✅ KPIs operacionais
- ✅ Projeções e cenários
- ✅ Identificação de tendências
- ✅ Storytelling com dados

### Negócio
- ✅ Gestão de ativos (CapEx)
- ✅ Custos operacionais (OpEx)
- ✅ Análise de ROI
- ✅ Indicadores de manutenção

---

## 💡 Aprendizados

1. **Modelagem de dados é fundamental** - Relacionamentos bem estruturados facilitam análises complexas
2. **DAX é poderoso** - Medidas calculadas permitem análises que SQL puro não alcançaria
3. **Visualização é arte + ciência** - Equilíbrio entre estética e funcionalidade
4. **Contexto de negócio guia decisões técnicas** - Conhecer o domínio é essencial
5. **Iteração melhora o produto** - Feedback contínuo refina o dashboard

---

## 🔗 Contato

**Desenvolvido por:** Diego Bernardes Silva  
**Data:** Fevereiro de 2026  
**Ferramentas:** Power BI Desktop, Python, DAX, Excel  

**Portfolio:** [https://www.dbsolutions.dev.br/]  
**LinkedIn:** [https://www.linkedin.com/in/diegobernardessv/]  
**GitHub:** [(https://github.com/diegobernardessv)]  
**E-mail:** [diegobernardessv@gmail.com]

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio.  
Dados sensíveis foram anonimizados/simulados quando necessário.

---

## ⭐ Destaques

- ✨ **4 páginas interativas** e navegáveis
- ✨ **25+ visuais customizados**
- ✨ **15+ medidas DAX**
- ✨ **R$ 4,38 Mi em ativos** analisados
- ✨ **Insights acionáveis** para tomada de decisão

---

**⚡ Dashboard completo demonstrando capacidade em Business Intelligence, desde coleta de dados até entrega de insights estratégicos!**
