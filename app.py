import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from tensorflow.keras.models import load_model


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Adaptive Zero-Day NIDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CYBER SECURITY CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800&family=Rajdhani:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
}

.stApp {

    background:
    radial-gradient(
        circle at 80% 10%,
        rgba(0,190,255,0.15),
        transparent 30%
    ),

    radial-gradient(
        circle at 10% 90%,
        rgba(60,0,255,0.14),
        transparent 30%
    ),

    linear-gradient(
        135deg,
        #020617,
        #06152e,
        #020617
    );

    color: #eaf6ff;
}


/* MAIN TITLE */

.main-title {

    font-family: 'Orbitron', sans-serif;

    font-size: 38px;

    font-weight: 800;

    letter-spacing: 3px;

    color: #00d9ff;

    text-shadow:
        0 0 8px #00d9ff,
        0 0 25px #0066ff;

    animation: glow 2s infinite alternate;
}


.subtitle {

    font-family: 'Rajdhani', sans-serif;

    font-size: 18px;

    letter-spacing: 3px;

    color: #8edcff;

}


/* GLOW ANIMATION */

@keyframes glow {

    from {

        text-shadow:
        0 0 5px #00d9ff,
        0 0 15px #0066ff;

    }

    to {

        text-shadow:
        0 0 15px #00d9ff,
        0 0 35px #0088ff;

    }

}


/* CARDS */

.cyber-card {

    background:
    linear-gradient(
        145deg,
        rgba(8,32,65,0.95),
        rgba(2,10,25,0.97)
    );

    border:

        1px solid
        rgba(0,200,255,0.35);

    border-radius: 18px;

    padding: 22px;

    margin-bottom: 18px;

    box-shadow:

        0 0 20px
        rgba(0,150,255,0.08),

        inset 0 0 20px
        rgba(0,150,255,0.03);

    transition: 0.3s;
}


.cyber-card:hover {

    transform: translateY(-3px);

    border-color: #00d9ff;

    box-shadow:

        0 0 30px
        rgba(0,200,255,0.25);

}


/* CARD TITLE */

.card-title {

    font-family: 'Orbitron', sans-serif;

    color: #00d9ff;

    font-size: 16px;

    font-weight: 700;

    letter-spacing: 2px;

    margin-bottom: 15px;

}


/* RISK NUMBER */

.risk-number {

    font-family: 'Orbitron', sans-serif;

    font-size: 60px;

    font-weight: 800;

    text-align: center;

    color: #00e5ff;

    text-shadow:
        0 0 15px #00d9ff,
        0 0 30px #0066ff;

}


.risk-label {

    text-align: center;

    font-family: 'Orbitron', sans-serif;

    font-size: 18px;

    letter-spacing: 3px;

}


/* MODEL ROW */

.model-row {

    padding: 13px;

    margin: 8px 0;

    border-radius: 10px;

    background:
        rgba(0,120,200,0.08);

    border-left:
        3px solid #00cfff;

}


.model-name {

    font-family: 'Orbitron', sans-serif;

    color: #c9efff;

    font-weight: 600;

}


.model-status {

    float: right;

    font-weight: 700;

}


.status-online {

    color: #00ffb3;

    text-shadow:
        0 0 10px #00ffb3;

}


.status-alert {

    color: #ff5277;

    text-shadow:
        0 0 10px #ff5277;

}


/* SECTION */

.section-title {

    font-family: 'Orbitron', sans-serif;

    color: white;

    font-size: 22px;

    letter-spacing: 2px;

    margin-top: 20px;

}


/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:

    linear-gradient(
        180deg,
        #020817,
        #06152e,
        #020817
    );

    border-right:
        1px solid
        rgba(0,190,255,0.25);

}


section[data-testid="stSidebar"] * {

    color: #cceeff;

}


/* BUTTON */

.stButton > button {

    background:

    linear-gradient(
        90deg,
        #005eff,
        #00bfff
    );

    color: white;

    border: none;

    border-radius: 10px;

    font-family: 'Orbitron', sans-serif;

    font-weight: 600;

    letter-spacing: 1px;

    box-shadow:
        0 0 15px
        rgba(0,150,255,0.3);

}


.stButton > button:hover {

    box-shadow:
        0 0 25px
        rgba(0,200,255,0.7);

    transform: scale(1.02);

}


/* METRICS */

[data-testid="stMetric"] {

    background:
        rgba(4,25,52,0.8);

    border:
        1px solid
        rgba(0,180,255,0.2);

    padding: 15px;

    border-radius: 12px;

}


/* DIVIDER */

hr {

    border-color:
        rgba(0,180,255,0.2);

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODELS
# =========================================================

@st.cache_resource
def load_models():

    iso_model = joblib.load(
        "models/isolation_forest.pkl"
    )

    xgb_model = joblib.load(
        "models/xgboost_model.pkl"
    )

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    # Try different possible LSTM filenames
    lstm_model = None

    possible_files = [
        "models/lstm_autoencoder.keras",
        "models/lstm_autoencoder.h5",
        "models/lstm_model.keras",
        "models/lstm_model.h5"
    ]

    for file in possible_files:

        if os.path.exists(file):

            lstm_model = load_model(file)

            break

    return (
        iso_model,
        xgb_model,
        scaler,
        lstm_model
    )


iso_model, xgb_model, scaler, lstm_model = load_models()


# =========================================================
# LOAD CICIDS DATA
# =========================================================

@st.cache_data
def load_data():

    # IMPORTANT:
    # Do NOT load all 2.5 million rows.

    df = pd.read_csv(
        "data/cleaned_CICIDS2017_EDA.csv",
        nrows=50000
    )

    df.columns = df.columns.str.strip()

    return df


df = load_data()


# =========================================================
# PREPARE FEATURES
# =========================================================

X_data = df.drop(
    columns=[
        "Label",
        "Traffic_Type"
    ],
    errors="ignore"
)


# Only numerical features

X_data = X_data.select_dtypes(
    include=np.number
)


# Remove infinity

X_data = X_data.replace(
    [np.inf, -np.inf],
    np.nan
)


# Remove missing values

X_data = X_data.dropna()


# Keep EXACT features used by scaler

X_data = X_data[
    scaler.feature_names_in_
]


X_data = X_data.reset_index(
    drop=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-title">
    🛡 ADAPTIVE ZERO-DAY NIDS
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="subtitle">
    MULTI-MODEL NETWORK THREAT INTELLIGENCE SYSTEM
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("---")


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
        font-family:Orbitron;
        font-size:20px;
        color:#00d9ff;
        letter-spacing:2px;">
        ⚙ NIDS CONTROL
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")


    # Risk threshold

    threshold = st.slider(
        "Risk Threshold",
        10,
        90,
        60
    )


    # Live monitoring

    live_mode = st.toggle(
        "🔴 Live Monitoring",
        True
    )


    st.markdown(
        "### Active Models"
    )


    use_iso = st.checkbox(
        "🌲 Isolation Forest",
        True
    )


    use_xgb = st.checkbox(
        "🌳 XGBoost",
        True
    )


    use_lstm = st.checkbox(
        "🧠 LSTM Autoencoder",
        lstm_model is not None
    )


    st.markdown("---")


    st.markdown(
        """
        <div style="
        color:#00ffb3;
        font-family:Orbitron;
        font-size:14px;">
        ● SYSTEM ONLINE
        </div>
        """,
        unsafe_allow_html=True
    )


    st.caption(
        "Adaptive threat monitoring enabled"
    )


# =========================================================
# NETWORK FLOW SELECTOR
# =========================================================

st.markdown(
    """
    <div class="section-title">
    🔎 NETWORK FLOW ANALYZER
    </div>
    """,
    unsafe_allow_html=True
)


flow_number = st.slider(
    "Select CICIDS2017 Network Flow",
    0,
    len(X_data) - 1,
    0
)


sample = X_data.iloc[
    [flow_number]
]


sample_scaled = scaler.transform(
    sample
)


# =========================================================
# MODEL PREDICTIONS
# =========================================================

iso_result = 0

xgb_result = 0

lstm_result = 0


# =========================================================
# ISOLATION FOREST
# =========================================================

if use_iso:

    iso_prediction = iso_model.predict(
        sample_scaled
    )[0]


    if iso_prediction == -1:

        iso_result = 1

    else:

        iso_result = 0


# =========================================================
# XGBOOST
# =========================================================

xgb_probability = 0


if use_xgb:

    xgb_prediction = xgb_model.predict(
        sample
    )[0]


    xgb_probability = (
        xgb_model.predict_proba(
            sample
        )[0][1]
    )


    xgb_result = int(
        xgb_prediction
    )


# =========================================================
# LSTM AUTOENCODER
# =========================================================

lstm_error = 0


if use_lstm and lstm_model is not None:

    timesteps = 10


    # Create a 10-flow window

    start = max(
        0,
        flow_number - timesteps + 1
    )


    end = start + timesteps


    sequence = X_data.iloc[
        start:end
    ]


    if len(sequence) == timesteps:

        sequence_scaled = scaler.transform(
            sequence
        )


        sequence_scaled = sequence_scaled.reshape(
            1,
            timesteps,
            sequence_scaled.shape[1]
        )


        reconstructed = lstm_model.predict(
            sequence_scaled,
            verbose=0
        )


        lstm_error = np.mean(
            np.square(
                sequence_scaled -
                reconstructed
            )
        )


        # Simple anomaly signal

        if lstm_error > 1.0:

            lstm_result = 1

        else:

            lstm_result = 0


# =========================================================
# RISK SCORES
# =========================================================


# ---------- Isolation Forest Risk ----------

iso_score = iso_model.decision_function(
    sample_scaled
)[0]


iso_risk = np.clip(
    (0.5 - iso_score) * 100,
    0,
    100
)


# ---------- XGBoost Risk ----------

xgb_risk = (
    xgb_probability * 100
)


# ---------- LSTM Risk ----------

lstm_risk = np.clip(
    lstm_error * 50,
    0,
    100
)


# =========================================================
# ACTIVE MODEL COUNT
# =========================================================

active_models = sum(
    [
        use_iso,
        use_xgb,
        use_lstm
    ]
)


if active_models > 0:

    base_risk = (

        (iso_risk if use_iso else 0)

        +

        (xgb_risk if use_xgb else 0)

        +

        (lstm_risk if use_lstm else 0)

    ) / active_models

else:

    base_risk = 0


# =========================================================
# MODEL CONSENSUS
# =========================================================

votes = (

    (iso_result if use_iso else 0)

    +

    (xgb_result if use_xgb else 0)

    +

    (lstm_result if use_lstm else 0)

)


if active_models > 0:

    consensus_risk = (
        votes /
        active_models
    ) * 100

else:

    consensus_risk = 0


# =========================================================
# FINAL ADAPTIVE RISK
# =========================================================

final_risk = (

    0.75 * base_risk

    +

    0.25 * consensus_risk

)


final_risk = np.clip(
    final_risk,
    0,
    100
)


# =========================================================
# RISK LEVEL
# =========================================================

if final_risk <= 30:

    risk_level = "LOW"

    risk_symbol = "🟢"


elif final_risk <= 60:

    risk_level = "SUSPICIOUS"

    risk_symbol = "🟡"


elif final_risk <= 80:

    risk_level = "HIGH"

    risk_symbol = "🟠"


else:

    risk_level = "CRITICAL"

    risk_symbol = "🔴"


# =========================================================
# TOP DASHBOARD CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="cyber-card">

        <div class="card-title">
        ADAPTIVE RISK SCORE
        </div>

        <div class="risk-number">
        {final_risk:.0f}
        </div>

        <div class="risk-label">
        {risk_symbol} {risk_level}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.metric(
        "⚡ Attack Probability",
        f"{xgb_probability * 100:.1f}%"
    )


with col3:

    st.metric(
        "🧠 Model Consensus",
        f"{votes}/{active_models}"
    )


with col4:

    st.metric(
        "📡 Flow Number",
        flow_number
    )


# =========================================================
# MODEL INTELLIGENCE
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# MODEL STATUS
# =========================================================

with col1:

    st.markdown(
        """
        <div class="cyber-card">

        <div class="card-title">
        MODEL INTELLIGENCE
        </div>
        """,
        unsafe_allow_html=True
    )


    # Isolation Forest

    if use_iso:

        if iso_result:

            status = "🚨 ANOMALY"

            css = "status-alert"

        else:

            status = "✓ NORMAL"

            css = "status-online"


        st.markdown(
            f"""
            <div class="model-row">

            <span class="model-name">
            🌲 Isolation Forest
            </span>

            <span class="model-status {css}">
            {status}
            </span>

            </div>
            """,
            unsafe_allow_html=True
        )


    # XGBoost

    if use_xgb:

        if xgb_result:

            status = "🚨 ATTACK"

            css = "status-alert"

        else:

            status = "✓ NORMAL"

            css = "status-online"


        st.markdown(
            f"""
            <div class="model-row">

            <span class="model-name">
            🌳 XGBoost
            </span>

            <span class="model-status {css}">
            {status}
            </span>

            </div>
            """,
            unsafe_allow_html=True
        )


    # LSTM

    if use_lstm and lstm_model is not None:

        if lstm_result:

            status = "🚨 ANOMALY"

            css = "status-alert"

        else:

            status = "✓ NORMAL"

            css = "status-online"


        st.markdown(
            f"""
            <div class="model-row">

            <span class="model-name">
            🧠 LSTM Autoencoder
            </span>

            <span class="model-status {css}">
            {status}
            </span>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# RISK BREAKDOWN
# =========================================================

with col2:

    st.markdown(
        """
        <div class="cyber-card">

        <div class="card-title">
        RISK SIGNAL BREAKDOWN
        </div>
        """,
        unsafe_allow_html=True
    )


    st.write(
        f"🌲 Isolation Forest: **{iso_risk:.1f}**"
    )

    st.progress(
        int(iso_risk)
    )


    st.write(
        f"🌳 XGBoost: **{xgb_risk:.1f}**"
    )

    st.progress(
        int(xgb_risk)
    )


    st.write(
        f"🧠 LSTM: **{lstm_risk:.1f}**"
    )

    st.progress(
        int(lstm_risk)
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


# =========================================================
# THREAT DECISION
# =========================================================

if final_risk >= threshold:

    st.error(
        f"🚨 THREAT DETECTED | "
        f"Risk Score: {final_risk:.1f}"
    )

else:

    st.success(
        f"🛡️ NETWORK MONITORED | "
        f"Risk Score: {final_risk:.1f}"
    )


# =========================================================
# NETWORK FLOW FEATURES
# =========================================================

st.markdown(
    """
    <div class="section-title">
    🔬 FLOW INTELLIGENCE
    </div>
    """,
    unsafe_allow_html=True
)


with st.expander(
    "View Network Flow Features"
):

    feature_table = pd.DataFrame(
        {
            "Feature": sample.columns,

            "Value": sample.iloc[0].values
        }
    )


    st.dataframe(
        feature_table,
        use_container_width=True,
        height=400
    )


# =========================================================
# WHAT-IF SIMULATOR
# =========================================================

st.markdown(
    """
    <div class="section-title">
    🎛️ ADAPTIVE WHAT-IF SIMULATOR
    </div>
    """,
    unsafe_allow_html=True
)


st.caption(
    "Modify a network feature and observe the change "
    "in XGBoost attack probability."
)


selected_feature = st.selectbox(
    "Select Network Feature",
    list(X_data.columns)
)


original_value = float(
    sample[selected_feature].iloc[0]
)


new_value = st.number_input(
    "Change Feature Value",
    value=original_value
)


what_if_sample = sample.copy()


what_if_sample[
    selected_feature
] = new_value


what_if_probability = (

    xgb_model.predict_proba(
        what_if_sample
    )[0][1]

    * 100

)


c1, c2 = st.columns(2)


with c1:

    st.metric(
        "Original Attack Probability",
        f"{xgb_probability * 100:.2f}%"
    )


with c2:

    st.metric(
        "What-If Probability",
        f"{what_if_probability:.2f}%",

        delta=
        f"{what_if_probability - xgb_probability * 100:.2f}%"
    )


# =========================================================
# SECURITY ANALYSIS
# =========================================================

st.markdown(
    """
    <div class="section-title">
    🛰 SECURITY ANALYSIS
    </div>
    """,
    unsafe_allow_html=True
)


if votes >= 2:

    st.warning(
        "⚠️ Multiple AI models agree that "
        "this traffic requires investigation."
    )


elif votes == 1:

    st.info(
        "🔎 One AI model detected suspicious behavior. "
        "Further investigation is recommended."
    )


else:

    st.success(
        "✅ No strong threat signal detected "
        "by the active models."
    )


# =========================================================
# SYSTEM STATUS
# =========================================================

st.markdown("---")


status_col1, status_col2, status_col3 = st.columns(3)


with status_col1:

    st.markdown(
        """
        🟢 **SYSTEM ONLINE**
        """
    )


with status_col2:

    st.markdown(
        f"""
        📡 **FLOWS LOADED: {len(X_data):,}**
        """
    )


with status_col3:

    st.markdown(
        """
        🛡️ **ADAPTIVE MONITORING ACTIVE**
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")


st.markdown(
    """
    <div style="
    text-align:center;
    color:#62a9d1;
    font-family:Orbitron;
    font-size:12px;
    letter-spacing:2px;">

    ADAPTIVE ZERO-DAY NIDS

    <br><br>

    ISOLATION FOREST
    •
    XGBOOST
    •
    LSTM AUTOENCODER

    <br><br>

    MULTI-MODEL NETWORK THREAT INTELLIGENCE

    </div>
    """,
    unsafe_allow_html=True
)