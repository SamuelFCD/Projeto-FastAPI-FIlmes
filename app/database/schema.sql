

CREATE TABLE filmes (
    filme_id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ano INTEGER NOT NULL CHECK (ano > 0),
    diretor VARCHAR(100) NOT NULL,
    duracao_min INTEGER NOT NULL CHECK (duracao_min > 0),
    criado_em TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);