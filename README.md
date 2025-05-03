# 🎮 Jogo da Forca em Python

Um clássico jogo da forca implementado em Python, onde o jogador deve adivinhar a palavra secreta em até 6 tentativas.

## 🚀 Como Executar

```bash
python jogo_da_forca.py
🔧 Configuração
Para alterar a palavra secreta, edite a variável no código:

python
palavra = ["E", "X", "C", "E", "S", "S", "O"]  # Altere para a palavra desejada
🎯 Regras do Jogo
Você tem 6 tentativas para adivinhar a palavra

Digite uma letra por vez

Letras corretas são reveladas na posição correspondente

Cada erro avança um estágio do desenho da forca

O jogo termina quando:

Você acerta a palavra completa (vitória!)

Ou esgota todas as tentativas (derrota)

✨ Recursos
Visualização do estado atual da forca

Lista de letras já tentadas

Conversão automática para maiúsculas

Feedback imediato sobre acertos/erros

📝 Estrutura do Código
palavra: Variável com a palavra secreta

HANGMANPICS: Arte ASCII dos estágios da forca

letras_usadas: Lista de tentativas do jogador

acertos: Progresso atual do jogador

📌 Observações
Todas as entradas são convertidas para maiúsculas

A palavra deve ser definida como lista de letras maiúsculas

O desenho da forca é exibido progressivamente a cada erro

Divirta-se! 🎉
