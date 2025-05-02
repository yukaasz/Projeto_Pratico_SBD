CREATE TABLE Jogador (  
  	ID_jogador INT PRIMARY KEY,
	nome_jogador VARCHAR(1000),
  	mao_dominante VARCHAR(10),
  	altura INT,
  	COI VARCHAR(10)
 );
 
CREATE TABLE Ranking (  
  	ID_jogador INT,
	ID_Torneio INT,
  	pontos INT,
	PRIMARY KEY(ID_jogador, ID_Torneio),
	FOREIGN KEY(ID_jogador) REFERENCES Jogador(ID_jogador)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY(ID_Torneio) REFERENCES Torneio(ID_Torneio)
		ON UPDATE CASCADE
		ON DELETE CASCADE
 );
 
CREATE TABLE Torneio (  
  	ID_Torneio VARCHAR(500) PRIMARY KEY,
	nome_torneio VARCHAR(500),
  	categoria VARCHAR(10),
  	ano INT
 );
