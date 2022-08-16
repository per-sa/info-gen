
# info-gen

Info-gen is a REST API to generate valid data

### Data Generators
for now:
- CPF : CPF(Cadastro de Pessoa Fisica) is the Brazilian individual taxpayer registry identification maintaned by Receita Federal Do Brasil.
- CNPJ: CNPJ(Cadastro Nacional da Pessoa Jurídica) is a nationwide registry of corporations, partnerships, foundations, investment funds, and other legal entities, created and maintained by the Receita Federal Do Brasil
- Cellphone Number: Brazilian cellphone numbers with DDD(Discagem Direta à Distância)

### Endpoints

CPF: `api/v1/cpf/`

CNPJ: `api/v1/cnpj/`

Cellphone Number: `api/v1/telephone/`


### Contribute
I think this is a tool that can be expanded in high levels, so if you think you can contribute with anything, follow these steps:

Clone the repo:
```bash
git clone https://github.com/matheusclmb/info-gen.git
```

Create a virtual env:
```bash
python -m venv env
```

Activate the env:
```bash
macOS: source env/bin/Activate
winOS: env\scripts\activate
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Make migrations:
```bash
python manage.py migrate
python manage.py makemigrations
```

Run:
```bash
python manage.py runserver
```

