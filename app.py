import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vibe Coding Masterpiece", layout="centered")

st.markdown("""
    <style>
        .block-container { padding: 0; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stAppViewContainer"] { background-color: #ffc2d4; }
    </style>
    """, unsafe_allow_html=True)

# Твоят линк към снимката
YOUR_IMAGE_URL = "https://github.com/sgerov24a/Game/blob/main/Screenshot%202026-05-05%20230606.png?raw=true"

funny_app_html = f"""
<div style="display: flex; align-items: center; justify-content: center; height: 95vh; background-color: #F8BDCE; font-family: 'Segoe UI', sans-serif;">

    <!-- ОБЩИЯТ КОНТЕЙНЕР С ГРАНИЦА (Като на Браво екрана) -->
    <div style="
        border: 10px solid black; 
        border-radius: 40px; 
        padding: 40px; 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        box-shadow: 8px 8px 0px rgba(0,0,0,0.25); 
        max-width: 750px; 
        width: 95%; 
        background-color: #EB6A90;">

        <!-- ВЪПРОСЪТ -->
        <div style="border: 8px solid black; border-radius: 20px; padding: 25px 50px; background-color: #FFC2D4; margin-bottom: 25px; text-align: center; box-shadow: 8px 8px 0px rgba(0,0,0,0.25);">
            <h2 style="margin: 0; font-family: 'Comic Sans MS', cursive; color: black; font-weight: 400; font-size: 28px;">Ще ми дадеш ли отличен (6) на проекта?</h2>
        </div>

        <!-- БЯЛОТО ПОЛЕ (ЗОНА ЗА ИГРА) -->
        <div id="mainContainer" style="width: 100%; max-width: 650px; height: 450px; background-color: white; border: 8px solid black; border-radius: 25px; position: relative; overflow: hidden; box-shadow: 8px 8px 0px rgba(0,0,0,0.25)">
            <button id="yesBtn" style="position: absolute; top: 180px; left: 15%; padding: 18px 40px; font-size: 22px; font-weight: bold; background-color: #2ecc71; color: white; border: 6px solid black; border-radius: 15px; cursor: pointer; z-index: 10; box-shadow: 8px 8px 0px rgba(0,0,0,0.5)">
                Да
            </button>

            <button id="noBtn" style="position: absolute; top: 180px; right: 15%; padding: 18px 40px; font-size: 22px; font-weight: bold; background-color: #e74c3c; color: white; border: 6px solid black; border-radius: 15px; z-index: 10; transition: all 0.3s ease-out; touch-action: none; cursor: default;box-shadow: 8px 8px 0px rgba(0,0,0,0.5)">
                Не
            </button>
        </div>
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

        const rect = noBtn.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        const currX = rect.left - containerRect.left;
        const currY = rect.top - containerRect.top;

        let newX, newY;
        
        do {{
            newX = Math.random() * (containerWidth - btnWidth);
            newY = Math.random() * (containerHeight - btnHeight);
        }} while (Math.hypot(newX - currX, newY - currY) < 150);

        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.right = 'auto';
    }}

    noBtn.addEventListener('mousemove', glide);
    noBtn.addEventListener('touchstart', (e) => {{ e.preventDefault(); glide(); }}, {{passive: false}});
    noBtn.addEventListener('click', (e) => {{ e.preventDefault(); glide(); }});

    yesBtn.addEventListener('click', () => {{
        document.body.innerHTML = `
            <div style="display: flex; align-items: center; justify-content: center; height: 100vh; background-color: #ffc2d4; font-family: sans-serif; padding: 20px;">
                <div style="background-color: #EB6A90; border: 6px solid black; border-radius: 40px; padding: 40px; display: flex; flex-direction: column; align-items: center; box-shadow: 15px 15px 0px rgba(0,0,0,0.25); max-width: 500px; width: 90%;">
                    <h1 style="font-size: 55px; color: white; text-shadow: 4px 4px 0px black; margin: 0;">БРАВО!</h1>
                    <h2 style="background: #ffc2d4; color: black; padding: 15px 30px; border: 4px solid black; border-radius: 20px; margin: 25px 0; font-weight: 800; font-size: 22px;box-shadow: 8px 8px 0px rgba(0,0,0,0.25)">
                        ЗНАЕХ, ЧЕ ЩЕ СЕ СЪГЛАСИШ!
                    </h2>
                    <img src="{YOUR_IMAGE_URL}" style="width: 100%; max-width: 320px; height: auto; border-radius: 25px; border: 5px solid black; background-color: #ffc2d4; object-fit: contain;">
                </div>
            </div>
        `;
    }});
</script>
"""

components.html(funny_app_html, height=850)
