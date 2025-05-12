README - Entrega de Backup do Banco de Dados

=================================================================

INFORMAÇÕES GERAIS

Utilizamos dados do Kaggle para alimentar nosso banco de dados PostgreSQL. 
Os dados foram transformados em comandos SQL por meio de um script em Python.
O backup do banco de dados inclui a estrutura (esquema) e todos os dados (registros) necessários para recriação completa do ambiente.

=================================================================

ESTRUTURA DA ENTREGA

- Criacao_Tabelas.sql — Arquivo contendo o esquema do banco (CREATE TABLE).
- insert_players.sql — Arquivo contendo os INSERTs da tabela Jogador.
- insert_torneios.sql — Arquivo contendo os INSERTs da tabela Torneio.
- insert_rankings.sql — Arquivo contendo os INSERTs da tabela Ranking.
- scripts/Geracao_Dados.py — Script Python que converte arquivos CSV em comandos SQL.
- README.txt — Instruções para execução e restauração, além de estatísticas do projeto.

=================================================================

FERRAMENTAS UTILIZADAS

- SGBD: PostgreSQL 16.X
- Interface gráfica: pgAdmin 4
- Linguagem de script: Python 3.x
- Fonte de dados (Kaggle):
  - Dataset: Huge Tennis Database
  - Link: https://www.kaggle.com/datasets/guillemservera/tennis

=================================================================

ESTATÍSTICAS DO BANCO DE DADOS

- Número de registros:
  - Jogador: XXX registros
  - Torneio: XXX registros
  - Ranking: XXX registros

- Tamanho total do BD (soma dos arquivos .sql):
  - Criacao_Tabelas.sql: XX KB
  - insert_players.sql: XX KB
  - insert_torneios.sql: XX KB
  - insert_rankings.sql: XX KB
  - Total: XX MB

=================================================================

COMO RESTAURAR O BANCO DE DADOS

OPÇÃO 1: Usando o pgAdmin 4

1. Abra o pgAdmin 4 e conecte-se ao seu servidor PostgreSQL.
2. Crie um novo banco de dados com o nome desejado.
3. Vá em "Tools > Query Tool".
4. Execute os seguintes arquivos na ordem:
   - Criacao_Tabelas.sql
   - insert_players.sql
   - insert_torneios.sql
   - insert_rankings.sql
5. Execute cada script clicando no botão de "executar".

OPÇÃO 2: Usando o terminal (psql)

psql -U [seu_usuario] -d [nome_do_banco] -f Criacao_Tabelas.sql  
psql -U [seu_usuario] -d [nome_do_banco] -f insert_players.sql  
psql -U [seu_usuario] -d [nome_do_banco] -f insert_torneios.sql  
psql -U [seu_usuario] -d [nome_do_banco] -f insert_rankings.sql

=================================================================

OBSERVAÇÃO SOBRE O ARQUIVO ZIP

O projeto foi compactado em um arquivo ZIP nomeado conforme solicitado:  
SBD_2025.1_G2_anne_daniella_felipe.zip

Ao descompactar, é criada uma pasta com o mesmo nome do ZIP, contendo:
- Arquivos .sql
- Pasta scripts/ com o script Python
- README.txt

Certifique-se de que a extração mantém essa estrutura de pastas.

=================================================================

O arquivo de backup excede 250 MB, portanto está disponível no link abaixo:
(!!!)

=================================================================
