# to-do-list
Imersão Django

Este é um projeto de gerenciamento de tarefas criado com Django, voltado para aprendizado e prática de desenvolvimento web com Python.

## Descrição
O projeto permite que usuários adicionem, editem, excluam e marquem tarefas como concluídas, promovendo a organização e produtividade. Utilizamos as melhores práticas de desenvolvimento com Django, incluindo modelagem de dados, views, templates e formulários.

## Tecnologias Utilizadas
- Django 5.1.2
- Python 3.12
- PostgreSQL
- Docker e Docker Compose
- Bootstrap 5
- Gunicorn
- Poetry para gerenciamento de dependências
- GitHub Actions para integração contínua

## Funcionalidades
- Adicionar tarefas
- Listar tarefas pendentes e concluídas
- Editar tarefas
- Remover tarefas
- Marcar tarefas como concluídas ou pendentes

## Estrutura do Projeto
- **Frontend**: Utiliza templates em Django com Bootstrap para estilização e responsividade.
- **Backend**: Desenvolvimento com Django, utilizando um modelo relacional para tarefas e autenticação de usuários.
- **Configuração de Deploy**: O projeto está configurado para rodar em contêineres Docker, incluindo serviços de backend, banco de dados (PostgreSQL) e Nginx como servidor proxy reverso.

## Como Configurar o Projeto
### Pré-requisitos
Certifique-se de ter as ferramentas abaixo instaladas:
- Python 3.12+
- Docker e Docker Compose
- Poetry

### Passos para Instalação
1. Clone o repositório:
   ```bash
   git clone <repositório_url>
   cd to-do-list
   ```

2. Configure as variáveis de ambiente criando um arquivo `.env` no formato esperado (verifique o `settings.py` e o `docker-compose.yml`).

3. Inicie os serviços com o Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Acesse o projeto no navegador:
   [http://localhost](http://localhost)

> **Dica**: Você também pode acessar o projeto na instância configurada do EC2. Use o link abaixo:
   [Projeto ao vivo](http://ec2-3-86-142-4.compute-1.amazonaws.com)

## Testes
Rode os testes para garantir que o projeto funcione corretamente:
```bash
poetry run pytest
```

## Contribuição
Fique à vontade para contribuir, enviando *issues* ou *pull requests*. Todo feedback e sugestão são bem-vindos!

---

### Links Úteis
- [Documentação do Django](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Poetry](https://python-poetry.org/)

### Contato
- E-mail: [gustavojuniordos@hotmail.com](mailto:gustavojuniordos@hotmail.com)
- Criado por: [Gustavo Junior Dos Santos no LinkedIn](https://www.linkedin.com/in/gustavo-junior-dos-santos/)

---