# 📊 DataOps Mini Lab — Pipeline com Temporal e MongoDB

## 🚀 Descrição

Este projeto implementa um pipeline de dados completo utilizando Python, com geração de dados sintéticos, orquestração de workflow e persistência em banco de dados na nuvem.

O objetivo é simular um cenário real de engenharia de dados, onde dados são gerados, processados e armazenados de forma automatizada.

---

## 🧠 Arquitetura do Pipeline

O pipeline segue as seguintes etapas:

1. **Geração de dados**

   * Criação de um arquivo CSV sintético (~10MB)
   * Uso da biblioteca Faker

2. **Orquestração**

   * Execução controlada por workflow
   * Separação entre Workflow e Activities

3. **Persistência**

   * Inserção dos dados no MongoDB Atlas

4. **Agregação**

   * Cálculo de métricas por status de pedidos

---

## 🛠️ Tecnologias utilizadas

* Python 3.12
* pandas
* Faker
* Temporal.io (Python SDK)
* MongoDB Atlas
* PyMongo
* python-dotenv

---

## 📁 Estrutura do projeto

```
dataops-mini-lab/
├── data/
│   └── raw/
│       └── orders_fake_10mb.csv
├── app/
│   ├── activities.py
│   ├── workflows.py
│   ├── worker.py
│   ├── run_workflow.py
│   └── generate_fake_csv.py
├── docs/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuração

### 1. Criar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Configurar MongoDB Atlas

Crie um arquivo `.env` na raiz:

```env
MONGODB_URI=your_connection_string_here
```

---

### 4. Iniciar o Temporal

```bash
temporal server start-dev
```

---

## ▶️ Execução

### 1. Iniciar o Worker

```bash
python -m app.worker
```

---

### 2. Executar o Workflow

```bash
python -m app.run_workflow
```

---

## 📊 Resultado esperado

* Geração de arquivo CSV (~10MB)
* Inserção de dados no MongoDB Atlas
* Agregação por status de pedidos

Exemplo de saída:

```json
{
  "csv_path": "data/raw/orders_fake_10mb.csv",
  "load_result": "Inserted 84175 documents",
  "aggregation": [
    {"status": "cancelled", "total_orders": 21166},
    {"status": "processing", "total_orders": 21018}
  ]
}
```

---

## 🌐 Validação

### Temporal Web UI

Acesse: http://localhost:8233

### MongoDB Atlas

* Database: `dataops_lab`
* Collection: `orders_raw`

---

## 🧪 Objetivos alcançados

* Geração de dados sintéticos em escala
* Orquestração de pipeline com Temporal
* Persistência em banco de dados cloud
* Execução e monitoramento de workflows

---

## ⚠️ Limitações

Este projeto ainda não está pronto para produção. Melhorias necessárias:

* Tratamento de erros
* Retry automático
* Logs estruturados
* Monitoramento
* Validação de dados
* Segurança (credenciais)

---

## 👩‍💻 Autora

Projeto desenvolvido por Myllena Navarro Lins como prática de DataOps.

---
