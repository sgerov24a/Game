import streamlit as st
import streamlit.components.v1 as components

# Настройка за по-изчистен вид
st.set_page_config(page_title="Vibe Coding Project", layout="centered")

# Скриваме стандартните полета на Streamlit (padding), за да се слива по-добре
st.markdown("""
    <style>
        .block-container { padding-top: 2rem; padding-bottom: 0rem; }
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ТВОЯТА СНИМКА: Постави линка към твоята снимка тук
# Може да е линк от интернет или файл, качен в GitHub (ползвай "Raw" линка)
YOUR_IMAGE_URL = "https://images.unsplash.com/photo-1531256456869-ce942a665e80?q=80&w=500&auto=format&fit=crop"

funny_app_html = f"""
<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: transparent;">

    <!-- ВЪПРОСЪТ: ПРАВОЪГЪЛНИК СЪС ЗАОБЛЕНИ ЪГЛИ -->
    <div style="
        border: 4px solid black; 
        border-radius: 20px; 
        padding: 25px 40px; 
        background-color: white; 
        margin-bottom: 30px;
        text-align: center;
        width: 80%;
        max-width: 500px;">
        <h1 style="margin: 0; font-size: 26px; color: black; font-weight: 800;">Ще ми дадеш ли отличен (6) на проекта?</h1>
    </div>

    <!-- БЯЛОТО ПОЛЕ (ЗОНА ЗА ИГРА) -->
    <div id="mainContainer" style="
        width: 95%; 
        max-width: 650px; 
        height: 450px; 
        background-color: white; 
        border: 4px solid black; 
        border-radius: 30px; 
        position: relative; 
        overflow: hidden;
        box-shadow: 10px 10px 0px rgba(0,0,0,0.05);">
        
        <button id="yesBtn" style="
            position: absolute; 
            top: 180px; 
            left: 15%; 
            width: 130px;
            padding: 15px 0; 
            font-size: 22px; 
            font-weight: bold;
            background-color: #2ecc71; 
            color: white; 
            border: 4px solid black; 
            border-radius: 15px; 
            cursor: pointer;
            z-index: 10;
            transition: transform 0.1s;">
            Да
        </button>

        <button id="noBtn" style="
            position: absolute; 
            top: 180px; 
            right: 15%; 
            width: 130px;
            padding: 15px 0; 
            font-size: 22px; 
            font-weight: bold;
            background-color: #e74c3c; 
            color: white; 
            border: 4px solid black; 
            border-radius: 15px; 
            z-index: 10;
            touch-action: none;">
            Не
        </button>
    </div>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const container = document.getElementById('mainContainer');
    const yesBtn = document.getElementById('yesBtn');

    function teleport() {{
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

    noBtn.addEventListener('mouseover', teleport);
    noBtn.addEventListener('touchstart', (e) => {{ e.preventDefault(); teleport(); }});

    yesBtn.addEventListener('click', () => {{
        document.body.innerHTML = `
            <div style="
                display: flex; 
                flex-direction: column; 
                align-items: center; 
                justify-content: center; 
                height: 100vh; 
                background-color: #2ecc71; 
                font-family: sans-serif;
                color: white;
                text-align: center;
                padding: 20px;">
                
                <h1 style="font-size: 50px; text-shadow: 4px 4px 0px black; margin: 0;">БРАВО!</h1>
                <h2 style="font-size: 24px; color: black; background: white; padding: 15px 30px; border: 4px solid black; border-radius: 15px; margin: 20px 0;">
                    ЗНАЕХ, ЧЕ ЩЕ СЕ СЪГЛАСИШ!
                </h2>
                
                <!-- ТВОЯТА СНИМКА СЪС ЗАОБЛЕНИ ЪГЛИ -->
                <img src="{YOUR_IMAGE_URL}" style="
                    width: 300px; 
                    height: auto; 
                    border-radius: 30px; 
                    border: 5px solid black; 
                    box-shadow: 10px 10px 0px rgba(0,0,0,0.2);">
            </div>
        `;
    }});
</script>
"""

# Рендиране
components.html(funny_app_html, height=850)
