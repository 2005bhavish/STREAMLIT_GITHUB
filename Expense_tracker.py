import streamlit as st
import mysql.connector as a
import datetime 


def connect_db():
    try:
        return a.connect(
            host='localhost',
            port=3307,  
            user='root',
            passwd='admin',
            auth_plugin='mysql_native_password',
            database='expensetracker'
        )
    except a.Error as e:
        st.error(f"❌ Error connecting to MySQL: {e}")
        st.stop()

con = connect_db()


st.title("WLECOME TO EXPENSE TRACKER")
choose = st.radio("Select an option", ["ENTER THE DETAILS","VIEW THE DETAILS","VIEW SUMMARY"])

if choose == "ENTER THE DETAILS":
    st.subheader("➕ Enter your expense details")
    date = st.date_input("📅 Date")
    category = st.selectbox("📁 Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
    amount = st.number_input("💵 Amount", min_value=0.0, format="%.2f")

    if st.button("Submit Entry"):
        try:
            with con.cursor() as cur:
                cur.execute("""
                    INSERT INTO expense(date, category, amount) 
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        category = VALUES(category),
                        amount = VALUES(amount);
                """, (date, category, amount))
                con.commit()
            st.success("✅ Entry logged/updated successfully!")
        except a.Error as e:
            st.error(f"❌ Failed to insert entry: {e}")
        
if choose == "VIEW THE DETAILS":
    try:
        with con.cursor() as cur:
            cur.execute("""
                SELECT * FROM expense ORDER BY date DESC
            """)
            rows = cur.fetchall()

            for row in rows:
                st.subheader(f"Date: {row[0]}")
                st.write(f"Category: {row[1]}")
                st.write(f"Amount: ₹{row[2]:.2f}")

    except a.Error as e:
            st.error(f"❌ NO ENTRY FOUND {e}")


if choose == "VIEW SUMMARY":
    with con.cursor() as cur:
        cur.execute("""
            SELECT category, SUM(amount)
            FROM expense
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """)
        rows = cur.fetchall()

        st.subheader("💸 Summary by Category")

        for row in rows:
            st.write(f"{row[0]}: ₹{row[1]:.2f}")

    
