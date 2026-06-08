import streamlit as st
import json

from parser import parser
from validator import is_valid
from duplicate_detector import detect_duplicates
from ai_analysis import analyse_duplicate

st.title("🏥 Insurance Claim Fraud Detection")

uploaded_file = st.file_uploader(
    "Upload Insurance Claim File"
)

if uploaded_file:

    records = []
    invalid_records = []

    lines = uploaded_file.readlines()

    for line in lines:

        line = line.decode("utf-8")

        parsed = parser(line)

        if not is_valid(parsed):
            invalid_records.append(parsed)
            continue

        records.append(parsed)

    duplicates = detect_duplicates(records)
    #st.write("Duplicates Raw:", duplicates)
    results = []

    for item in duplicates:

        pair = (
            item["record1"],
            item["record2"]
        )

        analysis = analyse_duplicate(pair)

        results.append({
            "record1": item["record1"],
            "record2": item["record2"],
            "similarity_score": round(
                item["similarity_score"],
                2
            ),
            "analysis": analysis
        })

    st.success("Analysis Complete ✅")
    st.metric(
        "Duplicate Claims Found",
        len(results)
    )

    st.metric(
        "Invalid Records",
        len(invalid_records)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Duplicate Claims Found",
            len(results)
        )

    with col2:
        st.metric(
            "Invalid Records",
            len(invalid_records)
        )

    st.divider()

    for index, item in enumerate(results, start=1):

        st.subheader(f"🚨 Duplicate Claim {index}")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### Claim 1")
            st.write(item["record1"])

        with col2:
            st.write("### Claim 2")
            st.write(item["record2"])

        score = item["similarity_score"]

        st.write("### Similarity Score")

        st.progress(score)

        st.write(f"Score: {score}")

        analysis = item["analysis"]

        st.write("### AI Fraud Analysis")

        st.write(
            f"✅ Duplicate Claim: {analysis.get('duplicate_claim')}"
        )

        st.write(
            f"⚠️ Possible Fraud: {analysis.get('possible_fraud')}"
        )

        st.write("### Fraud Indicators")

        for indicator in analysis.get(
            "fraud_indicators",
            []
        ):
            st.warning(indicator)

        st.write("### Recommended Action")

        st.error(
            analysis.get(
                "recommended_action"
            )
        )

        st.divider()
    