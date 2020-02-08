from pprint import pprint


def read_input():
    num_flights = int(input())
    return [tuple(input().split()) for _ in range(num_flights)], input() 



def solve(flights, strt):
    
    def _solve(flights, visited, current, path, all_paths):
        if len(path) == len(flights):
            all_paths.append(list(path)) 

        else:
            for flight in flights:
                if flight[0] == current and flight not in visited:
                    _solve(flights, set(visited) | {flight}, flight[1], list(path)+[flight], all_paths)
            path = [] 
            visited = set()

    all_ = [] 
    _solve(flights, set(), strt, [], all_)
    return all_

fl, strt = read_input()
pprint(solve(fl ,strt))
