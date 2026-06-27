figsize=(12,6),
        title=f"{ticker}",
        returnfig=True
    )

    st.pyplot(fig2)

    # =============================
    # KIỂM ĐỊNH MANN-KENDALL
    # =============================

    close_prices = df["Close"].dropna().reset_index(drop=True)

    result = mk.original_test(close_prices)

    st.subheader("Kết quả kiểm định Mann-Kendall")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Trend",
            result.trend
        )

        st.metric(
            "Tau",
            round(result.Tau,4)
        )

    with col2:

        st.metric(
            "p-value",
            round(result.p,6)
        )

        st.metric(
            "Variance S",
            round(result.var_s,2)
        )

    st.markdown("---")

    if result.p < 0.05:

        if result.trend == "increasing":

            st.success(
                "Có xu hướng TĂNG có ý nghĩa thống kê (p < 0.05)."
            )

        elif result.trend == "decreasing":

            st.success(
                "Có xu hướng GIẢM có ý nghĩa thống kê (p < 0.05)."
            )

        else:

            st.success(
                "Có xu hướng đáng kể về mặt thống kê."
            )

    else:

        st.warning(
            "Không phát hiện xu hướng có ý nghĩa thống kê."
        )
