import streamlit as st
import base64
import os
import time

# ── MUST BE FIRST ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="A Gift For You 🎁",
    page_icon="🎁",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CONFIG ─────────────────────────────────────────────────────────────────────
FRIEND_NAME  = "motu bhai"
CORRECT_PASS = "2307"
SECRET_LETTER = """
You've been one of the most genuine people I've ever met.
The kind of person who shows up, who listens, who makes everything
feel a little lighter just by being there.

This year I hope you get everything you deserve —
which is honestly quite a lot.

Happy Birthday.
"""

# ── GLOBAL STYLES ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #FAF7F2; min-height: 100vh; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 3rem; padding-bottom: 4rem; max-width: 680px; }

.display-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 6vw, 3.2rem);
    font-weight: 700;
    color: #2C2416;
    text-align: center;
    line-height: 1.15;
    margin-bottom: 0.25rem;
    letter-spacing: -0.02em;
}
.display-sub {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #7A6A55;
    text-align: center;
    margin-bottom: 2.5rem;
    letter-spacing: 0.02em;
}
.card {
    background: #F2EDE4;
    border: 1px solid #E0D5C5;
    border-radius: 20px;
    padding: 2.2rem 2.4rem;
    margin-bottom: 1.5rem;
}
.gold-rule {
    height: 1px;
    background: linear-gradient(90deg, transparent, #C9A96E, transparent);
    border: none;
    margin: 2rem auto;
    width: 90%;
}
.pass-label {
    color: #7A6A55;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
div[data-baseweb="input"] {
    border-radius: 12px !important;
    border: 1px solid #E0D5C5 !important;
    background: #FAF7F2 !important;
}
div[data-baseweb="input"] input {
    color: #7A6A55 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    letter-spacing: 0.08em !important;
}
.stButton > button {
    background: #C9A96E !important;
    color: #FAF7F2 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.06em !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.6rem 2rem !important;
    width: 100% !important;
    transition: opacity 0.2s !important;
    margin-top: 0.8rem !important;
}
.stButton > button:hover { opacity: 0.82 !important; }
div[data-testid="stAlert"] {
    border-radius: 12px !important;
    border: none !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
}
.letter-body {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.08rem;
    color: #2C2416;
    line-height: 1.85;
    white-space: pre-line;
    text-align: center;
}
.bday-headline {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 5vw, 2.6rem);
    color: #2C2416;
    text-align: center;
    font-weight: 700;
    margin-bottom: 0.2rem;
}
.bday-sub {
    color: #7A6A55;
    text-align: center;
    font-size: 0.92rem;
    letter-spacing: 0.08em;
    margin-bottom: 1.8rem;
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "unlocked"      not in st.session_state: st.session_state.unlocked      = False
if "show_letter"   not in st.session_state: st.session_state.show_letter   = False
if "letter_opened" not in st.session_state: st.session_state.letter_opened = False

# ══════════════════════════════════════════════════════════════════════════════
# LOCKED PAGE
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.unlocked:

    st.markdown('<p class="display-title">A gift, just for you 🎁</p>', unsafe_allow_html=True)
    st.markdown('<p class="display-sub">Something personal is waiting inside</p>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(
        '<p style="font-family:\'Playfair Display\',serif; font-style:italic; color:#1A120B;'
        'font-size:1rem; text-align:center; margin-bottom:1.5rem; line-height:1.7;">'
        'For someone who deserves a special day.<br>✦</p>',
        unsafe_allow_html=True,
    )

    st.markdown('<p class="pass-label">🔒 Secret Password</p>', unsafe_allow_html=True)

    password = st.text_input(
        label="password",
        type="password",
        placeholder="enter the password...",
        label_visibility="collapsed",
    )

    if st.button("Open Your Gift →"):
        if password == CORRECT_PASS:
            countdown = st.empty()
            for i in range(3, 0, -1):
                countdown.markdown(
                    f"<h1 style='text-align:center; color:#C9A96E;'>{i}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(1)
            countdown.empty()
            st.session_state.unlocked = True
            st.rerun()
        elif password == "":
            st.warning("Enter a password first.")
        else:
            st.error("That's not it. Try again. 🔐")

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# UNLOCKED PAGE
# ══════════════════════════════════════════════════════════════════════════════
else:
    st.balloons()

    # ── music ──
    BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(BASE_DIR, "birthday.mp3")

    if os.path.exists(audio_path):
        with open(audio_path, "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <audio autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True,
        )

    # ── typewriter headline ──
    title_placeholder = st.empty()
    title_text = f"Happy Birthday, {FRIEND_NAME}! 🎂"
    for i in range(len(title_text) + 1):
        title_placeholder.markdown(
            f'<p class="bday-headline">{title_text[:i]}</p>',
            unsafe_allow_html=True
        )
        time.sleep(0.05)

    st.markdown('<p class="bday-sub">A little something made just for you</p>', unsafe_allow_html=True)
    st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

    # ── birthday message card ──
    st.markdown("""
    <div class="card">
        <p style="color:#7A6A55; font-size:0.75rem; letter-spacing:0.12em;
                  text-transform:uppercase; margin-bottom:0.8rem;">
            A message from me
        </p>
        <p style="color:#2C2416; font-size:1.05rem; line-height:1.8;
                  font-family:'Playfair Display',serif; font-style:italic;">
            Wishing you a day as bright as you are.<br>
            May this year bring you everything you've been
            quietly hoping for — and a few things you
            didn't even know you needed.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── secret letter button ──
    if not st.session_state.letter_opened:
        if st.button("💌 Open the Secret Letter"):
            st.session_state.show_letter   = True
            st.session_state.letter_opened = True
            st.rerun()

    else:
        st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)

        st.markdown(
            '<p style="color:#7A6A55; font-size:0.75rem; letter-spacing:0.12em;'
            'text-transform:uppercase; text-align:center; margin-bottom:1rem;">'
            '💌 Just between us</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p class="letter-body">{SECRET_LETTER.strip()}</p>',
            unsafe_allow_html=True,
        )

        st.markdown('<hr class="gold-rule">', unsafe_allow_html=True)
        st.markdown(
            '<p style="text-align:center; color:#7A6A55; font-size:0.9rem;">coded by atif with lots of love 🤍</p>',
            unsafe_allow_html=True,
        )
