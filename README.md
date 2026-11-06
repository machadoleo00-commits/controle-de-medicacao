# 💊 Controle de Medicação

Aplicação web simples para cadastrar medicamentos de um tratamento e acompanhar, em uma tabela, **quanto tempo falta para a próxima dose** e **quanto tempo falta para o fim do tratamento**.

Projeto feito em Python com Flask e SQLite, como parte dos meus estudos de desenvolvimento de software. Tem foco em aprender conceitos de back-end: rotas, formulários, persistência em banco de dados, templates e cálculo com datas.

---

## 📋 Sumário

- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Como funciona o cálculo das doses](#-como-funciona-o-cálculo-das-doses)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Como executar](#-como-executar)
- [Banco de dados](#-banco-de-dados)
- [Rotas](#-rotas)
- [Limitações conhecidas](#-limitações-conhecidas)
- [Próximos passos](#-próximos-passos)
- [Autor](#-autor)

---

## ✅ Funcionalidades

- Cadastro de medicamento com **nome**, **doses por dia** (posologia) e **duração do tratamento em dias**.
- Registro automático da **data e hora de início** do tratamento no momento do cadastro.
- Listagem de todos os medicamentos em uma tabela com:
  - nome do medicamento;
  - doses por dia;
  - tempo restante até a próxima dose;
  - tempo restante até o fim do tratamento.
- Tratamento já concluído identificado na tabela, sem mostrar tempos negativos.
- Durações exibidas em português, sem microssegundos (por exemplo, `3 dias, 19:15:12`).
- Validação básica no formulário: campos obrigatórios e valores numéricos mínimos.

## 🛠 Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| Flask | Servidor web, rotas e templates |
| Jinja2 | Templates HTML (já incluso no Flask) |
| SQLite (`sqlite3`) | Banco de dados local, já incluso no Python |
| HTML e CSS | Interface |

## 🧮 Como funciona o cálculo das doses

O banco guarda a data de início do tratamento, e todos os tempos são calculados a partir dela:

- **Intervalo entre doses** = `24 horas ÷ doses por dia`. Com 3 doses por dia, o intervalo é de 8 horas.
- **Primeira dose** = início do tratamento + um intervalo.
- **Próxima dose** = primeira dose cujo horário ainda não passou, somando o intervalo dose a dose.
- **Fim do tratamento** = início + duração em dias.
- Se a próxima dose cairia depois do fim do tratamento, não há mais doses (a tabela mostra um traço).
- Se o fim já passou, a tabela mostra **Tratamento concluído**.

## 📁 Estrutura do projeto

```
medicamento/
├── app.py              # Aplicação Flask: rotas
├── database.py         # Acesso ao banco SQLite (criação da tabela e consultas)
├── funcoes.py          # Regras de negócio: cálculo de doses e formatação de tempo
├── templates/
│   ├── base.html       # Layout comum (menu e estilos)
│   ├── index.html      # Lista de medicamentos
│   └── add.html        # Formulário de cadastro
├── requirements.txt    # Dependências do projeto
├── .gitignore
└── README.md
```

O arquivo `tratamento.db` é criado automaticamente na primeira execução e não é versionado.

## 🚀 Como executar

### Pré-requisitos

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Passo a passo (Windows, PowerShell)

```powershell
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/controle-medicacao.git
cd controle-medicacao

# 2. (Opcional, recomendado) Criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
python app.py
```

### Linux ou macOS

```bash
git clone https://github.com/seu-usuario/controle-medicacao.git
cd controle-medicacao
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Depois, abra no navegador: **http://127.0.0.1:5000**

Para parar o servidor, use `Ctrl + C` no terminal.

> O app roda com `debug=True`, que recarrega o servidor ao salvar arquivos. Esse modo é apenas para desenvolvimento e não deve ser usado em produção.

## 🗄 Banco de dados

SQLite, arquivo `tratamento.db`, tabela `tratamento`:

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER (chave primária) | Identificador do registro |
| `medicamento` | TEXT | Nome do medicamento |
| `posologia` | INTEGER | Número de doses por dia |
| `tempo` | INTEGER | Duração do tratamento, em dias |
| `inicio` | TEXT | Data e hora de início (`AAAA-MM-DD HH:MM`) |

A tabela é criada automaticamente quando o `database.py` é importado.

## 🌐 Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Lista os medicamentos com o tempo até a próxima dose e o fim do tratamento |
| GET | `/add` | Exibe o formulário de cadastro |
| POST | `/add` | Recebe o formulário, grava no banco e redireciona para `/` |

## ⚠️ Limitações conhecidas

- Os cálculos buscam o medicamento pelo **nome**. Dois medicamentos com o mesmo nome podem se confundir. A solução planejada é trocar a busca pelo `id`.
- A primeira dose é considerada **um intervalo após o cadastro**, e não um horário escolhido pelo usuário.
- Os tempos são calculados quando a página carrega. Para atualizar, é preciso recarregar a página.
- Ainda não há autenticação: o app foi pensado para uso local e individual.

## 🗺 Próximos passos

- [ ] Editar medicamentos cadastrados
- [ ] Excluir medicamentos
- [ ] Alarme de dose com botão "já tomei" (janela de 10 minutos após o horário, com aviso de atraso até a confirmação)
- [ ] Escolher o horário da primeira dose no formulário
- [ ] Buscar medicamentos por `id` em vez de nome
- [ ] Atualização automática da tabela
- [ ] Testes automatizados

## 👤 Autor

**Leonardo Machado de Souza**

- LinkedIn: [leonardo-machado-de-souza](https://www.linkedin.com/in/leonardo-machado-de-souza-823953341/)

---

⚠️ **Aviso:** este é um projeto de estudo. Ele não substitui a orientação de um médico ou farmacêutico, e não deve ser a única forma de controlar o uso de medicamentos.
