# 📋 Task Manager

Aplicação web de gerenciamento de tarefas desenvolvida com Python e Django.
Projeto prático criado para consolidar conhecimentos em desenvolvimento web back-end.

## 🔗 Acesse o projeto
👉 [task-manager-production-8322.up.railway.app](https://task-manager-production-8322.up.railway.app)

## ✅ Funcionalidades

- Cadastro e autenticação de usuários
- Criar, editar e excluir tarefas
- Definir prioridade (Alta, Média, Baixa) e prazo
- Filtrar tarefas por status e prioridade
- Mensagens de feedback em todas as ações
- Interface responsiva com Bootstrap 5

## 🛠️ Tecnologias utilizadas

- Python 3.13
- Django 6
- Bootstrap 5
- SQLite (desenvolvimento) 
- Git & GitHub
- Deploy: Railway

## 🚀 Como rodar localmente

```bash
git clone https://github.com/Tubelo/task-manager.git
cd task-manager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse http://127.0.0.1:8000

## 👨‍💻 Autor

Cristiano Serrano Tubelo Filho  
[GitHub](https://github.com/Tubelo) · [LinkedIn](https://www.linkedin.com/in/cristiano-serrano-tubelo-filho-2057801a8/)
