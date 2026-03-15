import util

class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def expand(self, state):
        util.raiseNotDefined()

    def getActions(self, state):
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        util.raiseNotDefined()

    def getNextState(self, state, action):
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from util import Stack
    frontier = Stack()
    frontier.push((problem.getStartState(), []))
    explored = set()

    while not frontier.isEmpty():
        state, path = frontier.pop()
        if problem.isGoalState(state):
            return path
        if state not in explored:
            explored.add(state)
            for successor, action, stepCost in problem.expand(state):
                if successor not in explored:
                    frontier.push((successor, path + [action]))
    return []

def breadthFirstSearch(problem):
    from util import Queue
    frontier = Queue()
    frontier.push((problem.getStartState(), []))
    explored = set()
    visited = set()

    while not frontier.isEmpty():
        state, path = frontier.pop()
        if problem.isGoalState(state):
            return path
        if state not in explored:
            explored.add(state)
            for successor, action, stepCost in problem.expand(state):
                if successor not in explored and successor not in visited:
                    frontier.push((successor, path + [action]))
                    visited.add(successor)
    return []

def uniformCostSearch(problem):
    from util import PriorityQueue
    frontier = PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    explored = dict()

    while not frontier.isEmpty():
        state, path = frontier.pop()
        cost = problem.getCostOfActionSequence(path)
        if problem.isGoalState(state):
            return path
        if state not in explored or cost < explored[state]:
            explored[state] = cost
            for successor, action, stepCost in problem.expand(state):
                new_path = path + [action]
                new_cost = problem.getCostOfActionSequence(new_path)
                if successor not in explored or new_cost < explored.get(successor, float('inf')):
                    frontier.push((successor, new_path), new_cost)
    return []

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    from util import PriorityQueue
    frontier = PriorityQueue()
    start = problem.getStartState()
    frontier.push((start, []), heuristic(start, problem))
    explored = dict()

    while not frontier.isEmpty():
        state, path = frontier.pop()
        cost = problem.getCostOfActionSequence(path)
        if problem.isGoalState(state):
            return path
        if state not in explored or cost < explored[state]:
            explored[state] = cost
            for successor, action, stepCost in problem.expand(state):
                new_path = path + [action]
                new_cost = problem.getCostOfActionSequence(new_path)
                if successor not in explored or new_cost < explored.get(successor, float('inf')):
                    priority = new_cost + heuristic(successor, problem)
                    frontier.push((successor, new_path), priority)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch