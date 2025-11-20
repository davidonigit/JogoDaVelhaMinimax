# JogoDaVelhaMinimax

Implementação do algoritmo de IA Minimax para o jogo da velha em python. Pela característica e baixa complexidade do jogo, se torna impossível de vencer a IA, o máximo possível é empatar.

## Minimax

O algoritmo Minimax trabalha de forma recursiva, simulando todas as possibilidades do jogo até o fim. Nos turnos da IA, ele busca o maior score; nos turnos do oponente, ele assume que o oponente escolherá a jogada que resulta no menor score.

Sabendo de todos os possíveis casos, o algoritmo seleciona, para a jogada atual, aquela que garante o melhor resultado possível (score mais alto) vindo dessa árvore de possibilidades.
