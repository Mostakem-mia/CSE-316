<h1>Lab Report-01</h1>

<h2>Code Description and Output</h2>

<h2 id="iddfs-maze">PROBLEM: Implement IDDFS to find a path in a 2D maze from a start to a target position, moving only through open cells (0s) and avoiding walls (1s).</h2>
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

<p><strong>Example Input:</strong></p>
<pre>
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3
</pre>

<p><strong>Example Output:</strong></p>
<pre>
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (0,1), (2,1), (2,2), (2,3)]
</pre>

<hr>

