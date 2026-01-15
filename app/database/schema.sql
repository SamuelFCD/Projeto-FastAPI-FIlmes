CREATE TABLE filmes (
    filme_id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    ano INTEGER NOT NULL,
    genero VARCHAR(50) NOT NULL,
    diretor VARCHAR(100),
    duracao_min INTEGER,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE atores (
    ator_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);

CREATE TABLE filme_ator (
    filme_id INTEGER NOT NULL,
    ator_id INTEGER NOT NULL,
    PRIMARY KEY (filme_id, ator_id),
    FOREIGN KEY (filme_id) REFERENCES filmes(filme_id) ON DELETE CASCADE,
    FOREIGN KEY (ator_id) REFERENCES atores(ator_id) ON DELETE CASCADE
);
