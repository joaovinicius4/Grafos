from google import genai
import os
from dotenv import load_dotenv
import networkx as nx
import matplotlib.pyplot as plt

load_dotenv()

MINHA_CHAVE = os.getenv("MINHA_CHAVE")

client = genai.Client(api_key=MINHA_CHAVE)

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Buenos Aires",
    "Santiago",
    "Lima",
    "Bogotá",
    "Cidade do México",
    "Nova York",
    "Toronto",
    "Los Angeles",
    "Londres",
    "Paris",
    "Madrid",
    "Roma",
    "Dubai",
    "Cairo",
    "Tóquio",
    "Pequim",
    "Sydney",
    "Joanesburgo"
]

prompt = f"""
Tenho estas 20 cidades:
{chr(10).join(cidades)}
Liste as rotas aéreas comerciais DIRETAS entre essas cidades.
Considere somente voos diretos entre duas das cidades da lista.
Retorne SOMENTE as rotas, uma por linha, exatamente neste formato:
São Paulo;Rio de Janeiro
São Paulo;Buenos Aires
Londres;Paris
Não escreva explicações.
Não use números.
Não coloque marcadores.
Não coloque código.
"""

resposta = client.models.generate_content(
    model="models/gemini-3.1-flash-lite",
     contents=prompt
)

texto_rotas = resposta.text

with open("rotas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_rotas)

print("Rotas recebidas do Gemini.")
print("Rotas salvas em rotas.txt")

N = len(cidades)
matriz = [[0 for _ in range(N)] for _ in range(N)]
for linha in texto_rotas.splitlines():

    linha = linha.strip()
    if ";" not in linha:
        continue

    origem, destino = linha.split(";", 1)
    origem = origem.strip()
    destino = destino.strip()

    if origem not in cidades or destino not in cidades:
        print("Rota ignorada:", linha)
        continue

    i = cidades.index(origem)
    j = cidades.index(destino)

    matriz[i][j] = 1
    matriz[j][i] = 1

print("CIDADES")

for i, cidade in enumerate(cidades):
    print(f"{i:2} - {cidade}")

print("MATRIZ DE ADJACÊNCIA")
print("     ", end="")

for i in range(N):
    print(f"{i:2}", end=" ")

print()

for i in range(N):

    print(f"{i:2}   ", end="")
    for j in range(N):
        print(f"{matriz[i][j]:2}", end=" ")

    print()

G = nx.Graph()

for i in range(len(cidades)):
    G.add_node(i, label=cidades[i])

for i in range(len(cidades)):
    for j in range(i + 1, len(cidades)):
        if matriz[i][j] == 1:
            G.add_edge(i, j)


def escolher_cidade(mensagem):
    while True:
        escolha = input(mensagem).strip()
        if escolha.isdigit():
            indice = int(escolha)
            if 0 <= indice < len(cidades):
                return indice
        for indice, cidade in enumerate(cidades):
            if escolha.casefold() == cidade.casefold():
                return indice
        print("Cidade invalida. Digite um indice da lista ou o nome completo.")

origem = escolher_cidade("Cidade de origem (indice ou nome): ")
destino = escolher_cidade("Cidade de destino (indice ou nome): ")

if nx.has_path(G, origem, destino):
    caminho = nx.shortest_path(G, origem, destino)
    arestas_caminho = list(zip(caminho, caminho[1:]))
    nomes_caminho = " -> ".join(cidades[indice] for indice in caminho)

    print("Existe um caminho entre as cidades, desconsiderando o sentido das rotas.")
    print("Caminho encontrado:", nomes_caminho)
else:
    caminho = []
    arestas_caminho = []
    print("Nao existe caminho entre as cidades, desconsiderando o sentido das rotas.")

pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=1000
)

nx.draw_networkx_edges(
    G,
    pos,
    edge_color="gray",
    width=1
)

labels = {i: cidades[i] for i in range(len(cidades))}
nx.draw_networkx_labels(
    G,
    pos,
    labels=labels,
    font_size=7
)

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=arestas_caminho,
    edge_color="red",
    width=3
)

plt.title("Grafo das Rotas Aéreas")
if caminho:
    plt.suptitle("Caminho destacado em vermelho", fontsize=10)
plt.axis("off")
plt.tight_layout()
plt.show()
