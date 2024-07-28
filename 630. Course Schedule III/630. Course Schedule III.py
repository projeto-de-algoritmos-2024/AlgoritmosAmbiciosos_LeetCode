class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Ordenar os cursos pelo último dia possível em ordem crescente
        courses.sort(key=lambda x: x[1])
        max_heap = []
        total_time = 0
        
        for duration, last_day in courses:
            # Adiciona a duração do curso no heap
            heapq.heappush(max_heap, -duration)
            total_time += duration
            
            # Se o tempo total ultrapassar o último dia permitido para o curso
            if total_time > last_day:
                # Remove o curso mais longo (duração máxima)
                total_time += heapq.heappop(max_heap)
        
        return len(max_heap)

# Exemplo de uso
sol = Solution()
