import json
import re
import os

class AssameseTranspiler:
    """Transpiles Assamese (.aspy) code to Python code."""

    def __init__(self):
        self.mapping = self.load_mapping()

    def load_mapping(self):
        """Load Assamese → Python mapping from mapping.json"""
        mapping_path = os.path.join(os.path.dirname(__file__), "mapping.json")
        with open(mapping_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def transpile(self, code: str) -> str:
        """Replace Assamese tokens with Python equivalents (Unicode-safe)."""
        for assamese, python_kw in sorted(self.mapping.items(), key=lambda x: len(x[0]), reverse=True):
            # Match tokens surrounded by spaces, colons, parentheses, etc.
            code = re.sub(rf'(?<!\w){re.escape(assamese)}(?!\w)', python_kw, code)
        return code
