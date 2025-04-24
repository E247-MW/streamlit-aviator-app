import streamlit as st
import hashlib

st.title("Seed Hash Analyzer & Odds Predictor")
st.write("Enter multiple client seeds (one per line). This tool hashes them using SHA-512 and evaluates risk levels based on leading decimal values.")

# Input box
seeds_input = st.text_area("Paste client seeds here:", height=200)

if seeds_input:
    seeds = seeds_input.strip().split("\n")

    st.subheader("Results:")
    for seed in seeds:
        seed = seed.strip()
        if not seed:
            continue

        hash_hex = hashlib.sha512(seed.encode()).hexdigest()
        first_hex = hash_hex[:13]
        decimal_value = int(first_hex, 16)

        # Extract first 2 digits of decimal for pattern logic
        first_digits = int(str(decimal_value)[:2])

        # Determine label and color
        if first_digits >= 90:
            risk = "HOT"
            color = "green"
        elif first_digits >= 70:
            risk = "WARM"
            color = "orange"
        else:
            risk = "COLD"
            color = "red"

        st.markdown(f"""
        <div style='border:1px solid #ccc;padding:10px;margin:10px 0;background-color:#f9f9f9'>
        <strong>Seed:</strong> {seed}  
        <br><strong>Hash:</strong> {hash_hex}  
        <br><strong>Decimal:</strong> {decimal_value}  
        <br><strong>Risk:</strong> <span style='color:{color}; font-weight:bold'>{risk}</span>
        </div>
        """, unsafe_allow_html=True)
