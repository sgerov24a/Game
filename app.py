import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vibe Coding Masterpiece", layout="centered")

st.markdown("""
    <style>
        .block-container { padding: 0; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stAppViewContainer"] { background-color: white; }
    </style>
    """, unsafe_allow_html=True)

YOUR_IMAGE_URL = "https://github.com/sgerov24a/Game/blob/main/Screenshot%202026-05-05%20230606.png?raw=true"

funny_app_html = f"""
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 95vh; background-color: white; font-family: 'Segoe UI', sans-serif;">

    <div style="border: 8px solid black; border-radius: 20px; padding: 25px 50px; background-color: white; margin-bottom: 25px; text-align: center; box-shadow: 8px 8px 0px rgba(0,0,0,0.25);">
        <h2 style="margin: 0; color: black; font-weight: 500; font-size: 28px;">Ще ми дадеш ли отличен (6) на проекта?</h2>
    </div>

    <div id="mainContainer" style="width: 95%; max-width: 650px; height: 450px; background-color: white; border: 8px solid black; border-radius: 25px; position: relative; overflow: hidden;">
        <button id="yesBtn" style="position: absolute; top: 180px; left: 15%; padding: 18px 40px; font-size: 22px; font-weight: bold; background-color: #2ecc71; color: white; border: 4px solid black; border-radius: 15px; cursor: pointer; z-index: 10;">
            Да
        </button>

        <button id="noBtn" style="position: absolute; top: 180px; right: 15%; padding: 18px 40px; font-size: 22px; font-weight: bold; background-color: #e74c3c; color: white; border: 4px solid black; border-radius: 15px; z-index: 10; transition: all 0.3s ease-out; touch-action: none; cursor: default;">
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

        // Вземаме текущата позиция
        const rect = noBtn.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        const currX = rect.left - containerRect.left;
        const currY = rect.top - containerRect.top;

        let newX, newY;
        
        // Генерираме нова позиция, докато не е на поне 150px от старата
        do {{
            newX = Math.random() * (containerWidth - btnWidth);
            newY = Math.random() * (containerHeight - btnHeight);
        }} while (Math.hypot(newX - currX, newY - currY) < 150);

        noBtn.style.left = newX + 'px';
        noBtn.style.top = newY + 'px';
        noBtn.style.right = 'auto';
    }}

    // КЛЮЧОВАТА ПРОМЯНА: mousemove вместо mouseover
    noBtn.addEventListener('mousemove', glide);
    noBtn.addEventListener('touchstart', (e) => {{ e.preventDefault(); glide(); }}, {{passive: false}});
    
    // Допълнителна защита: ако все пак успеят да кликнат (хардуерен бъг), бутонът пак бяга
    noBtn.addEventListener('click', (e) => {{ e.preventDefault(); glide(); }});

    yesBtn.addEventListener('click', () => {{
        document.body.innerHTML = `
            <div style="display: flex; align-items: center; justify-content: center; height: 100vh; background-color: white; font-family: sans-serif; padding: 20px;">
                <div style="background-color: #2ecc71; border: 6px solid black; border-radius: 40px; padding: 40px; display: flex; flex-direction: column; align-items: center; box-shadow: 15px 15px 0px rgba(0,0,0,0.1); max-width: 500px; width: 90%;">
                    <h1 style="font-size: 55px; color: white; text-shadow: 4px 4px 0px black; margin: 0;">БРАВО!</h1>
                    <h2 style="background: white; color: black; padding: 15px 30px; border: 4px solid black; border-radius: 20px; margin: 25px 0; font-weight: 800; font-size: 22px;">
                        ЗНАЕХ, ЧЕ ЩЕ СЕ СЪГЛАСИШ!
                    </h2>
                    <img src="{YOUR_IMAGE_URL}" style="width: 100%; max-width: 320px; height: auto; border-radius: 25px; border: 5px solid black; background-color: white; object-fit: contain;">
                </div>
            </div>
        `;
    }});
</script>
"""

components.html(funny_app_html, height=850)
