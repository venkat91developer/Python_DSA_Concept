Here is a comparison of common graph algorithms based on the types of graphs they are used on:

| **Algorithm**              | **Graph Type**                         | **Weighted Graph** | **Directed Graph** | **Undirected Graph** | **Graph Properties**                       |
|----------------------------|-----------------------------------------|--------------------|--------------------|----------------------|--------------------------------------------|
| **Depth First Search (DFS)**| All graph types                        | No                 | Yes                | Yes                  | Suitable for both cyclic and acyclic graphs |
| **Breadth First Search (BFS)**| All graph types                       | No                 | Yes                | Yes                  | Suitable for both cyclic and acyclic graphs |
| **Dijkstra's Algorithm**    | Weighted graphs                        | Yes                | Yes                | Yes                  | Requires non-negative weights              |
| **Bellman-Ford Algorithm**  | Weighted graphs                        | Yes                | Yes                | Yes                  | Handles negative weight edges              |
| **Floyd-Warshall Algorithm**| Weighted graphs                        | Yes                | Yes                | Yes                  | Computes shortest paths between all pairs  |
| **Kruskal's Algorithm**     | Undirected weighted graphs             | Yes                | No                 | Yes                  | Used to find the Minimum Spanning Tree     |
| **Prim's Algorithm**        | Undirected weighted graphs             | Yes                | No                 | Yes                  | Used to find the Minimum Spanning Tree     |
| **Kahn’s Algorithm**        | Directed Acyclic Graphs (DAG)          | No                 | Yes                | No                   | Topological Sorting                       |
| **Tarjan's Algorithm**      | All graph types                        | No                 | Yes                | Yes                  | Finds Strongly Connected Components        |
| **Kosaraju's Algorithm**    | Directed graphs                        | No                 | Yes                | No                   | Finds Strongly Connected Components        |
| **Disjoint Set (Union-Find)**| All graph types (used with Kruskal's)  | No                 | No                 | Yes                  | Helps detect cycles and connect components |
| **Topological Sort**        | Directed Acyclic Graphs (DAG)          | No                 | Yes                | No                   | Linear ordering of vertices                |

This table shows which graph types (directed, undirected, weighted, etc.) are applicable for each algorithm and what specific graph properties are relevant to their functionality.