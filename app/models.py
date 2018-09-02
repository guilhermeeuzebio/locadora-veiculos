from app import db
from datetime import datetime
from sqlalchemy.orm import validates
from passlib.hash import bcrypt_sha256

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    senha_hash = db.Column(db.String, unique=False, nullable=False)
    
    #Encrypt password using bcrypt
    def hash_password(senha):
        return bcrypt_sha256.hash(senha)

    #Verify if the encrypted password in database is equals the password passed by the user
    def verify_password(senha, senha_hash):
        return bcrypt_sha256.verify(senha, senha_hash)

    """
    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')

        if Funcionario.query.filter(Funcionario.username == username).first():
            raise AssertionError('Username is already in use')

        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters')

        return username
    """

class Carro(db.Model):
    __tablename__ = 'carro'
    id = db.Column(db.Integer, primary_key=True) 
    modelo = db.Column(db.String(40), unique=False, nullable=False)
    placa = db.Column(db.String(8), unique=True, nullable=False) 
    ano = db.Column(db.Integer, unique=False, nullable=False)  
    renavam = db.Column(db.BigInteger, unique=True, nullable=False)
    disponivel = db.Column(db.Boolean, unique=False, nullable=False, default=True)
    frota = db.Column(db.Boolean, unique=False, nullable=False, default=True)
    alugar = db.relationship('Alugar', backref='car', lazy='dynamic')

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=False, nullable=False)
    telefone = db.Column(db.Integer, unique=True, nullable=False) 
    email = db.Column(db.String(40), unique=True, nullable=False)
    cpf_cnpj = db.Column(db.BigInteger, unique=True, nullable=True) 
    alugar = db.relationship('Alugar', backref='clien', lazy='dynamic')

class Alugar(db.Model):
    __tablename__ = 'alugar'
    id = db.Column(db.Integer, primary_key=True) 
    carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    checkin = db.Column(db.DateTime, default=datetime.utcnow)
    checkout = db.Column(db.DateTime)

    @validates('carro')
    def validate_carro(self, key, id):
        carro = Carro.query.filter(Carro.id==id).first()
        print(carro)
        if carro:
            if carro.disponivel == False:
                raise AssertionError('Carro informado não está disponível')                 
            if carro.frota == False:
                raise AssertionError('Carro informado não é mais parte da frota')                 
            else:
                Carro.query.filter(Carro.id==id).update({Carro.disponivel:False})
                db.session.commit()
                return carro.id
        else:
            raise AssertionError('Carro informado não faz parte da frota')            

    @validates('cliente')
    def validate_cliente(self, key, id):
        cliente = Cliente.query.filter(Cliente.id==id).first()
        print(cliente)
        if cliente:
            return cliente.id
        else:
            raise AssertionError('Cliente não cadastrado')            
