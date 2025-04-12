# EVA - Plataforma de Gestão de Tarefas Colaborativa

EVA é uma aplicação web para gestão de tarefas colaborativa, desenvolvida com Django no backend e SQLite como banco de dados. A aplicação permite gerenciar tarefas com autenticação JWT, incluindo criação, leitura, atualização e exclusão de tarefas.

## 🚀 Funcionalidades

- **Autenticação de Usuários**: Login e registro com autenticação JWT.
- **Gestão de Tarefas**:
  - Criar novas tarefas.
  - Listar tarefas existentes com título, descrição, status e responsável.
  - Atualizar tarefas.
  - Excluir tarefas.
- **Busca**: Pesquise tarefas por título ou status.
- **Responsividade**: Interface amigável e responsiva.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python, Django, Django REST Framework (DRF), Djoser.
- **Banco de Dados**: SQLite.
- **Autenticação**: JWT (via Djoser).
- **Implantação**: Servidor EC2 da AWS.

---

## 📥 Como Clonar e Rodar o Projeto

### 1. Clone o Repositório
Use o comando abaixo para clonar o repositório:
```bash
git clone https://github.com/almir-ticarreiras/eva.git

Entre no diretório do projeto:
```bash
cd eva

### 2. Crie e Ative um Ambiente Virtual
Use o comando abaixo para criar o ambiente virtual:
```bash
python3 -m venv venv

Use o comando abaixo para ativar o ambiente virtual:
```bash
source venv/bin/activate

### 3. Instale as Dependências
Com o ambiente virtual ativo, instale as dependências listadas no arquivo requirements.txt usando o comando abaixo:
```bash
pip install -r requirements.txt

### 4. Configure o Banco de Dados
Use o comando abaixo para criar as migrações do banco de dados:
```bash
python3 manage.py makemigrations
python3 manage.py migrate

### 5. Inicie o Servidor de Desenvolvimento
Execute o servidor de desenvolvimento, através do seguinte comando:
```bash
python3 manage.py runserver

## A aplicação estará acessível no endereço: http://localhost:8000




