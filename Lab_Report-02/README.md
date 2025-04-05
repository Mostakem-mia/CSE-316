<h1>Lab Report-02</h1>

<h2>Code Description and Output</h2>

<h3 id="iddfs-maze">PROBLEM: You are given a 2D grid representing a maze, where each cell is either an empty space (0) or a wall (1). Your task is to implement a Python program that uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists from a given start cell to a specified target cell. You may move up, down, left, or right to adjacent empty cells, but you cannot pass through walls, and each cell may be visited only once during a single path exploration.</h3>
<p>This Python program uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists between a given start and target cell in a 2D grid maze. It explores paths by incrementally increasing the depth limit until a solution is found or the maximum depth is reached.</p>

<p><strong>Key Features:</strong></p>
<li><strong>Maze Representation:</strong></li>
<ol>
  <li>The maze is a 2D grid of 0s (empty) and 1s (walls).</li>
  <li>The start and target positions are user-defined coordinates.</li>
</ol>

<li><strong>IDDFS Algorithm:</strong></li>
<ol>
  <li>Combines the benefits of DFS and BFS by incrementally deepening the depth of exploration.</li>
  <li>Calls a depth-limited recursive DFS at each level.</li>
  <li>Only valid, unvisited neighbors are considered at each step.</li>
</ol>

<li><strong>Output and Traversal:</strong></li>
<ol>
  <li>If a path is found, the algorithm prints the path and the depth at which it was discovered.</li>
  <li>It prints the order of cell traversal.</li>
  <li>If no path exists within the max depth, it prints a failure message.</li>
</ol>

<p><strong>Example Input:(Case 01)</strong></p>
<pre>
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Enter start position (row col): 0 0
Enter goal position (row col): 2 3
</pre>

<p><strong>Example Output:(Case 01)</strong></p>
<pre>
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (0,1), (1,1), (2,1), (2,2), (2,3)]
</pre>

<p><strong>Example Input:(Case 02)</strong></p>
<pre>
3 3
0 1 0
0 1 0
0 1 0
Enter start position (row col): 0 0
Enter goal position (row col): 2 2
</pre>

<p><strong>Example Output:(Case 02)</strong></p>
<pre>
No path found within maximum depth limit of 9 using IDDFS
</pre>


<hr>

