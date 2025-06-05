# Aprendendo API com FastAPI
## O que é uma API?
Uma API (Application Programming Interface ou Interface de Programação de Aplicações) é um conjunto de regras e definições que permite que diferentes sistemas, softwares ou aplicações se comuniquem entre si. Em termos simples, uma API age como um intermediário que facilita a interação entre diferentes programas.

### Principais Características de uma API
1. Interface Bem Definida:
    As APIs expõem funcionalidades de um sistema de maneira controlada e padronizada.

2. Abstração:
    O usuário da API não precisa conhecer os detalhes internos de como as funcionalidades são implementadas, apenas como utilizá-las.

3. Comunicação Padronizada:
    APIs geralmente usam protocolos bem estabelecidos, como HTTP/HTTPS, e formatos como JSON ou XML para troca de dados.

### Exemplos do Cotidiano
* **Aplicativos de clima:** Um aplicativo de previsão do tempo pode     usar a API de um serviço meteorológico para obter informações atualizadas.
* **Pagamentos online:** Serviços como PayPal ou Stripe oferecem APIs para que e-commerces possam integrar sistemas de pagamento.
* **Redes sociais:** APIs de plataformas como Twitter ou Instagram permitem que desenvolvedores acessem dados ou postem em nome dos usuários.


## Instalar dependências
Comando para instalar as dependências do projeto
> pip freeze -r requeriments.txt

## Iniciar servidor
> uvicorn main:app --reload

ou utilize o comando fastapi instale da seguinte forma para funcionar o comando fastapi
> pip install fastapi[standard]

Inicie o servidor em modo Dev em modo Development, recarrega automaticamente a cada vez que salva um arquivo
> fastapi dev

para produção
> fastapi run

### Parou o serviço e a porta continua sendo utilizada?
Isso acontece muito no MacOS quando se usa o `Control + z`, quando o correto deve utilizar é `Control + c`, caso aconteça isso rode o comando abaixo no terminal.
> kill -9 $(lsof -ti :8001)

### Acessar a documentação da API
No navegador acesse o ip que está rodando e foi printado no terminal e adicione o barramento '/docs'
> http://127.0.0.1:8000/docs

Lá você vai encontrar todos os endpoints que foram criados e poderá testar ali mesmo pelo Swagger

## Bibliotecas
### Black - Formatador de código
Formata o seu código e deixá-lo mais legivel e amigável.
Em caso de dúvidas utilize o comando para obter ajuda
> black --help

Para formatar todos os arquivos do projeto, o ponto '.' é conhecido como raiz do projeto
> black .

Para formatar apenas um arquivo
> black nome_do_arquivo.py


### Validate-docbr
É utilizada para gerar documentos válidos como CPF, CNPJ, PIS e etc
Com ele você pode gerar um documento, por padrão ao gerar o documento não é formatado, caso queira que venha formatado informe a 'mask' como verdadeiro
```py
from validate_docbr import CPF
CPF().generate(mask=True) # 123.456.789-10
```

### Faker
Faker é uma biblioteca para gerar nomes de usuários aleatórios
```py
from faker import Faker
fk = Faker()
print("Nome:", fk.name())
```
ou se prefirir, pode instalar a extensão 'vscode-faker' se caso for para coisa simples que não vá utilizar toda hora, pesquise o ID abaixo na aba de extensões do vscode
> deerawan.vscode-faker
