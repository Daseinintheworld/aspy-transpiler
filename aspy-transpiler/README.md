# 🐍 ASPY Transpiler — Assamese → Python

ASPY Transpiler is an experimental project that allows you to **write Python programs in Assamese language syntax**.  
It translates `.aspy` files (Assamese-style Python) into standard Python, executes them safely,  
and can be used from both **Command Line** and **Visual Studio Code**.

---

## 🚀 Features

✅ Assamese → Python transpilation  
✅ CLI execution (`aspy_cli`)  
✅ VS Code extension with syntax highlighting  
✅ Output panel and input() UI  
✅ Safe execution sandbox with timeout  
✅ Sample Assamese programs included  

---

## 🧩 Folder Structure

aspy-transpiler/
├── backend/
│ ├── init.py
│ ├── transpiler.py # Assamese → Python logic
│ ├── executor.py # Safe sandbox execution
│ ├── mapping.json # Assamese → Python token mapping
│ └── tests/
│ └── test_transpiler.py # Unit tests
│
├── cli/
│ └── aspy_cli.py # CLI entry point
│
├── vscode-extension/
│ ├── package.json # Extension manifest
│ ├── src/
│ │ ├── extension.ts # Register commands & connect to backend
│ │ ├── panel.ts # Output panel logic
│ │ └── inputUI.ts # Small input() UI
│ └── syntaxes/
│ └── aspy.tmLanguage.json # TextMate grammar for Assamese syntax
│
├── samples/
│ ├── loop.aspy
│ ├── function.aspy
│ └── fibonacci.aspy
│
├── README.md
└── requirements.txt

yaml
Copy code

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aspy-transpiler.git
cd aspy-transpiler
2. Create and Activate a Virtual Environment
bash
Copy code
python3 -m venv transpiler_venv
source transpiler_venv/bin/activate   # On Windows: transpiler_venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
💻 Running from CLI
You can run any .aspy file directly from the command line:

bash
Copy code
python -m cli.aspy_cli samples/loop.aspy
Example Assamese Code:

assamese
Copy code
চক্ৰ i ত সীমা(0, 5):
    প্ৰিন্ট(i)
Expected Output:

python
Copy code
🧩 Transpiled Python Code:
 for i in range(0, 5):
     print(i)

⚙️ Execution Output:
0
1
2
3
4
🧠 How It Works
The Transpiler (backend/transpiler.py) reads mapping.json
and replaces Assamese keywords with Python equivalents.

The Executor (backend/executor.py) safely runs the generated Python code in a sandbox.

Output is displayed in:

The terminal (CLI mode), or

The VS Code panel (extension mode).

🧭 VS Code Extension
Open the vscode-extension/ folder in VS Code.

Run npm install to install dependencies.

Press F5 in VS Code to launch the extension in a new “Extension Development Host”.

Create a .aspy file and type Assamese code, for example:

assamese
Copy code
কাৰ্য্য যোগফল(x, y):
    ফলাফল x + y

প্ৰিন্ট(যোগফল(3, 5))
Use Command Palette → Run Assamese Code
to see output in the bottom panel.

🔣 mapping.json Example
json
Copy code
{
  "চক্ৰ": "for",
  "ত": "in",
  "সীমা": "range",
  "প্ৰিন্ট": "print",
  "যদি": "if",
  "নতুবা": "else",
  "ফলাফল": "return",
  "কাৰ্য্য": "def"
}
🧪 Running Tests
bash
Copy code
pytest backend/tests/test_transpiler.py