\# Grafos - Rotas Aéreas

Projeto desenvolvido para a disciplina de Grafos da Universidade Estadual de Montes Claros (Unimontes).

\## Objetivo

Representar rotas aéreas entre 20 cidades do mundo utilizando um grafo e uma matriz de adjacência.

O projeto também permite verificar se existe um caminho entre duas cidades, desconsiderando o sentido das rotas.

\## Cidades

O projeto utiliza as seguintes 20 cidades:

CIDADES
0 - São Paulo
1 - Rio de Janeiro
2 - Buenos Aires
3 - Santiago
4 - Lima
5 - Bogotá
6 - Cidade do México
7 - Nova York
8 - Toronto
9 - Los Angeles
10 - Londres
11 - Paris
12 - Madrid
13 - Roma
14 - Dubai
15 - Cairo
16 - Tóquio
17 - Pequim
18 - Sydney
19 - Joanesburgo

\## Tecnologias utilizadas

\- Python

\- Google Gemini API

\- NetworkX

\- Matplotlib

\## Funcionamento

O projeto utiliza um Large Language Model (LLM) para obter informações sobre rotas aéreas comerciais entre as cidades.

As rotas são utilizadas para construir uma matriz de adjacência:

\- `1` indica que existe uma rota direta entre duas cidades.

\- `0` indica que não existe uma rota direta.

Como as rotas são consideradas sem sentido, o grafo é não direcionado.

Exemplo:

```text

São Paulo → Londres

```
