# Grafos — Rotas Aéreas

Projeto desenvolvido para a disciplina de Grafos da Universidade Estadual de Montes Claros (Unimontes).

## Objetivo

Representar rotas aéreas entre 20 cidades do mundo por meio de um grafo não direcionado e de uma matriz de adjacência.

O programa consulta o Google Gemini para obter uma lista de rotas aéreas diretas, constrói o grafo e permite ao usuário escolher duas cidades. Em seguida, verifica se existe um caminho entre elas, desconsiderando o sentido das rotas, e destaca em vermelho o menor caminho encontrado.

## Cidades

- São Paulo
- Rio de Janeiro
- Buenos Aires
- Santiago
- Lima
- Bogotá
- Cidade do México
- Nova York
- Toronto
- Los Angeles
- Londres
- Paris
- Madrid
- Roma
- Dubai
- Cairo
- Tóquio
- Pequim
- Sydney
- Joanesburgo

## Tecnologias utilizadas

- Python
- Google Gemini API
- NetworkX
- Matplotlib

## Como executar

### 1. Pré-requisitos

Instale o Python 3 e obtenha uma chave de API do Google Gemini.

### 2. Crie e ative um ambiente virtual

No PowerShell, dentro da pasta do projeto, execute:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 4. Configure a chave da API

Crie um arquivo chamado `.env` na raiz do projeto:

```env
MINHA_CHAVE=sua_chave_do_gemini
```

### 5. Execute o programa

```powershell
python Rotas.py
```

O programa consultará o Gemini, salvará as rotas recebidas em `rotas.txt`, imprimirá a matriz de adjacência e apresentará a lista numerada das cidades.

Escolha a origem e o destino digitando o índice ou o nome completo da cidade:

```text
Cidade de origem (indice ou nome): São Paulo
Cidade de destino (indice ou nome): Tóquio
```

Se existir um caminho, o terminal mostrará a sequência de cidades e uma janela será aberta com o grafo. Todas as rotas aparecerão em cinza e as arestas do caminho encontrado aparecerão em vermelho.

## Matriz de adjacência

Na matriz:

- `1` indica que existe uma rota direta entre as duas cidades;
- `0` indica que não existe uma rota direta.

Como o sentido das rotas é desconsiderado, a matriz é simétrica: se existe uma ligação entre as cidades `i` e `j`, tanto `matriz[i][j]` quanto `matriz[j][i]` recebem o valor `1`.

## Arquivos principais

- `Rotas.py`: consulta as rotas, cria a matriz e o grafo, procura o caminho e gera a visualização;
- `rotas.txt`: armazena a resposta mais recente recebida do Gemini;
- `requirements.txt`: lista as dependências necessárias;
- `.env`: contém a chave da API local e não é versionado.
