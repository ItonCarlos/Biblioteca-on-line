from app import db, User, app
from app import User

# Criação de um novo contexto de aplicação
with app.app_context():
    # Criação de todas as tabelas
    db.create_all()

    # Criação de um usuário de teste
    username = "admin"
    password = "senha123"
    admin = User(username=username, password=password,first_name='iton',last_name='Sangaletti',role='Admin',is_admin=True)
    db.session.add(admin)
    db.session.commit()

    print(f"Usuário {username} criado com sucesso!")