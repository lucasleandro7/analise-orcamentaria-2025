🏛️ Análise do Orçamento Federal 2024 — Execução por Órgão Superior

Este projeto apresenta uma análise detalhada da execução orçamentária dos órgãos superiores da Administração Pública Federal brasileira no ano de 2024.
O objetivo é compreender como os recursos foram distribuídos, empenhados e executados, identificar padrões, níveis de eficiência e possíveis gargalos.

Toda a análise foi realizada em Python, utilizando principalmente Pandas, Matplotlib, Seaborn e Jupyter Notebook.

📂 1. Sobre o Dataset

Fonte dos dados: Portal da Transparência / Siga Brasil

Ano analisado: 2024

Unidade de análise: Órgãos superiores federais

Total de órgãos: 36

Granularidade: Orçamento atualizado, empenhado e realizado por órgão

📘 Dicionário de Dados
Coluna Descrição
nome*orgao_superior Nome do órgão superior
orcamento_atualizado*(r$)	Valor total atualizado disponível
orcamento_empenhado_(r$) Valor reservado/empenhado
orcamento*realizado*(r$) Valor efetivamente utilizado
percentual_execucao Execução (%) = realizado ÷ atualizado
🧼 Tratamentos realizados

Remoção de valores infinitos e inconsistentes

Eliminação de registros inválidos

Padronização de tipos numéricos

Cálculo consistente do percentual de execução

Ordenações e filtros para ranking de análise

🧠 2. Processo de Análise

A análise foi conduzida seguindo as etapas:

Carregar e explorar os dados brutos

Limpar, corrigir e padronizar valores

Criar métricas relevantes (percentual de execução)

Gerar rankings e destaques

Construir gráficos explicativos

Interpretar insights e padrões

Gerar relatório e README final

📊 3. Principais Resultados
🔹 3.1. Órgãos com maior percentual de execução

Os cinco órgãos mais eficientes na execução do orçamento foram:

Ministério do Trabalho e Emprego — 86,8%

Ministério do Desenvolvimento e Assistência Social — 82,9%

Ministério da Previdência Social — 80,4%

Ministério das Relações Exteriores — 80,3%

Ministério da Fazenda — 77,8%

Esses órgãos apresentam desempenho acima da média nacional, demonstrando eficiência na utilização dos recursos.

🔹 3.2. Órgãos com menor percentual de execução

Os menores desempenhos foram identificados em:

Ministério do Esporte — 8,7%

Portos e Aeroportos — 11,8%

Turismo — 12,7%

Mulheres — 19,9%

Empreendedorismo e Pequenas Empresas — 23,0%

Esses órgãos representam alto risco de subexecução, podendo indicar atrasos administrativos, reorganização institucional ou baixo volume operacional.

🔹 3.3. Órgãos com maiores orçamentos

Os cinco maiores orçamentos absolutos:

Ministério da Fazenda — R$ 3,21 trilhões

Previdência Social — R$ 1,05 trilhão

Desenvolvimento e Assistência Social — R$ 291 bilhões

Saúde — R$ 248 bilhões

Educação — R$ 235 bilhões

🔹 3.4. Relação orçamento × eficiência

A análise mostra que:

Um orçamento grande não garante boa execução — porém alguns órgãos combinam ambos, como Fazenda, Previdência e MDS.

🔹 3.5. Detecção de outliers

Ministério da Fazenda domina o orçamento federal (mais de 3 trilhões).

Ministério do Esporte apresenta a menor execução entre todos (8,7%).

Órgãos recentes (como Mulheres, Igualdade Racial) têm execuções menores — comportamento esperado.

📈 4. Visualizações

O projeto inclui gráficos como:

Ranking dos Top 10 maiores percentuais de execução

Ranking dos Top 10 menores percentuais de execução

Maiores orçamentos atualizados (gráfico horizontal)

Dispersão entre orçamento vs execução

Tabelas formatadas para leitura rápida

(As imagens podem ser adicionadas na pasta /docs e referenciadas aqui.)

🛠️ 5. Ferramentas Utilizadas

Python 3

Pandas

Matplotlib

Seaborn

Jupyter Notebook

Git & GitHub
