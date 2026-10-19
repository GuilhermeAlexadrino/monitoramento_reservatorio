# Monitoramento de Reservatório de Água

Programa em Python que simula o monitoramento do nível de um reservatório de água. A cada leitura, o sistema mostra no terminal a situação atual do reservatório, com uma mensagem de alerta e uma cor que indica o grau de risco.

Projeto desenvolvido como atividade do curso técnico de Desenvolvimento de Sistemas.

## Objetivo

Praticar o uso de listas, funções e bibliotecas externas em Python, simulando um ambiente real de monitoramento.

## Níveis e cores

| Nível | Situação | Cor |
|-------|----------|-----|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Requisitos

- Python 3.8 ou superior
- Biblioteca colorama

## Instalação

Instale a biblioteca colorama com o comando:

```
pip install colorama
```

## Como executar

No terminal, dentro da pasta do projeto, rode:

```
python monitoramento_reservatorio.py
```

## Exemplo de saída

```
=== MONITORAMENTO DO RESERVATÓRIO ===

Leitura 1: Nível 3 - Médio: situação normal de operação.
Leitura 2: Nível 2 - Baixo: atenção, o reservatório está esvaziando.
Leitura 3: Nível 1 - Muito baixo (CRÍTICO): risco de falta de água!
Leitura 4: Nível 2 - Baixo: atenção, o reservatório está esvaziando.
Leitura 5: Nível 3 - Médio: situação normal de operação.
Leitura 6: Nível 4 - Alto: reservatório bem abastecido.
Leitura 7: Nível 5 - Muito alto (ALERTA): risco de transbordamento!
Leitura 8: Nível 4 - Alto: reservatório bem abastecido.

Monitoramento encerrado.
```

No terminal, cada mensagem aparece na cor correspondente ao seu nível.

## Como o código funciona

### Lista de mensagens

A lista `MENSAGENS` guarda as cinco mensagens de alerta, do nível 1 ao nível 5. Como listas em Python começam no índice 0, o nível 1 fica na posição 0, e por isso o código acessa a mensagem com `MENSAGENS[nivel - 1]`.

### Função `definir_cor(nivel)`

Recebe o nível (de 1 a 5) e retorna a cor correspondente da biblioteca colorama. Para um nível inválido, retorna branco, evitando que o programa quebre.

### Função `exibir_situacao(nivel)`

Busca a mensagem do nível na lista, obtém a cor com `definir_cor` e imprime a mensagem colorida. Se o nível estiver fora do intervalo de 1 a 5, exibe uma mensagem informando que a leitura é inválida.

### Função `main()`

Define a simulação com uma lista de leituras e percorre cada uma delas, exibindo a situação do reservatório. Ao final, restaura o estilo padrão do terminal.

### Restauração do terminal

Cada mensagem termina com `Style.RESET_ALL`, que desfaz a cor aplicada. Um reset adicional é feito ao fim do programa para garantir que o terminal volte ao normal.

## Personalização

A simulação usa valores definidos no próprio código, sem entrada de dados do usuário. Para testar outros cenários, altere a lista `leituras` dentro da função `main()`:

```python
leituras = [3, 2, 1, 2, 3, 4, 5, 4]
```

Qualquer sequência de números de 1 a 5 funciona.

## Conceitos praticados

- Listas e acesso por índice
- Criação e uso de funções
- Estruturas condicionais (`if`, `elif`, `else`)
- Laço de repetição com `for` e `enumerate`
- Importação e uso de bibliotecas externas (colorama)

## Observação

As cores aparecem normalmente em terminais comuns, como cmd, PowerShell e o terminal do VS Code. Alguns terminais embutidos em sites ou editores online podem não exibir as cores.

## Autor

Guilherme Alexandrino Menezes de Paula
