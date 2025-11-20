"""
Módulo de limpeza e preparação dos dados do orçamento público.

Este arquivo contém funções responsáveis por:
- Carregar o CSV bruto
- Padronizar nomes de colunas
- Tratar valores monetários no formato brasileiro
- Criar colunas numéricas limpas
- Gerar agregações básicas para análise
"""

import pandas as pd
import numpy as np

def load_raw(path: str) -> pd.DataFrame:
    """
    Carrega o arquivo CSV bruto e padroniza os nomes das colunas.
    
    - Converte nomes para minúsculo
    - Substitui espaços por _
    - Remove acentos e caracteres especiais
    """

    # Lê o CSV aceitando o padrão brasileiro (; e latin-1)
    df = pd.read_csv(path, encoding='latin1', sep=';')

    # Normalização dos nomes das colunas
    df.columns = (
        df.columns
        .str.lower()                # tudo minúsculo
        .str.strip()                # remove espaços no começo/fim
        .str.replace(' ', '_')      # troca espaço por _
        .str.normalize('NFKD')      # normaliza acentos para remoção
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')        # remove acentos
    )

    return df

def parse_money(value):
    """
    Converte valores no formato brasileiro (1.234.567,89) para float.
    - Remove pontos de milhar
    - Troca vírgula decimal por ponto
    - Converte para float
    """

    if pd.isna(value):
        return np.nan

    # Converte para string (caso venha como número)
    value = str(value).strip()

    if value == "":
        return np.nan

    # Remove pontos de milhar (.)
    value = value.replace('.', '')

    # Troca vírgula decimal por ponto
    value = value.replace(',', '.')

    # Tenta converter para número
    try:
        return float(value)
    except ValueError:
        return np.nan

def clean_money_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encontra automaticamente colunas com valores monetários
    e cria versões numéricas com sufixo '_float'.
    """

    # Critério simples: colunas que contem palavras relacionadas a dinheiro
    money_keywords = ['valor', 'despesa', 'dotacao', 'orcado', 'credito']

    money_columns = [
        col for col in df.columns
        if any(keyword in col for keyword in money_keywords)
    ]

    for col in money_columns:
        df[col + '_float'] = df[col].apply(parse_money)

    return df

def basic_aggregations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria agregações básicas por órgão, somando todos os valores monetários.
    Produz um DataFrame útil para análises e gráficos.
    """

    # Encontrar todas as colunas numéricas criadas ('*_float')
    numeric_cols = [col for col in df.columns if col.endswith('_float')]

    if not numeric_cols:
        print("⚠️ Nenhuma coluna numérica encontrada. Execute clean_money_columns() antes.")
        return pd.DataFrame()

    # Agrupa por órgão
    if "orgao" not in df.columns:
        print("⚠️ A coluna 'orgao' não existe no dataset.")
        return pd.DataFrame()

    grouped = df.groupby("orgao")[numeric_cols].sum().reset_index()

    return grouped

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa o pipeline completo de limpeza de dados:

    - Normaliza nomes das colunas
    - Converte valores monetários
    - Retorna o DataFrame pronto para análise
    """

    # Reaplica a normalização dos nomes (por segurança)
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(' ', '_')
        .str.normalize('NFKD')
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
    )

    # Cria colunas monetárias convertidas para float
    df = clean_money_columns(df)

    return df

def save_clean_df(df: pd.DataFrame, output_path: str):
    """
    Salva o DataFrame limpo em um caminho especificado.
    """
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Arquivo salvo em: {output_path}")


# Permite rodar o script diretamente pelo terminal:
# python src/cleaning.py data/raw/arquivo.csv
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 2:
        print("Uso: python src/cleaning.py caminho/do/arquivo.csv")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f"Arquivo não encontrado: {input_path}")
        sys.exit(1)

    print("Carregando arquivo...")
    df = load_raw(input_path)

    print("Limpando dados...")
    df_clean = clean_data(df)

    # Nome do arquivo gerado
    output_path = "data/processed/dados_limpos.csv"

    print("Salvando arquivo limpo...")
    save_clean_df(df_clean, output_path)

    print("✔️ Finalizado!")
