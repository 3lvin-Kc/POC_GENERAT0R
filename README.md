# Zero-Day/Exploit POC Generator CLI

A powerful, human-friendly CLI tool for generating proof-of-concept (POC) exploits for vulnerabilities using Large Language Models (LLMs) like OpenAI GPT-4 and Google Gemini.

## 🚀 Features
- **Step-by-step POC generation** for any CVE or vulnerability
- **Supports multiple LLMs:** OpenAI (GPT-4) and Gemini
- **Highly engineered prompts** for elite, code-only output
- **Flexible output formats:** Python, C, Bash, PowerShell, etc.
- **Simple, scriptable CLI interface**

## 🛠️ How It Works
1. You provide vulnerability details (CVE, description, advisory, target OS, output type) via CLI arguments.
2. The tool builds a detailed, context-rich prompt for the LLM.
3. The selected LLM generates a POC exploit, which is printed to your terminal.

## 📦 Installation & Setup
1. **Clone the repo and install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set your LLM API key(s):**
   - For OpenAI:
     ```bash
     export OPENAI_API_KEY=your-openai-api-key
     ```
   - For Gemini: (if using Gemini and not hardcoded)
     ```bash
     export GEMINI_API_KEY=your-gemini-api-key
     ```

## 📝 Usage
Run the CLI with required arguments:
```bash
python cli.py \
  --cve CVE-2023-12345 \
  --desc "Buffer overflow in XYZ" \
  --advisory "https://nvd.nist.gov/vuln/detail/CVE-2023-12345" \
  --target_os "Linux x86_64" \
  --output_type "python" \
  --llm openai
```

**Arguments:**
- `--cve`         : CVE identifier (e.g., CVE-2023-12345)
- `--desc`        : Short description of the vulnerability
- `--advisory`    : Advisory text or link (NVD, vendor, blog, etc.)
- `--target_os`   : Target OS/architecture/platform
- `--output_type` : Desired output format (Python, C, Bash, etc.)
- `--llm`         : LLM provider to use (`openai` or `gemini`)

## 🧠 How the Prompt Works
The tool uses a "God Mode" prompt template, instructing the LLM to:
- Output only code (no narrative)
- Parse and weaponize advisory details
- Provide multi-path, stealthy, and modular exploits
- Annotate assumptions and post-exploit steps

## 📁 Code Structure
- `cli.py`                : Main CLI entry point
- `prompts/prompt_engine.py` : Prompt template and builder
- `llm/openai_api.py`     : OpenAI API integration
- `llm/gemini_api.py`     : Gemini API integration
- `requirements.txt`      : Python dependencies

## 🛡️ Disclaimer
This tool is for educational and authorized security research purposes only. Use responsibly and legally.

## 🙏 Contributing
Pull requests and suggestions are welcome!

---

**Make your red-team, research, or learning workflow faster and more creative with LLM-powered POC generation!** 
