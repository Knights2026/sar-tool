import streamlit as st
import anthropic

client = anthropic.Anthropic(api_key="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")

st.title("SAR Draft Tool")
st.subheader("AI-Powered Suspicious Activity Report Generator")

name = st.text_input("Subject Name")
amount = st.text_input("Transaction Amount ($)")
account = st.text_input("Account Number")
country = st.text_input("Country of Transaction")
red_flag = st.text_area("Describe the Red Flag")

if st.button("Generate SAR Narrative"):
    if name and amount and account and red_flag:
        with st.spinner("Drafting SAR narrative..."):
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

            st.success("SAR Narrative Generated!")
            st.markdown("---")
            st.markdown(message.content[0].text)
            st.markdown("---")
            st.caption("This document is confidential. Disclosure of SAR filing is prohibited under 31 U.S.C. § 5318(g)(2).")
    else:
        st.error("Please fill in all fields before generating.")