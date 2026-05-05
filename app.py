import streamlit as st
import streamlit.components.v1 as components

# Настройка на страницата
st.set_page_config(page_title="Vibe Coding Joke", layout="centered")

# HTML код с вграден CSS и JavaScript
funny_app_html = """
<div style="font-family: 'Comic Sans MS', cursive, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; background-color: #f0f0f0;">

    <!-- ВЪПРОСЪТ В ЕЛИПСА -->
    <div style="
        border: 4px solid black; 
        border-radius: 50% / 50%; 
        padding: 20px 50px; 
        background-color: white; 
        margin-bottom: 30px;
        box-shadow: 5px 5px 0px rgba(0,0,0,0.1);
        text-align: center;
        min-width: 300px;">
        <h1 style="margin: 0; font-size: 24px; color: black;">Ще ми дадеш ли отличен (6) на проекта?</h1>
    </div>

    <!-- БЯЛОТО ПОЛЕ С ЧЕРНА РАМКА -->
    <div id="mainContainer" style="
        width: 100%; 
        max-width: 600px; 
        height: 400px; 
        background-color: white; 
        border: 4px solid black; 
        border-radius: 25px; 
        position: relative; 
        overflow: hidden;">
        
        <!-- БУТОН ДА -->
        <button id="yesBtn" style="
            position: absolute; 
            top: 150px; 
            left: 10%; 
            width: 120px;
            padding: 15px 0; 
            font-size: 20px; 
            font-weight: bold;
            background-color: #2ecc71; 
            color: black; 
            border: 3px solid black; 
            border-radius: 20px; 
            cursor: pointer;
            z-index: 10;">
            Да
        </button>

        <!-- БУТОН НЕ (БЯГАЩИЯТ) -->
        <button id="noBtn" style="
            position: absolute; 
            top: 150px; 
            right: 10%; 
            width: 120px;
            padding: 15px 0; 
            font-size: 20px; 
            font-weight: bold;
            background-color: #e74c3c; 
            color: black; 
            border: 3px solid black; 
            border-radius: 20px; 
            transition: 0.05s;
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

    // Функция за внезапно "изплъзване"
    function teleportButton() {
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;
        const btnWidth = noBtn.clientWidth;
        const btnHeight = noBtn.clientHeight;

        // Генериране на координати, така че бутонът винаги да остава вътре в бялото поле
        const newX = Math.random() * (containerWidth - btnWidth);
        const newY = Math.random() * (containerHeight - btnHeight);

        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.right = 'auto'; // Премахваме първоначалното дясно позициониране
    }

    // За компютър: Бяга при доближаване с мишката
    noBtn.addEventListener('mouseover', teleportButton);

    // За телефон: Бяга при допир
    noBtn.addEventListener('touchstart', (e) => {
        e.preventDefault();
        teleportButton();
    });

    // Действие при натискане на "ДА"
    yesBtn.addEventListener('click', () => {
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
                text-align: center;">
                <h1 style="font-size: 60px; text-shadow: 4px 4px 0px black; margin-bottom: 20px;">БРАВО!</h1>
                <h2 style="font-size: 30px; color: black; background: white; padding: 10px 20px; border: 4px solid black; border-radius: 15px;">
                    ЗНАЕХ, ЧЕ ЩЕ СЕ СЪГЛАСИШ!
                </h2>
                <div style="font-size: 100px; margin-top: 20px;">🎖️</div>
            </div>
        `;
    });
</script>
"""

# Рендиране на приложението
components.html(funny_app_html, height=800)
