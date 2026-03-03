# codefor

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

## Development

Install [PostgreSQL](https://formulae.brew.sh/formula/postgresql@18), [pgvector](https://github.com/pgvector/pgvector), and [uv](https://docs.astral.sh/uv/getting-started/installation/) (if necessary):

```bash
brew install postgresql@18
```

```bash
brew install pgvector
```

```bash
curl -LsSf https://astral.sh/uv/0.8.12/install.sh | sh
```

```bash
LC_ALL="en_US.UTF-8" /opt/homebrew/opt/postgresql@18/bin/postgres -D /opt/homebrew/var/postgresql@18
```

```bash
uv python install
```

```bash
uv venv
```

```bash
source .venv/bin/activate
```

```bash
uv pip install -r requirements.txt
```

```bash
python index.py
```

```bash
mypy
```

```bash
ruff check --fix
```

```bash
ruff format
```

```bash
deactivate
```
