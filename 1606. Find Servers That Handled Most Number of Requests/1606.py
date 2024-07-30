import heapq

from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        livres = SortedList(range(k)) 
        ocupados = []
        # Contador para registrar quantas vezes cada servidor foi usado
        contador = [0] * k
        # Processa cada requisição, com seus tempos de chegada (inicio) e carga (duracao)
        for i, (inicio, duracao) in enumerate(zip(arrival, load)):
            # Libera os servidores que terminaram suas tarefas até o tempo de início atual
            while ocupados and ocupados[0][0] <= inicio:
                # Adiciona o servidor de volta à lista de livres
                livres.add(ocupados[0][1])
                heapq.heappop(ocupados)
            
            # Se não há servidores livres, passa para a próxima requisição
            if not livres:
                continue
            
            # Encontra o primeiro servidor livre com índice maior ou igual a i % k
            j = livres.bisect_left(i % k)
            # Se j estiver fora do intervalo, reinicia a busca a partir do índice 0
            if j == len(livres):
                j = 0
            
            # Seleciona o servidor encontrado
            servidor = livres[j]
            # Incrementa o contador de uso para esse servidor
            contador[servidor] += 1
            # Adiciona o servidor à lista de ocupados com o tempo de término de sua tarefa
            heapq.heappush(ocupados, (inicio + duracao, servidor))
            # Remove o servidor da lista de livres
            livres.remove(servidor)
        
        # Encontra o número máximo de requisições atendidas
        maximo = max(contador)
        # Retorna a lista de servidores que atenderam o número máximo de requisições
        return [i for i, v in enumerate(contador) if v == maximo]