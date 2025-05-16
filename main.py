import streamlit as st
import seaborn as sns

def main():
    df = sns.load_dataset("titanic")
    st.dataframe(df)

if __name__ == "__main__":
    main()