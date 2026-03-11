import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Talking Rabbitt MVP", layout="wide")

# Title
st.title("Talking Rabbitt – Conversational Analytics MVP")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Show preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))
    
    # Question input
    question = st.text_input("Ask a question about your data:", placeholder="e.g., Which region has the highest revenue?")
    
    if question:
        question_lower = question.lower()
        
        # Answer section
        st.subheader("Answer")
        
        # Logic: Highest revenue by region
        if "highest revenue" in question_lower or "best" in question_lower or "most revenue" in question_lower:
            if "Region" in df.columns and "Revenue" in df.columns:
                revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
                top_region = revenue_by_region.index[0]
                top_revenue = revenue_by_region.iloc[0]
                
                st.write(f"**{top_region}** has the highest revenue with **${top_revenue:,.2f}**")
                
                # Bar chart
                fig, ax = plt.subplots(figsize=(10, 6))
                revenue_by_region.plot(kind='bar', ax=ax, color='steelblue')
                ax.set_title("Revenue by Region")
                ax.set_xlabel("Region")
                ax.set_ylabel("Revenue ($)")
                ax.tick_params(axis='x', rotation=45)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.error("Dataset must contain 'Region' and 'Revenue' columns")
        
        # Logic: Trend by quarter
        elif "trend" in question_lower or "quarter" in question_lower:
            if "Quarter" in df.columns and "Revenue" in df.columns:
                revenue_by_quarter = df.groupby("Quarter")["Revenue"].sum().sort_index()
                
                st.write(f"Revenue trend across quarters:")
                for quarter, revenue in revenue_by_quarter.items():
                    st.write(f"- **{quarter}**: ${revenue:,.2f}")
                
                # Line chart
                fig, ax = plt.subplots(figsize=(10, 6))
                revenue_by_quarter.plot(kind='line', ax=ax, marker='o', color='green', linewidth=2)
                ax.set_title("Revenue Trend by Quarter")
                ax.set_xlabel("Quarter")
                ax.set_ylabel("Revenue ($)")
                ax.grid(True, alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.error("Dataset must contain 'Quarter' and 'Revenue' columns")
        
        else:
            st.info("Try asking: 'Which region has the highest revenue?' or 'Show revenue trend by quarter'")
else:
    st.info("👆 Upload a CSV file to get started")
