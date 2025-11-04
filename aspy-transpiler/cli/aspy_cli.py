import argparse
from backend.executor import execute_safely
from backend.transpiler import AssameseTranspiler

def main():
    parser = argparse.ArgumentParser(description="Assamese → Python Transpiler CLI")
    parser.add_argument("file", help="Path to .aspy file")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        source = f.read()

    transpiler = AssameseTranspiler()
    py_code = transpiler.transpile(source)
    print("🧩 Transpiled Python Code:\n", py_code)
    print("\n⚙️ Execution Output:\n", execute_safely(py_code))

if __name__ == "__main__":
    main()
