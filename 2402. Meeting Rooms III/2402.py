class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Ordena as reuniões pelo horário de início
        meetings.sort()
        # Lista para manter as salas ocupadas com seus horários de liberação
        ocupadas = []        
        # Inicializa uma lista de salas livres, de 0 a n-1
        livres = list(range(n))       
        # Transforma a lista de salas livres em uma fila de prioridade (heap)
        heapify(livres)     
        # Lista para contar quantas vezes cada sala foi utilizada
        contador = [0] * n       
        # Itera sobre cada reunião na lista de reuniões
        for inicio, fim in meetings:
            # Libera as salas que estão ocupadas mas já estão disponíveis
            while ocupadas and ocupadas[0][0] <= inicio:
                # Reinsere a sala na lista de salas livres
                heappush(livres, heappop(ocupadas)[1])           
            if livres:
                # Retira a sala de menor índice da lista de livres
                i = heappop(livres)
                contador[i] += 1
                # Marca a sala como ocupada até o fim da reunião
                heappush(ocupadas, (fim, i))
            else:
                # Se não há salas livres, pega a próxima sala que ficará livre
                tempo_termino, i = heappop(ocupadas)
                contador[i] += 1
                # Marca a sala como ocupada até o novo horário de término ajustado
                heappush(ocupadas, (tempo_termino + fim - inicio, i))
        
        # Encontra a sala com o maior número de utilizações
        resposta = 0
        for i, valor in enumerate(contador):
            if contador[resposta] < valor:
                resposta = i
                return resposta