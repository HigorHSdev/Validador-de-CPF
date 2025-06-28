## 🧾 Validador de CPF – Projeto em Python

Este projeto é uma aplicação simples desenvolvida em Python com o objetivo de validar automaticamente números de CPF (Cadastro de Pessoa Física), utilizando lógica condicional e o algoritmo de verificação dos dígitos finais.

## 📌 Sobre o projeto
O CPF é um documento brasileiro que contém 11 dígitos, sendo os dois últimos chamados de dígitos verificadores. Esses dígitos seguem uma fórmula matemática específica que permite confirmar se o número foi gerado corretamente.

Este validador realiza esse cálculo de forma automática e informa se o CPF inserido é válido ou inválido.


## ✅ Funcionalidades do projeto
-🧹 Remove automaticamente pontos e traços do CPF digitado

-🔢 Verifica se o número possui 11 dígitos

-🚫 Detecta CPFs inválidos formados por dígitos repetidos (ex: 111.111.111-11)

-🧠 Realiza o cálculo dos dois dígitos verificadores conforme o algoritmo oficial

-📣 Informa se o CPF é válido com base nesses critérios


## 🚀 Como executar o projeto
-📥 Tenha o Python 3 instalado no computador

-🔗 Clone o repositório:
https://github.com/HigorHSdev/Validador-de-CPF.git

-📂 Acesse a pasta do projeto

-▶️ Execute o arquivo validador_cpf.py

-🖊️ Digite o CPF no terminal (com ou sem pontuação)

-✅ O sistema informará se o CPF é válido ou não

-💡 Exemplo de uso
```bash
Digite o CPF: 529.982.247-25  
✅ CPF Válido!
```

## 🛠️ Tecnologias utilizadas
-🐍 Python 3


## 📂 Organização do projeto
```bash
Validador-de-CPF/
├── src/                            # Código-fonte principal
│   └── validador_cpf.py           # Script de validação do CPF
│
├── tests/                         # (Opcional) Arquivos de teste automatizado
│   └── test_validador_cpf.py     # Testes unitários com pytest/unittest
│
├── docs/                          # Documentação adicional (futura)
│   └── explicacao_algoritmo.md   # Explicação do algoritmo de verificação
│
├── README.md                      # Documentação principal do projeto
├── LICENSE                        # Licença do projeto (MIT, por exemplo)
└── requirements.txt               # Dependências (opcional, caso use pacotes)

```


## 👨‍💻 Autor
-Desenvolvido por Higor Santana
🔗 GitHub: https://github.com/HigorHSdev
