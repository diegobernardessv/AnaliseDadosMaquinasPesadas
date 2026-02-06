import pandas as pd
import openpyxl

# Carregar o arquivo Excel
arquivo = r'D:\Users\diego.b.silva\Desktop\Projeto_MaquinasPesadas\ProjetoCusto_MaquinasPesadas.xlsx'

# Primeiro, vamos ver todas as abas disponíveis
xls = pd.ExcelFile(arquivo)
print("=" * 80)
print("ABAS DISPONÍVEIS NO ARQUIVO:")
print("=" * 80)
for i, aba in enumerate(xls.sheet_names, 1):
    print(f"{i}. {aba}")

print("\n" + "=" * 80)
print("ANÁLISE DETALHADA DE CADA ABA:")
print("=" * 80)

# Agora vamos ler e analisar cada aba
for aba in xls.sheet_names:
    print(f"\n{'=' * 80}")
    print(f"ABA: {aba}")
    print("=" * 80)
    
    try:
        df = pd.read_excel(arquivo, sheet_name=aba)
        
        print(f"\nDimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")
        print(f"\nColunas disponíveis:")
        for col in df.columns:
            print(f"  - {col}")
        
        print(f"\nPrimeiras linhas dos dados:")
        print(df.head(12).to_string())
        
        print(f"\nInformações sobre tipos de dados:")
        print(df.dtypes)
        
        print(f"\nResumo estatístico (colunas numéricas):")
        print(df.describe())
        
    except Exception as e:
        print(f"Erro ao ler aba {aba}: {e}")

print("\n" + "=" * 80)
print("ANÁLISE CONCLUÍDA")
print("=" * 80)
