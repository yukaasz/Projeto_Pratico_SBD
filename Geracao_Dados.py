# import pandas as pd
# import psycopg2
# from psycopg2.extras import execute_values

# conn = psycopg2.connect(
#     dbname='sua_base',
#     user='postgres',
#     password='03042004',
#     host='localhost'
# )
# cur = conn.cursor()



# # Exemplo de inserção em massa para Jogador
# players_df = pd.read_csv('players.csv')[:10000]  # adapte conforme necessário
# data = [
#     (row['name'], 'direita', row['height'], row['ioc'])
#     for _, row in players_df.iterrows()
# ]

# query = """
#     INSERT INTO Jogador (nome_jogador, mao_dominante, altura, COI)
#     VALUES %s
# """
# execute_values(cur, query, data)



import pandas as pd
import os
import random
from glob import glob

caminho_dados = "./archive/tennis_atp"  # caminho para os CSVs

# -------------------- JOGADORES --------------------
def tabela_jogadores():
    insert_players = open("insert_players.sql", "w", encoding="utf-8")
    df_players = pd.read_csv(os.path.join(caminho_dados, "atp_players.csv"))

    jogadores = []
    for _, row in df_players.iterrows():
        if pd.notnull(row["player_id"]):
            id_jogador = int(row["player_id"])
            nome = f"{row['name_first']} {row['name_last']}".replace("'", "''") if pd.notnull(row["name_first"]) and pd.notnull(row["name_last"]) else 'NULL'
            mao = row["hand"] if pd.notnull(row["hand"]) else 'NULL'
            altura = int(row["height"]) if pd.notnull(row["height"]) else random.randint(165, 190) ##para cobrir os jogadores com altura NULL
            ioc = row["ioc"] if pd.notnull(row["ioc"]) else 'NULL'
            jogadores.append(id_jogador)

            insert_players.write(f"INSERT INTO Jogador (id_jogador, nome_jogador, mao_dominante, altura, COI) VALUES ({id_jogador}, '{nome}', '{mao}', {altura}, '{ioc}');\n")

    insert_players.close()
# -------------------- TORNEIOS --------------------
def tabela_torneios(arquivo_matches):

    df_matches = pd.read_csv(arquivo_matches, index_col=False)

    for _, row in df_matches.iterrows():
        try:
            id_torneio = row["tourney_id"]
            if id_torneio in torneios_vistos:
                continue
            torneios_vistos.add(id_torneio)


            nome = row["tourney_name"].replace("'", "''")

            categoria = row["tourney_level"]
            ano_valor = int(str(row["tourney_date"])[:4])

            insert_torneios.write(f"INSERT INTO Torneio (id_torneio, nome_torneio, categoria, ano) VALUES ('{id_torneio}', '{nome}', '{categoria}', {ano_valor});\n")
        except:
            continue

# # -------------------- RANKINGS --------------------

# insert_rankings = open("insert_rankings.sql", "w", encoding="utf-8")

# for ano in anos:
#     arquivo_ranking = os.path.join(caminho_dados, f"atp_rankings_{ano}.csv")
#     if not os.path.exists
# for ano in anos:
#     arquivo_ranking = os.path.join(caminho_dados, f"atp_rankings_{ano}.csv")
#     arquivo_matches = os.path.join(caminho_dados, f"atp_matches_{ano}.csv")

#     if not os.path.exists(arquivo_ranking) or not os.path.exists(arquivo_matches):
#         continue

#     df_rank = pd.read_csv(arquivo_ranking)
#     df_match = pd.read_csv(arquivo_matches)

#     # Converte datas
#     df_match['tourney_date'] = pd.to_datetime(df_match['tourney_date'], format='%Y%m%d', errors='coerce')
#     df_rank['ranking_date'] = pd.to_datetime(df_rank['ranking_date'], format='%Y%m%d', errors='coerce')

#     for _, rank_row in df_rank.iterrows():
#         id_jogador = rank_row['player']
#         pontos = rank_row['points']
#         data_ranking = rank_row['ranking_date']

#         if pd.isnull(data_ranking) or id_jogador not in jogadores:
#             continue

#         # encontra torneio mais próximo
#         matches_mesmo_ano = df_match[df_match['tourney_date'].dt.year == data_ranking.year]
#         torneios_compatíveis = matches_mesmo_ano[abs(matches_mesmo_ano['tourney_date'] - data_ranking) <= pd.Timedelta(days=7)]

#         if not torneios_compatíveis.empty:
#             id_torneio = torneios_compatíveis.iloc[0]["tourney_id"]
#             insert_rankings.write(f"INSERT INTO Ranking (id_jogador, id_torneio, pontos) VALUES ({id_jogador}, '{id_torneio}', {pontos});\n")

# insert_rankings.close()



if __name__ == "__main__":

    # tabela_jogadores()
    
    insert_torneios = open("insert_torneios.sql", "w", encoding="utf-8")
    
    torneios_vistos = set()

    #torneios simples
    anos_torneios_simples = range(1968, 2025) # intervalo aberto à direita, então acrescentamos 1 no fim do intervalo

    for ano in anos_torneios_simples:
        arquivo_matches_simples = os.path.join(caminho_dados, f"atp_matches_{ano}.csv")
        if not os.path.exists(arquivo_matches_simples):
            continue

        tabela_torneios(arquivo_matches_simples)

    #torneios duplos
    anos_torneios_duplos = range(2000, 2021)
    
    for ano in anos_torneios_duplos:
        arquivo_matches_duplos = os.path.join(caminho_dados, f"atp_matches_doubles_{ano}.csv")
        if not os.path.exists(arquivo_matches_duplos):
            continue

        tabela_torneios(arquivo_matches_duplos)
    
    
    #torneio amador
    arquivo_matches_amador = os.path.join(caminho_dados, f"atp_matches_amateur.csv")
    if os.path.exists(arquivo_matches_amador):
        tabela_torneios(arquivo_matches_amador)

    #torneios futures
    anos_torneios_futures = range(1991, 2025)
    
    for ano in anos_torneios_futures:
        arquivo_matches_futures = os.path.join(caminho_dados, f"atp_matches_futures_{ano}.csv")
        if not os.path.exists(arquivo_matches_futures):
            continue

        tabela_torneios(arquivo_matches_futures)
    
    #torneios quall chall

    anos_torneios_qual_chall = range(1978, 2025)
    
    for ano in anos_torneios_qual_chall:
        arquivo_matches_qual_chall = os.path.join(caminho_dados, f"atp_matches_qual_chall_{ano}.csv")
        if not os.path.exists(arquivo_matches_qual_chall):
            continue

        tabela_torneios(arquivo_matches_qual_chall)
    

    insert_torneios.close()
    
    # tabela_ranking()

    print("Arquivo inserts.sql gerado com sucesso.")