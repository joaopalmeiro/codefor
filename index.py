import psycopg
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    with psycopg.connect(dbname="postgres", autocommit=True) as conn:
        conn.execute("DROP DATABASE IF EXISTS codefor")
        conn.execute("CREATE DATABASE codefor")

    with psycopg.connect(dbname="codefor") as conn:
        conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        register_vector(conn)

        conn.execute("DROP TABLE IF EXISTS documents")
        conn.execute("CREATE TABLE documents (id bigserial PRIMARY KEY, content text NOT NULL, embedding vector(2048) NOT NULL)")

        model = SentenceTransformer(
            "voyageai/voyage-4-nano",
            trust_remote_code=True,
            truncate_dim=2048,
            revision="67fabc9bef010dabc5f6024aa1b1b6b93410426f",
        )

        documents = ['print("Hello, World!")']
        embeddings = model.encode_document(documents)

        for content, embedding in zip(documents, embeddings, strict=True):
            conn.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (content, embedding))

        for row in conn.execute("SELECT * FROM documents LIMIT 5"):
            print(row)
