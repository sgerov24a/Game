import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Важен въпрос", layout="centered")

st.markdown("<h1 style='text-align: center;'>Въпрос към теб:</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Ще ми дадеш ли отличен (6) на проекта?</h2>", unsafe_allow_html=True)

# Обновен HTML с поддръжка за тъчскрийн
funny_button_html = """
<div id="container" style="height: 450px; position: relative; border: 2px dashed #ccc; border-radius: 20px; background-color: #ffffff; overflow: hidden;">
    
    <button id="yesBtn" style="
        position: absolute; 
        top: 40%; 
        left: 15%; 
        padding: 15px 40px; 
        font-size: 22px; 
        background-color: #2ecc71; 
        color: white; 
        border: none; 
        border-radius: 50px; 
        cursor: pointer;
        z-index: 10;">
        Да
    </button>

    <button id="noBtn" style="
        position: absolute; 
        top: 40%; 
        right: 15%; 
        padding: 15px 40px; 
        font-size: 22px; 
        background-color: #e74c3c; 
        color: white; 
        border: none; 
        border-radius: 50px; 
        transition: 0.1s;
        z-index: 10;
        touch-action: none;"> <!-- touch-action: none пречи на телефона да скролва вместо да мести бутона -->
        Не
    </button>
</div>

<script>
    const noBtn = document.getElementById('noBtn');
    const container = document.getElementById('container');
    const yesBtn = document.getElementById('yesBtn');

    function moveButton() {
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
    }

    // За компютър - бяга при доближаване с мишката
    noBtn.addEventListener('mouseover', moveButton);

    // За телефон - бяга веднага щом пръстът го докосне
    noBtn.addEventListener('touchstart', (e) => {
        e.preventDefault(); // Спира кликването
        moveButton();
    });

    // Резултат при "Да"
    yesBtn.addEventListener('click', () => {
        document.body.innerHTML = `
            <div style="text-align: center; padding-top: 50px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                <h1 style="color: #2ecc71; font-size: 40px;">🎉 БЛАГОДАРЯ! 🎉</h1>
                <p style="font-size: 20px;">Знаех си, че ще се съгласиш!</p>
                <div style="font-size: 100px;">🏆</div>
            </div>
        `;
    });
</script>
"""

components.html(funny_button_html, height=500)
