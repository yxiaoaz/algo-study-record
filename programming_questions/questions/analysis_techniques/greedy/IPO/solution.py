import heapq

from programming_questions.utils.solution import Solution

class maximized_capital(Solution):
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = [(-profits[i], capital[i]) for i in range(len(profits))]
        projects = sorted(projects, key = lambda p: p[1])
        print(projects)
        heap = []

        # i is the pointer to the sorted (from smallest constraint to largest) project list
        # in each iteration, it stops at the project with the largest capital req. that fulfills the constraint
        i = 0
        while k > 0:
            # add all new (i.e. not in heap) and constraint-fulfilling projects' profits
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(heap, projects[i][0])
                i += 1
            
            # break if no capital available
            if len(heap) == 0:
                break

            selected_project_profit = - heapq.heappop(heap)
            w += selected_project_profit
            k -= 1

        return w