<h1> 📘 Simple Calculator </h1>

<p> A beginner-friendly Python calculator that supports basic arithmetic operations, exponentiation, modulo and division by zero. This project runs in a loop, allowing the user to perform multiple calculations until they choose to quit.</p>

<h2>✨ Features</h2>
<ul>
  <li>➕ Addition</li>
  <li>➖ Subtraction</li>
  <li>✖️ Multiplication</li>
  <li>➗ Division</li>
  <li>🧮 Modulo (does not support modulo by zero)</li>
  <li>🔼 Exponentiation (**)</li>
  <li>🔁 Continuous loop until the user asks to quit</li>
  <li>🛡️ Input validation for operation and numbers</li>
</ul>

<h2>🚀 How It Works</h2>
<ol>
  <li>The user is prompted to choose an operation.</li>
  <li>It then prompts for two numbers</li>
  <li>The selected operation is performed, and the result is printed</li>
  <li>
    If the user enters:
    <ul>
      <li>an invalid operator → they are asked again</li>
      <li>invalid numbers → they are asked again</li>
      <li>modulo by zero → error message</li>
      <li>division by zero → returns <strong>"Infinity"</strong></li>
    </ul>
  </li>
  <li>The loop continues until the user enters <strong>q</strong>.</li>
</ol>

<h2>🧩 Example Usage</h2>
<pre>
Choose an operation (+, -, *, /, %, **), or 'q' to quit: /
Enter first number: 4
Enter second number: 0
Result: Infinity
</pre>

<h2>📂 Project Structure</h2>
<pre>
Simple-Calculator.py
README.md
</pre>

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>Python 3.x</li>
  <li>Standard input/output</li>
  <li>Basic control flow (loops, conditionals, error handling)</li>
</ul>

<h2>📚 What I Learned</h2>
<ul>
  <li>Handling user input safely</li>
  <li>Preventing runtime errors (like modulo by zero)</li>
  <li>Custom logic for division by zero</li>
  <li>Building a loop-based interactive program</li>
  <li>Writing clean, readable, commented Python code</li>
</ul>

<h2>👩‍💻 Author</h2>
<p><strong>Cátia Barros</strong></p>

<p align="center">✨ Thank you for checking out my project! ✨</p>
