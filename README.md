# locadora-veiculos
Repository with the code of a university work

## Documentation  

### How to use

Para usar o código deve ter python 3.6 instalado no computador.

Deve possuir instalado o pipenv, para instalar digite o comando no terminal:

pip install pipenv

Se estiver em ambiente Linux deve ter sudo no inicio e pip3, não pip

As seguintes variáveis de ambiente devem ser setadas no sistema que estiver usando:

Deve ter o PostgreSQL instalado

Após instalado, acesse com o seguinte comando:

psql -h localhost -U postgres

Digite a senha do mesmo

Crie um banco de dados, exemplo:

CREATE DATABASE locadora;

ENV=production

POSTGRES_USER=nome_do_usuário_do_banco 
POSTGRES_PW=senha_de_acesso_ao_banco
POSTGRES_URL=url_do_banco
POSTGRES_DB=nome_do_banco

Exemplo para setar as variáveis em ambiente Linux:

Digite no terminal

nano ~/.bashrc

Cole no arquivo .bashrc:

export ENV=production

export POSTGRES_USER=postgres
export POSTGRES_PW=123
export POSTGRES_URL=localhost
export POSTGRES_DB=locadora

Antes de rodar a aplicação entre no repositório e digite:

pipenv shell
pipenv install
flask db init
flask db migrate
flask db upgrade

Para rodar a aplicação:

flask run

### Endpoints

/api/v1/registro_admin        método: POST

Para registrar admin

```json
{
	"username": "admin",
	"senha": "admin",
}
```
/api/v1/login        método: POST

Para receber token e ter acesso a todos outros endpoints

```json
{
	"username": "admin",
	"senha": "admin",
}
```

/api/v1/registro_cliente        método: POST

Registrar cliente

```json
{
	"nome": "nome_do_cliente",
	"telefone": "número_de_telefone",
	"email": "endereço_email",
	"cpf_cnpj": "cpf_ou_cnpj_do_cliente"
}
```
Desses dados todos são obrigatórios.
Todos são tipo único, com exceção do nome.

/api/v1/clientes        método: GET

Para listar os clientes com todos seus respectivos dados.

/api/v1/registro_carro        método: POST

Para registrar um carro

```json
{
	"modelo": "modelo_carro",
	"placa": "placa_carro",
	"ano": "ano_do_carro",
	"renavam": "número_do_renavam"
}
```

Desses dados todos são obrigatórios.
Apenas placa e renavam são tipo único.

/api/v1/carros        método: GET

Para listar os carros com todos seus respectivos dados.


/api/v1/checkin        método: POST

Para fazer checkin

```json
{
	"carro_id": "número_de_id_carro",
	"cliente_id": "número_de_id_cliente"
}
```

/api/v1//frota_update        método: PUT

Para tirar um carro específico da frota

Exemplo:

```json
{
	"id": "número_de_id_carro"
}
```
/api/v1/checkout

Para fechar um checkin

Exemplo

```json
{
	"id": "número_de_id_checkin"
}
```