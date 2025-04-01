class BinarySearchWithCache:
    def __init__(self):
        # Inicializa o cache como um dicionário vazio
        self.cache = {}

    def binary_search(self, arr, target):
        """
        Método principal que verifica o cache antes de realizar a busca
        """
        # Cria uma chave única combinando o alvo e uma representação do array
        cache_key = f"{target}:{','.join(map(str, arr))}"
        
        # Verifica se o resultado está no cache
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Se não estiver no cache, realiza a busca binária
        result = self._binary_search_recursive(arr, target, 0, len(arr) - 1)
        
        # Armazena o resultado no cache antes de retornar
        self.cache[cache_key] = result
        return result

    def _binary_search_recursive(self, arr, target, left, right):
        """
        Implementação recursiva da busca binária
        """
        # Caso base: se os ponteiros se cruzarem, elemento não encontrado
        if left > right:
            return -1
        
        # Calcula o meio do intervalo
        mid = (left + right) // 2
        
        # Caso base: elemento encontrado
        if arr[mid] == target:
            return mid
        
        # Se o elemento é menor que o meio, busca na metade esquerda
        elif arr[mid] > target:
            return self._binary_search_recursive(arr, target, left, mid - 1)
        
        # Se o elemento é maior que o meio, busca na metade direita
        else:
            return self._binary_search_recursive(arr, target, mid + 1, right)

# Exemplo de uso
def main():
    # Cria uma instância da classe
    searcher = BinarySearchWithCache()
    
    # Array ordenado para teste
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Testa algumas buscas
    test_values = [7, 10, 3, 7]  # Inclui um valor repetido (7) para testar o cache
    
    for value in test_values:
        result = searcher.binary_search(arr, value)
        if result != -1:
            print(f"Valor {value} encontrado na posição {result}")
        else:
            print(f"Valor {value} não encontrado")
        
        # Mostra o estado atual do cache
        print(f"Cache atual: {searcher.cache}")
        print()

if __name__ == "__main__":
    main()