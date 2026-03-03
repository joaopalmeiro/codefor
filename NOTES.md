# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- pgvector:
  - https://github.com/pgvector/pgvector-python/blob/v0.4.2/examples/sentence_transformers/example.py
    - https://github.com/pgvector/pgvector-python/blob/v0.4.2/examples/sentence_transformers/requirements.txt
    - https://www.psycopg.org/install/
    - https://www.psycopg.org/psycopg3/docs/basic/usage.html#with-connection
    - https://www.psycopg.org/psycopg3/docs/basic/usage.html#main-objects-in-psycopg-3
  - https://github.com/pgvector/pgvector?tab=readme-ov-file#querying: "`<=>` - cosine distance"
- https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1: "(...) maps sentences & paragraphs to a 384 dimensional dense vector space (...)"
- https://huggingface.co/jinaai/jina-embeddings-v2-base-code
- https://stackoverflow.com/questions/70620960/how-to-create-a-database-using-psycopg3
- https://neon.com/postgresql/postgresql-administration/postgresql-show-databases
  - https://neon.com/postgresql/postgresql-administration/postgresql-show-tables
- https://www.postgresql.org/docs/current/sql-dropdatabase.html
- https://modal.com/blog/6-best-code-embedding-models-compared
- https://huggingface.co/spaces/mteb/leaderboard
- https://docs.mistral.ai/capabilities/embeddings/code_embeddings
  - https://mistral.ai/news/codestral-embed
- https://www.qodo.ai/products/code-embedding/
- https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models
- https://huggingface.co/jinaai/jina-embeddings-v4
- https://docs.vllm.ai/en/stable/models/supported_models/#embedding
- https://blog.voyageai.com/2026/01/15/voyage-4/
- https://huggingface.co/voyageai/voyage-4-nano:
  - "The `encode_query` and `encode_document` methods automatically prepend the `"Represent the query for retrieving supporting documents: "` and `"Represent the document for retrieval: "` prompts as defined in `config_sentence_transformers.json`, respectively."
  - "The default embedding dimension is 2048. To obtain lower-dimensional embeddings, you can use the `truncate_dim` argument in the `encode_query` and `encode_document` methods, or when initializing the model via the `truncate_dim` parameter. (...) The model supports 2048, 1024, 512, and 256-dimensional embeddings."
- https://huggingface.co/models?library=sentence-transformers&sort=trending
- https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b
  - https://huggingface.co/perplexity-ai/pplx-embed-v1-4b
  - https://arxiv.org/abs/2602.11151
  - "pplx-embed-v1 achieves competitive performance on the MTEB(Multilingual, v2), MTEB(Code), MIRACL, BERGEN, and ToolRet retrieval benchmarks (...)"
- https://huggingface.co/google/embeddinggemma-300m
- https://huggingface.co/models?library=sentence-transformers&sort=trending&search=code
- https://huggingface.co/models?library=sentence-transformers&sort=created&search=code
- https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-NOT-NULL

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```

### Show databases

```bash
/opt/homebrew/opt/postgresql@18/bin/psql -d postgres
```

```bash
\l+
```

```bash
\q
```
