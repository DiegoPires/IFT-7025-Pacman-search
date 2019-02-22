# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

"""
Generic method to resolve search problem
"""
def ResolverSearch(problem, typePath, heuristic=nullHeuristic):
    empthPath = []
    priority = 0
    nodesToSearchWithPath = typePath
    nodesSearched = []
    
    if isinstance(typePath, util.PriorityQueue):
        nodesToSearchWithPath.push( (problem.getStartState(), empthPath, priority), priority)
    else:
        nodesToSearchWithPath.push( (problem.getStartState(), empthPath))

    while not nodesToSearchWithPath.isEmpty():
        if isinstance(typePath, util.PriorityQueue):
            nodeToVisite, actionToThisNode, priorityToThisNode = nodesToSearchWithPath.pop()
        else:
            nodeToVisite, actionToThisNode = nodesToSearchWithPath.pop()

        print nodeToVisite
        if problem.isGoalState(nodeToVisite):
            return actionToThisNode

        if nodeToVisite not in nodesSearched:
            nodesSearched.append(nodeToVisite)
            
            successors = problem.getSuccessors(nodeToVisite)
            for successor, action, stepCost in successors:
                independentActionToThisNode = actionToThisNode + [action]

                if isinstance(typePath, util.PriorityQueue):
                    independentPriorityToThisNode = priorityToThisNode + stepCost + heuristic(nodeToVisite, problem)
                    nodesToSearchWithPath.push((successor, independentActionToThisNode, independentPriorityToThisNode), independentPriorityToThisNode)
                else:
                    nodesToSearchWithPath.push((successor, independentActionToThisNode))
       
    return empthPath

""" Search the deepest nodes in the search tree first.
python2 pacman.py -l tinyMaze -p SearchAgent
python2 pacman.py -l mediumMaze -p SearchAgent
python2 pacman.py -l bigMaze -z .5 -p SearchAgent
"""
def depthFirstSearch(problem):
    return ResolverSearch(problem, util.Stack())

""" Search the shallowest nodes in the search tree first.
python2 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python2 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 --frameTime 0
python2 eightpuzzle.py
"""
def breadthFirstSearch(problem):
    return ResolverSearch(problem, util.Queue())
    
""" Search the node of least total cost first.
python2 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python2 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python2 pacman.py -l mediumScaryMaze -p StayWestSearchAgent
"""
def uniformCostSearch(problem):
    return ResolverSearch(problem, util.PriorityQueue())

""" Search the node that has the lowest combined cost and heuristic first.
python2 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
"""
def aStarSearch(problem, heuristic=nullHeuristic):
    return ResolverSearch(problem, util.PriorityQueue(), heuristic)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
