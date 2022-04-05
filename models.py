class Jogos:

    def __init__(self, jogo, categoria, avaliacao):
        self.jogo = jogo
        self.categoria = categoria
        self.avaliacao = avaliacao

    def __str__(self) -> str:
        return f'Jogo: {self.jogo}, Categoria: {self.categoria}, Avaliacao: {self.avaliacao}'
