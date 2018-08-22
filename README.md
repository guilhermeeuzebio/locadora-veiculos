# locadora-veiculos
Repository with the code of a university work

## Documentation  

### Endpoints


/api/v1/registro_cliente        método: POST

```json
{
	"nome": "nome_do_cliente",
	"telefone": "número_de_telefone",
	"email": "endereço_email",
	"CPF": "cpf_do_cliente",
	"CNPJ": "cnpj_do_cliente"
}
```

Desses dados todos são obrigatórios, com exceção do CPF ou CNPJ.
Todos são tipo único, com exceção do nome.

/api/v1/listar_clientes        método: POST

Para listar um cliente específico algum dado único do mesmo deve ser passado (id, telefone, email, cpf, cnpj).

Exemplo:

```json
{
	"id": "número_de_id"
}
```

/api/v1/listar_clientes        método: GET

Lista todos os clientes trazendo todos seus dados.

/api/v1/registro_funcionario        método: POST

```json
{
	"username": "username_funcionário",
	"nome": "nome_do_funcionário",
	"senha": "senha_do_funcionário",
	"cpf": "cpf do funcionário",
	"telefone": "número_telefone_funcionário"
}
```

Desses dados todos são obrigatórios.
Todos são tipo único, com exceção do nome.


/api/v1/login        método: POST

```json
{
	"username": "username_funcionário",
	"senha": "senha_do_funcionário"
}
```

/api/v1/excluir_funcionario        método: DELETE

Para excluir um funcionário específico algum dado único do mesmo deve ser passado (id, telefone, cpf, username).

Exemplo:

```json
{
	"id": "número_de_id"
}
```

/api/v1/listar_funcionarios        método: GET

Lista todos os funcionários trazendo todos seus dados.

/api/v1/listar_funcionario        método: DELETE

Para listar um funcionário específico algum dado único do mesmo deve ser passado (id, telefone, cpf, username).

Exemplo:

```json
{
	"id": "número_de_id"
}
```

/api/v1/registro_carro        método: POST

```json
{
	"marca": "marca_carro",
	"modelo": "modelo_carro",
	"placa": "placa_carro",
	"cor": "cor_carro",
	"quantidade_assentos": "quantidade_de_assentos",
	"tipo_combustivel": "tipo_combustível",
	"km_rodados": "número_km_rodados",
	"ano": "ano_do_carro",
	"renavam": "número_do_renavam"
}
```

Desses dados todos são obrigatórios.
Apenas placa e renavam são tipo único.

/api/v1/listar_carro        método: GET

Para listar um carro específico algum dado único do mesmo deve ser passado (id, placa, renavam).

Exemplo:

```json
{
	"id": "número_de_id"
}
```

/api/v1/listar_carros        método: GET

Lista todos os carros da locadora, trazendo todos seus dados.

/api/v1/excluir_carro        método: DELETE

Para excluir um carro do cadastro algum dado único do mesmo deve ser passado (id, placa, renavam).

Exemplo:

```json
{
	"id": "número_de_id"
}
```

/api/v1/checkin



/api/v1/checkout


