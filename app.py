import streamlit as st
import streamlit.components.v1 as components

# Скриваме всичко излишно, за да се слива с браузъра
st.set_page_config(page_title="Vibe Coding Joke", layout="centered")

st.markdown("""
    <style>
        .block-container { padding: 0; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stAppViewContainer"] { background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# РАБОТЕЩ ЛИНК (Можеш да го замениш с твоя Raw линк от GitHub по-късно)
YOUR_IMAGE_URL = "https://github.com/sgerov24a/Game/blob/main/Screenshot%202026-05-05%20230606.png?raw=true"

funny_app_html = f"""
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 95vh; background-color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">

    <!-- ВЪПРОСЪТ: ПРАВОЪГЪЛНИК СЪС ЗАОБЛЕНИ ЪГЛИ -->
    <div style="
        border: 4px solid black; 
        border-radius: 20px; 
        padding: 25px 50px; 
        background-color: white; 
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 8px 8px 0px rgba(0,0,0,0.05);">
        <h2 style="margin: 0; color: black; font-weight: 900; font-size: 28px;">Ще ми дадеш ли отличен (6) на проекта?</h2>
    </div>

    <!-- БЯЛОТО ПОЛЕ (ЗОНА ЗА ИГРА) -->
    <div id="mainContainer" style="
        width: 95%; 
        max-width: 650px; 
        height: 450px; 
        background-color: white; 
        border: 4px solid black; 
        border-radius: 25px; 
        position: relative; 
        overflow: hidden;">
        
        <button id="yesBtn" style="
            position: absolute; 
            top: 180px; 
            left: 15%; 
            padding: 18px 40px; 
            font-size: 22px; 
            font-weight: bold;
            background-color: #2ecc71; 
            color: white; 
            border: 4px solid black; 
            border-radius: 15px; 
            cursor: pointer;
            z-index: 10;">
            Да
        </button>

        <!-- БУТОН "НЕ": ПЛАВНО ДВИЖЕНИЕ (EASE-OUT) -->
        <button id="noBtn" style="
            position: absolute; 
            top: 180px; 
            right: 15%; 
            padding: 18px 40px; 
            font-size: 22px; 
            font-weight: bold;
            background-color: #e74c3c; 
            color: white; 
            border: 4px solid black; 
            border-radius: 15px; 
            z-index: 10;
            transition: all 0.4s ease-out; /* ПЛЪЗГАНЕ КАТО НА ГРАФИКАТА ТИ */
            touch-action: none;">
            Не
        </button>
    </div>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const container = document.getElementById('mainContainer');
    const yesBtn = document.getElementById('yesBtn');

    function glide() {{
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;
        const btnWidth = noBtn.clientWidth;
        const btnHeight = noBtn.clientHeight;

        const newX = Math.random() * (containerWidth - btnWidth);
        const newY = Math.random() * (containerHeight - btnHeight);

        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.right = 'auto';
    }}

    noBtn.addEventListener('mouseover', glide);
    noBtn.addEventListener('touchstart', (e) => {{ e.preventDefault(); glide(); }});

    yesBtn.addEventListener('click', () => {{
        document.body.innerHTML = `
            <div style="
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                justify-content: center; 
                height: 100vh; 
                background-color: #2ecc71; 
                color: white;
                text-align: center;
                font-family: sans-serif;">
                
                <h1 style="font-size: 60px; text-shadow: 4px 4px 0px black; margin-bottom: 10px;">БРАВО!</h1>
                <h2 style="background: white; color: black; padding: 15px 30px; border: 5px solid black; border-radius: 20px; font-weight: 800;">
                    ЗНАЕХ, ЧЕ ЩЕ СЕ СЪГЛАСИШ!
                </h2>
                
                <img src="{https://github.com/sgerov24a/Game/blob/main/Screenshot%202026-05-05%20230606.png?raw=true}" style="
                    margin-top: 25px;
                    width: 350px; 
                    height: auto;
                    border-radius: 30px; 
                    border: 6px solid black;
                    box-shadow: 15px 15px 0px rgba(0,0,0,0.2);">
            </div>
        `;
    }});
</script>
"""

components.html(funny_app_html, height=850)
