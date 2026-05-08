import anthropic

client = anthropic.Anthropic(api_key="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")

print("=== SAR DRAFT TOOL ===")
name = input("Enter subject name: ")
amount = input("Enter transaction amount: $")
red_flag = input("Describe the red flag: ")
account = input("Enter account number: ")
country = input("Enter country of transaction: ")

prompt = f"""
You are a senior AML compliance officer with 15 years experience.
Draft a professional SAR narrative using FinCEN format with these exact sections:

SUBJECT INFORMATION:
- Name: {name}
- Account: {account}
- Transaction Amount: ${amount}
- Country: {country}

RED FLAGS IDENTIFIED:
- {red_flag}

Please structure your response with these sections:
1. SUBJECT INFORMATION
2. TRANSACTION DETAILS
3. RED FLAGS IDENTIFIED
4. NARRATIVE SUMMARY
5. RISK RATING (Low / Medium / High)
6. RECOMMENDED ACTION

Be specific, professional, and FinCEN compliant.
"""

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=2048,
    messages=[{"role": "user", "content": prompt}]
)

print("\n" + "="*50)
print("AI DRAFTED SAR NARRATIVE")
print("="*50)
print(message.content[0].text)
print("="*50)