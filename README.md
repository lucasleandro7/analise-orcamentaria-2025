# 📊 Análise Orçamentária Federal – 2025

Este projeto realiza uma análise exploratória do orçamento público federal, com foco na relação entre **orçamento atualizado**, **empenhado**, **pago** e **percentual de execução** por órgão superior.  
Ele foi desenvolvido em Python utilizando **Pandas**, **Matplotlib** e **Seaborn**, com scripts automatizados para geração de gráficos e apresentações profissionais.

---

## 🚀 Objetivos do Projeto

✔️ Organizar e limpar dados orçamentários  
✔️ Calcular indicadores de execução  
✔️ Gerar visualizações profissionais automaticamente  
✔️ Criar uma apresentação (PowerPoint) com gráficos e resultados  
✔️ Criar um repositório estruturado para portfólio  

---

## 📁 Estrutura do Repositório

📦 analise-orcamentaria-2025
├── data/
│ └── orc_por_orgao_final.csv
├── scripts/
│ ├── generate_charts.py
│ └── generate_pptx.py
├── output/
│ ├── charts/
│ └── apresentacao.pptx
└── README.md


---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **python-pptx**

---

## 📈 Indicadores Analisados

- **Orçamento atualizado**
- **Orçamento empenhado**
- **Orçamento pago**
- **Percentual de execução**
- Comparação entre órgãos federais
- Ranking dos maiores valores executados e atualizados

---

## 📊 Geração Automática de Gráficos

O script `generate_charts.py` gera automaticamente:

- Top 10 maiores orçamentos atualizados  
- Top 10 maiores valores empenhados  
- Top 10 maiores valores pagos  
- Top 10 menores percentuais de execução  
- Distribuições gerais  
- Gráficos comparativos entre indicadores  

Todos os gráficos são salvos automaticamente na pasta:

---

## 🎞️ Geração Automática do PowerPoint

O script `generate_pptx.py` monta uma apresentação profissional com:

- Capa  
- Introdução  
- Metodologia  
- Todos os gráficos  
- Conclusões  

A saída é:
output/apresentacao.pptx


---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/lucasleandro7/analise-orcamentaria-2025.git
Instale as dependências:
pip install -r requirements.txt
Execute os scripts:
python scripts/generate_charts.py
python scripts/generate_pptx.py


📚 Dataset

O arquivo utilizado é:
data/orc_por_orgao_final.csv

🧾 Licença

Este projeto é distribuído sob a licença MIT.


✨ Autor

Lucas Leandro
🚀 Projeto para portfólio de análise de dados
