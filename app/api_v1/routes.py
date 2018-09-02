from app import db
from datetime import datetime
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from ..models import Admin, Cliente, Carro, Alugar

api_v1 = Blueprint('api_v1', __name__)


@api_v1.route('/registro_admin', methods=['POST'])
def register_admin():
	try:
		payload = request.get_json(silent=True)
		admin = Admin(username=payload['username'],
					senha_hash=Admin.hash_password(payload['senha']))
		db.session.add(admin)
		db.session.commit()
		#token = user.generate_confirmation_token()
		return jsonify({'sucesso': {'mensagem': 'conta de administrador criada'}}) 
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})


@api_v1.route('/login', methods=['POST'])
def login():
	try:
		
		if not request.is_json:
			return jsonify({"msg": "Missing JSON in request"}), 400

		username = request.json.get('username', None)
		senha = request.json.get('senha', None)
		
		if not username:
			return jsonify({"msg": "Missing username parameter"}), 400

		if not senha:
			return jsonify({"msg": "Missing password parameter"}), 400
		
		admin = Admin.query.filter_by(username=username).first()
	
		if admin is not None and Admin.verify_password(senha, admin.senha_hash):
			# Identity can be any data that is json serializable
			access_token = create_access_token(identity=username)
			return jsonify(access_token=access_token), 200
		else:
			return jsonify({"msg": "Bad username or password"}), 401

	except 	Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})

@api_v1.route('/registro_cliente', methods=['POST'])
@jwt_required
def registro_cliente():
	try:
		payload = request.get_json(silent=True)
		cliente = Cliente(nome=payload['nome'],
							telefone=payload['telefone'],
							email=payload['email'],
							cpf_cnpj=payload['cpf_cnpj'])
		db.session.add(cliente)
		db.session.commit()
		#token = user.generate_confirmation_token()
		return jsonify({'sucesso': {'mensagem': 'cliente foi cadastrado'}}) 
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})

@api_v1.route('/clientes', methods=['GET'])
@jwt_required
def get_clientes():
	try:
		clientes = Cliente.query.all()
		cliente_lista = []
		for cliente in clientes:
			data = {"id": cliente.id, "nome": cliente.nome, "telefone": cliente.telefone,
			 		"email": cliente.email, "cpf_cnpj": cliente.cpf_cnpj} 
			cliente_lista.append(data)
		return jsonify({"clientes": cliente_lista})
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})
	
@api_v1.route('/registro_carro', methods=['POST'])
@jwt_required
def registro_carro():
	try:
		payload = request.get_json(silent=True)
		carro = Carro(modelo=payload['modelo'],
						placa=payload['placa'],
						ano=payload['ano'],
						renavam=payload['renavam'])
		db.session.add(carro)
		db.session.commit()
		#token = user.generate_confirmation_token()
		return jsonify({'sucesso': {'mensagem': 'carro foi registrado'}}) 
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})

@api_v1.route('/carros', methods=['GET'])
@jwt_required
def get_carros():
	try:
		carros = Carro.query.all()
		carro_lista = []
		for carro in carros:
			data = {"id": carro.id, "modelo": carro.modelo, "placa": carro.placa,	"ano": carro.ano, 
				"renavam": carro.renavam, "disponivel": carro.disponivel, "frota": carro.frota} 
			carro_lista.append(data)
		return jsonify({"carros": carro_lista})
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})

@api_v1.route('/frota_update', methods=['PUT'])
@jwt_required
def update_frota():
	try:

		if not request.is_json:
			return jsonify({"msg": "Missing JSON in request"}), 400

		id = request.json.get('id', None)
		
		if not id:
			return jsonify({"msg": "Missing id parameter"}), 400

		Carro.query.filter_by(id=id).update({Carro.frota:False})
		db.session.commit()
		return jsonify({'sucesso': {'mensagem': 'carro foi retirado da frota'}}) 
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})

@api_v1.route('/checkin', methods=['POST'])
@jwt_required
def checkin():
	try:
		payload = request.get_json(silent=True)
		alugar = Alugar(carro=payload['carro_id'],
						cliente=payload['cliente_id'])
		db.session.add(alugar)
		db.session.commit()
		return jsonify({'sucesso': {'mensagem': 'registro de aluguel foi adicionado'}}) 
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})

@api_v1.route('/checkout', methods=['PUT'])
@jwt_required
def checkout():
	try:
		payload = request.get_json(silent=True)
		id = payload['id']
		date_time = datetime.utcnow()
		print(date_time)
		Alugar.query.filter_by(id=id).update({Alugar.checkout: date_time})
		db.session.commit()
		return jsonify({'sucesso': {'mensagem': 'checkout feito'}}) 
	except Exception as e:
		print('ERROR: {}'.format(e))
		return jsonify({'error': {'mensagem': 'servidor não obteve dados para processar'}, 'status': 400})




