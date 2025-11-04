import * as vscode from "vscode";
import { execFile } from "child_process";
import * as path from "path";

export function activate(context: vscode.ExtensionContext) {
  const runCommand = vscode.commands.registerCommand("aspy.run", async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) return;
    const filePath = editor.document.fileName;

    const pythonPath = "python"; // assume Python in PATH
    const cliPath = path.join(context.extensionPath, "../cli/aspy_cli.py");

    execFile(pythonPath, [cliPath, filePath], (err, stdout, stderr) => {
      const panel = vscode.window.createOutputChannel("ASPY Output");
      panel.show(true);
      if (err) panel.appendLine(`Error: ${stderr}`);
      else panel.append(stdout);
    });
  });

  const showCommand = vscode.commands.registerCommand("aspy.showPython", async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) return;
    const code = editor.document.getText();

    const response = await fetch("http://localhost:5000/transpile", { // placeholder backend
      method: "POST",
      body: JSON.stringify({ code }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await response.text();
    vscode.window.showInformationMessage("Transpiled Python:\n" + data);
  });

  context.subscriptions.push(runCommand, showCommand);
}
