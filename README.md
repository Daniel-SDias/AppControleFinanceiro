# AppControleFinanceiro

Aplicacao web em Flask para controle financeiro pessoal, com cadastro de transacoes, organizacao por categorias e estrutura preparada para dashboards.

## Versao

Versao atual: `0.1.0`

## Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- SQLite
- Tailwind CSS via CDN
- uv para ambiente e dependencias

## Estrutura

```text
webapp/
  blueprints/
    dashboard/
    home/
    transacoes/
  static/
  templates/
run.py
pyproject.toml
uv.lock
version.py
```

## Funcionalidades atuais

- Inicializacao da aplicacao via factory em `webapp/__init__.py`
- Banco SQLite criado automaticamente na primeira execucao
- Blueprint `home` com pagina inicial
- Blueprint `transacoes` com formulario de nova transacao e endpoint `POST` para gravacao
- Modelo `Transaction` relacionado ao modelo `Category`
- Estrutura inicial do `dashboard`, `movimentacoes` e `categorias`
- Interface com layout base, header global, favicon e formulario com Flatpickr

## Setup com uv

O projeto foi ajustado para usar `uv` no lugar de `poetry`.

### Requisitos

- `uv` instalado
- Python no path informado:
  `C:\Users\danie\AppData\Roaming\uv\python\cpython-3.12-windows-x86_64-none\python.exe`

### Instalar dependencias

```powershell
uv sync --python "C:\Users\danie\AppData\Roaming\uv\python\cpython-3.12-windows-x86_64-none\python.exe"
```

### Executar a aplicacao

```powershell
uv run python run.py
```

A aplicacao sobe em `http://127.0.0.1:5000`.

## Rotas principais

- `/` redireciona para `/home`
- `/home`
- `/dashboard/dashboard`
- `/transacoes/adicionar_transacao`
- `/transacoes/movimentacoes`
- `/transacoes/categorias`
- `/transacoes/add_transaction` com metodo `POST`

## Banco de dados

- O arquivo SQLite e criado automaticamente na primeira execucao
- A configuracao atual usa `sqlite:///database.db`
- Os modelos atuais sao `Transaction` e `Category`

## Estado atual

- O fluxo de criacao de transacoes ja existe
- Algumas paginas ainda estao em placeholder
- Ainda nao ha suite de testes automatizados no repositorio

## Historico

O resumo da evolucao do projeto esta em [CHANGELOG.md](CHANGELOG.md).
