import streamlit as st
import streamlit.components.v1 as components

# Настройка за пълно сливане с браузъра
st.set_page_config(page_title="Изненада!", layout="centered")

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
YOUR_IMAGE_URL = "https://images.unsplash.com/photo-1531256456869-ce942a665e80?q=80&w=500&auto=format&fit=crop"

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
                
                <img src="{YOUR_IMAGE_URL}" style="
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
