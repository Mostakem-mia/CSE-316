<h1>Lab Report-01<h1>

<h2>Code Description and Output</h2>

<h2 id="list-duplicates">PROBLEM: Write a program that generates a random N×N grid (N between 4 and 7) with non-obstacle source and goal states. It performs DFS to find a path from source to goal and prints the grid, source, goal, DFS path, and topological order of node traversal.</h2>
<p>This program generates a random 𝑁×𝑁 grid (where 𝑁 is between 4 and 7) consisting of open spaces (1s) and obstacles (0s). It then selects a random source and goal position, ensuring they are placed in open spaces. The program employs a Depth-First Search (DFS) algorithm to find a path from the source to the goal while keeping track of the traversal order.</p>
<p><strong>Key Features:</strong></p>
<li>Grid Generation:</li>
<ol>The program randomly selects 𝑁 between 4 and 7.</ol>
<ol>It creates an N×N grid with values of either 1 (open space) or 0 (obstacle).</ol>
<ol>The source and goal positions are chosen randomly from valid open spaces.</ol>
<li>Depth-First Search (DFS) Algorithm:</li>
<p><strong>Example Input:</strong></p>
<pre>list: [1,4,5,2,5,2,1,7,6,5,8,8,9]</pre>
<p><strong>Example Output:</strong></p>
 <pre><img src="images/1.png" alt="list" width="500"></pre>
