import argparse
from prompts.prompt_engine import build_prompt
from llm.openai_api import generate_with_openai
from llm.gemini_api import generate_with_gemini

# entry point 

def main():
    # Set args parser for CLI
    parser = argparse.ArgumentParser(description="Zero-Day/Exploit POC Generator CLI")
    parser.add_argument('--cve', required=True, help='CVE identifier (e.g., CVE-2023-XXXX)')
    parser.add_argument('--desc', required=True, help='Vulnerability summary/description')
    parser.add_argument('--advisory', required=True, help='Advisory or leak content/link')
    parser.add_argument('--target_os', required=True, help='Target OS/Architecture/Platform')
    parser.add_argument('--output_type', required=True, help='Desired output format (C, Bash, Python, etc.)')
    parser.add_argument('--llm', choices=['openai', 'gemini'], default='openai', help='LLM provider to use (default: openai)')
    args = parser.parse_args()

    # Build the prompt  using user input
    prompt = build_prompt(
        cve=args.cve,
        desc=args.desc,
        advisory=args.advisory,
        target_os=args.target_os,
        output_type=args.output_type
    )

    # Call the selected LLM provider 
    if args.llm == 'openai':
        result = generate_with_openai(prompt)
    else:
        result = generate_with_gemini(prompt)

    # Output the generated POC to the user
    print("\n=== Generated POC ===\n")
    print(result)

if __name__ == "__main__":
    main() 