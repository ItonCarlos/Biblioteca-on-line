from app import db, User, app
from app import User

# Criação de um novo contexto de aplicação
with app.app_context():
    # Criação de todas as tabelas
    db.create_all()

     #Criação de um usuário de teste
    username = "admin"
    password = "senha123"
    first_name = "Iton"
    last_name = "Sangaletti"
    role = "admin"
    is_admin = True
    admin = User(username=username, password=password,first_name=first_name,last_name=last_name,role=role,is_admin=is_admin)
    db.session.add(admin)
    db.session.commit()

    print(f"Usuário {username} criado com sucesso!")