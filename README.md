\# Grafos - Rotas Aéreas



Projeto desenvolvido para a disciplina de Grafos da Universidade Estadual de Montes Claros (Unimontes).



\## Objetivo



Representar rotas aéreas entre 20 cidades do mundo utilizando um grafo e uma matriz de adjacência.



O projeto também permite verificar se existe um caminho entre duas cidades, desconsiderando o sentido das rotas.



\## Cidades



O projeto utiliza as seguintes 20 cidades:



\- São Paulo

\- Rio de Janeiro

\- Buenos Aires

\- Santiago

\- Lima

\- Bogotá

\- Cidade do México

\- Nova York

\- Toronto

\- Los Angeles

\- Londres

\- Paris

\- Madrid

\- Roma

\- Dubai

\- Cairo

\- Tóquio

\- Pequim

\- Sydney

\- Joanesburgo



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

