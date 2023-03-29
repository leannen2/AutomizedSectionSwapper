# AutomizedSectionSwapper

## Project Log

**Mar 28: Research & Brainstorm Algorithms to Implement**
[Johnson's Circuit Finding Algorithm](https://www.cs.tufts.edu/comp/150GA/homeworks/hw1/Johnson%2075.PDF) finds all simple cycles in graph in linear time.

Accomplished: 
1. Started Graph and Student classes

To Do: 
1. get_SCCs: function to find strongly connected components using Tarjan's algorithm
2. simple_cycles: function that finds simple cycles using Johnson's algorithm
3. unblock: helper function to get_simple_cycles that unblocks certain nodes following Johnson's algo
4. remove_node: helper function to get_simple_cycles that removes node from graph

## Brainstorm

1. Create Graph class
2. Create StudentNode class
3. Write/Find algorithm to find all simple cycles in graph (Idea: Johnson's Algo)
4. Write/Find algorithm to find the best combination of simple cycles that include the most number of StudentNodes
