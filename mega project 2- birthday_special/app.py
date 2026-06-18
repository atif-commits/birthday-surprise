import streamlit as st
import streamlit.components.v1 as components
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
FRIEND_NAME  = "Subhan"
CORRECT_PASS = "2106"
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
    animation: fade-in-up 0.7s ease-out both;
}
.gold-rule {
    height: 1px;
    background: linear-gradient(90deg, transparent, #C9A96E, transparent);
    border: none;
    margin: 2.5rem auto;
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
    transition: border-color 0.2s !important;
}
div[data-baseweb="input"]:focus-within {
    border-color: #C9A96E !important;
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
    transition: opacity 0.2s, transform 0.2s !important;
    margin-top: 0.8rem !important;
}
.stButton > button:hover  { opacity: 0.85 !important; transform: translateY(-1px) !important; }
.stButton > button:active { transform: translateY(0) !important; }
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
    font-weight: 700;
    color: #2C2416;
    text-align: center;
    margin-bottom: 0.2rem;
}
.bday-sub {
    color: #7A6A55;
    text-align: center;
    font-size: 0.92rem;
    letter-spacing: 0.08em;
    margin-bottom: 1.8rem;
}
.signoff {
    text-align: center;
    color: #A8997F;
    font-size: 0.82rem;
    letter-spacing: 0.05em;
}

@keyframes fade-in-up {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "unlocked"      not in st.session_state: st.session_state.unlocked      = False
if "letter_opened" not in st.session_state: st.session_state.letter_opened = False
if "typed"         not in st.session_state: st.session_state.typed         = False

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

    with st.form("unlock_form", clear_on_submit=False):
        password = st.text_input(
            label="password",
            type="password",
            placeholder="enter the password...",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Open Your Gift →")

    if submitted:
        if password == "":
            st.warning("Enter a password first.")
        elif password == CORRECT_PASS:
            countdown_html = """
            <div id="cd-root" style="position:fixed; inset:0; z-index:999999;
                 display:flex; align-items:center; justify-content:center;
                 background:#FAF7F2; font-family:'Playfair Display', serif;
                 font-weight:700; color:#C9A96E; font-size:min(45vw, 22rem);
                 line-height:1;">3</div>
            <script>
                (function () {
                    var doc = window.parent.document;
                    var old = doc.getElementById('cd-overlay-host');
                    if (old) old.remove();

                    var host = doc.createElement('div');
                    host.id = 'cd-overlay-host';
                    host.appendChild(document.getElementById('cd-root').cloneNode(true));
                    doc.body.appendChild(host);

                    var el = doc.getElementById('cd-root');
                    var n = 3;
                    var iv = setInterval(function () {
                        n -= 1;
                        if (n > 0) {
                            el.textContent = n;
                        } else {
                            clearInterval(iv);
                            host.remove();
                        }
                    }, 450);
                })();
            </script>
            """
            components.html(countdown_html, height=0)
            # 3 ticks * 0.45s = 1.35s total — matches the JS interval above
            # exactly, so the page swap lands right as "1" disappears.
            # Shortened from the original 0.7s/tick (2.4s total) since that
            # felt sluggish; this is the only sleep in the whole app and it
            # exists purely to keep this rerun from firing mid-animation.
            time.sleep(1.35)
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("That's not it. Try again. 🔐")

    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# UNLOCKED PAGE
# ══════════════════════════════════════════════════════════════════════════════
else:
    # ── music: always re-render the tag, but make playback idempotent ──
    # Why the earlier "inject once" fix broke playback: gating the whole
    # st.markdown call behind `music_started` stops it from running again
    # on later reruns (e.g. the "Open the Secret Letter" click) — which
    # also means the <audio> element's HTML is simply never written into
    # the new page at all, since Streamlit rebuilds the DOM from scratch
    # on every rerun by replaying whichever st.markdown/components calls
    # actually execute. Skipped call -> no element in the new DOM -> sound
    # cuts out, which is exactly what happened.
    #
    # The correct fix: keep emitting the tag every single rerun (so it's
    # always present), but move the "only once" logic into the JS itself.
    # The script checks the *parent* document (where components.html
    # content gets cloned to) for an existing #bday-audio element before
    # doing anything. If one's already there and already playing, it does
    # nothing — no second element, no restart, no interruption. If one
    # isn't there yet (first render), it creates it and calls .play() once.
    BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(BASE_DIR, "birthday.mp3")

    if os.path.exists(audio_path):
        with open(audio_path, "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode()
        components.html(
            f"""
            <script>
                (function () {{
                    var doc = window.parent.document;
                    var existing = doc.getElementById('bday-audio');
                    if (existing) {{
                        // Already created on an earlier rerun and still
                        // looping — leave it completely alone.
                        return;
                    }}
                    var audio = doc.createElement('audio');
                    audio.id = 'bday-audio';
                    audio.loop = true;
                    audio.style.display = 'none';
                    audio.src = 'data:audio/mp3;base64,{audio_base64}';
                    doc.body.appendChild(audio);
                    audio.play().catch(function () {{ /* autoplay blocked, ignore */ }});
                }})();
            </script>
            """,
            height=0,
        )

    st.balloons()

    # ── headline: real character-by-character typewriter (plays once) ──
    title_text = f"Happy Birthday, {FRIEND_NAME}! 🎂"

    if not st.session_state.typed:
        typewriter_html = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
            html, body {{ margin:0; padding:0; background:transparent; overflow:hidden; }}
            #tw-line {{
                font-family:'Playfair Display', serif;
                font-weight:700;
                font-size: clamp(1.8rem, 6.5vw, 2.6rem);
                color:#2C2416;
                text-align:center;
                white-space:nowrap;
            }}
            #tw-cursor {{
                display:inline-block;
                border-right: 0.08em solid #C9A96E;
                margin-left: 1px;
                animation: blink 0.75s step-end infinite;
            }}
            @keyframes blink {{
                from, to {{ border-color: transparent; }}
                50%      {{ border-color: #C9A96E; }}
            }}
        </style>
        <div id="tw-line"><span id="tw-text"></span><span id="tw-cursor">&nbsp;</span></div>
        <script>
            var text = {title_text!r};
            var i = 0;
            var el = document.getElementById('tw-text');
            (function typeNext() {{
                if (i < text.length) {{
                    el.textContent += text.charAt(i);
                    i += 1;
                    setTimeout(typeNext, 65);
                }} else {{
                    var cur = document.getElementById('tw-cursor');
                    if (cur) cur.style.display = 'none';
                }}
            }})();
        </script>
        """
        components.html(typewriter_html, height=70)
        st.session_state.typed = True
    else:
        st.markdown(f'<p class="bday-headline">{title_text}</p>', unsafe_allow_html=True)

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
            '<p class="signoff">coded by atif with lots of love 🤍</p>',
            unsafe_allow_html=True,
        )
