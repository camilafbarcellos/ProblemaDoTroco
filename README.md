# Resolução do Problema do Troco com Programação Dinâmica e Algoritmo Guloso

Este repositório contém a implementação em Python para resolver o **problema do troco** utilizando duas abordagens: **Programação Dinâmica** e **Algoritmo Guloso**. O problema consiste em determinar a quantidade mínima de moedas necessárias para dar o troco em um valor específico, dado um conjunto de moedas disponíveis.

## Sobre o Problema

O problema do troco é um clássico da área de algoritmos e otimização. Dado um valor inteiro representando um troco a ser dado, e um conjunto de moedas de diferentes valores, o objetivo é encontrar a menor quantidade de moedas que somadas resultam no troco desejado. Neste repositório, exploramos duas abordagens: **Programação Dinâmica** e **Algoritmo Guloso**.

## Implementações

### Programação Dinâmica

A abordagem de Programação Dinâmica utiliza uma tabela para armazenar a quantidade mínima de moedas necessárias para cada valor de troco. A tabela é preenchida gradualmente usando subproblemas menores para calcular o troco de valores maiores.

### Algoritmo Guloso

O Algoritmo Guloso aborda o problema escolhendo a maior moeda disponível sempre que possível, reduzindo gradualmente o valor do troco. Essa abordagem pode não garantir sempre a solução ótima, mas é rápida e muitas vezes oferece uma solução próxima do mínimo.

## Como Executar

1. Informe o valor do troco desejado.
> Caso desejado, você pode alterar a lista de moedas disponíveis
2. O programa irá calcular o troco necessário utilizando Programação Dinâmica e Algoritmo Guloso e irá exibir a quantidade e quais as moedas necessárias com cada abordagem.

**Aviso:** A abordagem de Algoritmo Guloso pode não funcionar em todos os cenários, especialmente quando as moedas disponíveis não formam um sistema canônico (como quando a moeda de valor 1 não está presente). Certifique-se de considerar os resultados cuidadosamente e ajustar as moedas disponíveis conforme necessário.

_© Camila Barcellos 2023 - IFSul_