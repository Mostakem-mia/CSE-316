<h1>Lab Report-03</h1>

<h2>Code Description and Output</h2>

<h2 id="graph-coloring">PROBLEM: You are given an undirected graph with N vertices and M edges. Your task is to implement a Python program that uses Backtracking to determine whether the graph can be colored using K colors such that no two adjacent vertices share the same color. The input will be read from a file, where the first line contains three integers: N (number of vertices, numbered from 0 to N−1), M (number of edges), and K (number of available colors). Each of the following M lines contains two integers u and v, representing an undirected edge between vertex u and vertex v.</h2>
<p>This Python program reads a graph from a file and checks if it can be colored using K colors such that no adjacent nodes share the same color. It uses a backtracking approach to try every possible valid assignment.</p>

<p><strong>Key Features:</strong></p>
<li><strong>Graph Input:</strong></li>
<ol>
  <li>Input is read from a file in the format: N (nodes), M (edges), K (colors).</li>
  <li>The next M lines represent edges between nodes.</li>
</ol>

<li><strong>Backtracking Coloring Algorithm:</strong></li>
<ol>
  <li>Assigns colors to each node recursively.</li>
  <li>Backtracks whenever a conflict is detected.</li>
  <li>Ensures no adjacent vertices share the same color.</li>
</ol>

<li><strong>Output:</strong></li>
<ol>
  <li>If a valid coloring is possible, it prints the color assignment.</li>
  <li>Otherwise, it indicates that coloring is not possible.</li>
</ol>

<p><strong>Example Input (input.txt):(Case 01)</strong></p>
<pre>
4 5 3
0 1
0 2
1 2
1 3
2 3
</pre>

<p><strong>Example Output:(Case 01)</strong></p>
<pre>
Coloring Possible with 3 Colors
Color Assignment: [1, 2, 3, 1]
</pre>

<p><strong>Example Input (input.txt):(Case 02)</strong></p>
<pre>
4 5 2
0 1
0 2
1 2
1 3
2 3
</pre>

<p><strong>Example Output:(Case 02)</strong></p>
<pre>
Coloring Not Possible with 2 Colors
</pre>
