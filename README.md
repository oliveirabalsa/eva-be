# EVA - Backend da Plataforma de Gestão de Tarefas

## 📋 Visão Geral

Este repositório contém o código-fonte do backend da aplicação EVA, uma API REST desenvolvida com Django para suportar a plataforma de gestão de tarefas. O backend fornece endpoints para autenticação, gerenciamento de usuários e operações CRUD de tarefas.

## 🚀 Funcionalidades

- **Autenticação Segura**:
  - Autenticação baseada em JWT (JSON Web Token)
  - Endpoints para registro, login e refresh de token
- **Gerenciamento de Usuários**:
  - Cadastro de novos usuários
  - Perfis de usuário
- **API RESTful para Tarefas**:
  - Criação de tarefas
  - Listagem de tarefas com filtros
  - Atualização de tarefas (título, descrição, status)
  - Exclusão de tarefas
- **Filtros e Busca**:
  - Busca por título de tarefa
  - Filtragem por status

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Django**: Framework web
- **Django REST Framework**: Toolkit para construção de APIs
- **Simple JWT**: Autenticação via JWT
- **Djoser**: Endpoints adicionais de autenticação
- **SQLite**: Banco de dados
- **Django CORS Headers**: Configuração de CORS

## 📦 Estrutura do Projeto

- `myproject/`: Configurações principais do Django
  - `settings.py`: Configurações do projeto
  - `urls.py`: Mapeamento de URLs principal
- `myapp/`: Aplicação principal
  - `models.py`: Modelos de dados (User, Task)
  - `serializers.py`: Serialização de dados
  - `views.py`: Viewsets da API
  - `urls.py`: Rotas da API
- `manage.py`: Script de gerenciamento do Django
- `requirements.txt`: Dependências do projeto

## 🚀 Como Executar o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/oliveirabalsa/eva-be.git
   cd eva-be
   ```

2. **Crie e ative um ambiente virtual**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional)**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

7. **Acesse a API**:
   - A API estará disponível em: http://127.0.0.1:8000/
   - Admin do Django: http://127.0.0.1:8000/admin/

## 📡 Endpoints da API

- **Autenticação**:

  - `POST /auth/token/`: Obter token JWT
  - `POST /auth/token/refresh/`: Atualizar token JWT
  - `POST /users/`: Registrar novo usuário

- **Tarefas**:
  - `GET /tasks/`: Listar todas as tarefas
  - `POST /tasks/`: Criar nova tarefa
  - `GET /tasks/{id}/`: Detalhes de uma tarefa
  - `PUT /tasks/{id}/`: Atualizar uma tarefa
  - `DELETE /tasks/{id}/`: Excluir uma tarefa

## 🔧 Integração com o Frontend

Este backend foi projetado para funcionar com o frontend React da aplicação EVA. Para configurar a integração, certifique-se de que:

1. O frontend está configurado para acessar a URL correta da API
2. CORS está configurado corretamente no backend
3. As requisições do frontend incluem os tokens JWT necessários para autenticação

## 📝 Licença

Este projeto está licenciado sob a licença MIT.
