# Sistema Bancário Simples em Python

Este é um programa em Python que simula um sistema bancário básico com as operações de depositar, sacar e exibir extrato.

## Funcionalidades

- Depositar: Permite depositar valores positivos na conta bancária.
- Sacar: Permite fazer até 3 saques diários, com um limite máximo de R$ 500,00 por saque.
- Extrato: Exibe todos os depósitos e saques realizados na conta.

## Funcionamento

- O programa contém apenas um usuário.
- Todos os depósitos são armazenados em uma variável e exibidos na operação de extrato.
- O sistema verifica a disponibilidade de saques diários e respeita o limite máximo por saque.

## Como Executar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Baixe ou clone este repositório para a sua máquina.
3. Navegue até o diretório onde o código está localizado.
4. Execute o arquivo '**desafio-sistema-bancario.py**'.
5. Siga as instruções apresentadas no console para realizar as operações desejadas.

## Exemplo de Uso

``` python
# Exemplo de depósito
depositar(1000)  # Depositar R$ 1000,00

# Exemplo de saque
sacar(300)  # Sacar R$ 300,00

# Exemplo de extrato
exibir_extrato()  # Exibir todos os depósitos e saques realizados
```

## Limitações e Melhorias Futuras

- Este programa é uma versão inicial e possui limitações como ter apenas um usuário e armazenar os depósitos em uma variável.
- Para melhorias futuras, considere implementar o armazenamento em um banco de dados, permitir múltiplos usuários, entre outras funcionalidades.
