import streamlit as st
import streamlit.components.v1 as components

# Настройка за пълно сливане с браузъра
st.set_page_config(page_title="Vibe Coding Joke", layout="centered")

# CSS за премахване на всички граници от Streamlit
st.markdown("""
    <style>
        .block-container { padding: 0; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body { background-color: white; }
    </style>
    """, unsafe_allow_html=True)

# ТВОЯТА СНИМКА (замени линка вътре в кавичките)
YOUR_IMAGE_URL = "data:image/jpeg;base64,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"

funny_app_html = f"""
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 90vh; background-color: white; font-family: sans-serif;">

    <!-- ВЪПРОСЪТ: ЗАОБЛЕН ПРАВОЪГЪЛНИК -->
    <div style="
        border: 4px solid black; 
        border-radius: 15px; 
        padding: 20px 40px; 
        background-color: white; 
        margin-bottom: 20px;
        text-align: center;">
        <h2 style="margin: 0; color: black; font-weight: bold;">Ще ми дадеш ли отличен (6) на проекта?</h2>
    </div>

    <!-- БЯЛОТО ПОЛЕ (ЗОНА ЗА ИГРА) -->
    <div id="mainContainer" style="
        width: 90%; 
        max-width: 600px; 
        height: 400px; 
        background-color: white; 
        border: 4px solid black; 
        border-radius: 20px; 
        position: relative; 
        overflow: hidden;">
        
        <button id="yesBtn" style="
            position: absolute; 
            top: 150px; 
            left: 15%; 
            padding: 15px 35px; 
            font-size: 20px; 
            font-weight: bold;
            background-color: #2ecc71; 
            color: white; 
            border: 3px solid black; 
            border-radius: 12px; 
            cursor: pointer;
            z-index: 10;">
            Да
        </button>

        <!-- БУТОН "НЕ" С ПЛАВНО ДВИЖЕНИЕ (TRANSITION) -->
        <button id="noBtn" style="
            position: absolute; 
            top: 150px; 
            right: 15%; 
            padding: 15px 35px; 
            font-size: 20px; 
            font-weight: bold;
            background-color: #e74c3c; 
            color: white; 
            border: 3px solid black; 
            border-radius: 12px; 
            z-index: 10;
            cursor: pointer;
            transition: all 0.4s ease-out; /* ТОВА ПРАВИ ПЛЪЗГАНЕТО ПО ТВОЯТА ГРАФИКА */
            touch-action: none;">
            Не
        </button>
    </div>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const container = document.getElementById('mainContainer');
    const yesBtn = document.getElementById('yesBtn');

    function glideButton() {{
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;
        const btnWidth = noBtn.clientWidth;
        const btnHeight = noBtn.clientHeight;

        // Генерираме нови координати
        const newX = Math.random() * (containerWidth - btnWidth);
        const newY = Math.random() * (containerHeight - btnHeight);

        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.right = 'auto';
    }}

    // Задействане при доближаване (mouseover)
    noBtn.addEventListener('mouseover', glideButton);
    
    // Задействане при докосване на телефон
    noBtn.addEventListener('touchstart', (e) => {{
        e.preventDefault();
        glideButton();
    }});

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
                font-family: sans-serif;">
                
                <h1 style="font-size: 50px; text-shadow: 3px 3px 0px black;">БРАВО!</h1>
                <h2 style="background: white; color: black; padding: 10px 20px; border: 4px solid black; border-radius: 10px; margin: 20px 0;">
                    ЗНАЕХ, ЧЕ ЩЕ СЕ СЪГЛАСИШ!
                </h2>
                
                <img src="{data:image/jpeg;base64,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}" style="
                    width: 300px; 
                    border-radius: 25px; 
                    border: 4px solid black;
                    box-shadow: 10px 10px 0px rgba(0,0,0,0.2);">
            </div>
        `;
    }});
</script>
"""

components.html(funny_app_html, height=800)
