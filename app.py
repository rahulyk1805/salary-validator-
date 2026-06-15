import streamlit as st
import tempfile
import os

from cleaner import process_salary_file

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Salary Validation Tool",
    page_icon="💰",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
# 💰 Salary Validation Tool

Validate salary files automatically using block-wise verification.

### Validation Rules

✔ Detect bold rows as block headers

✔ Sum all rows between two bold rows

✔ Compare sums against header values

✔ Validate all numeric columns independently

✔ Ignore final Grand Total row

✔ Process all sheets automatically

✔ Generate Validation_Report sheet
""")

st.divider()

# =====================================================
# FILE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "📂 Upload Salary File",
    type=["xls", "xlsx"]
)

# =====================================================
# PROCESS
# =====================================================

if uploaded_file:

    st.success(f"Selected File: {uploaded_file.name}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "File Size",
            f"{round(uploaded_file.size / 1024, 2)} KB"
        )

    with col2:
        st.metric(
            "File Type",
            uploaded_file.name.split(".")[-1].upper()
        )

    st.divider()

    if st.button(
        "🚀 Generate Validation Report",
        use_container_width=True
    ):

        with st.spinner("Processing Salary File..."):

            temp_dir = tempfile.mkdtemp()

            input_path = os.path.join(
                temp_dir,
                uploaded_file.name
            )

            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            try:

                output_file, mismatch_count = process_salary_file(
                    input_path
                )

                st.success(
                    f"Validation Completed | Total Mismatches: {mismatch_count}"
                )

                with open(output_file, "rb") as f:

                    st.download_button(
                        label="📥 Download Validated File",
                        data=f,
                        file_name=os.path.basename(output_file),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )

            except Exception as e:

                st.error(str(e))