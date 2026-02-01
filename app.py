import streamlit as st
from base import centered_texts, centered_gif, balloon_reset, empty_line, centered_button, placeholder_gif, placeholder_texts, snow_reset
import time

st.set_page_config(page_title="Just A Normal Webpage",
       page_icon="🚀",
       layout="centered")

# placeHolder = st.empty()

balloon_reset()
time.sleep(1)
# snow_reset()

centered_texts("Welcomesss...", 1, "red")
empty_line()

col1, col2 = st.columns([1, 1])
with col1:
    centered_gif("https://media.tenor.com/7UHqqhLP8tgAAAAi/stk.gif", 300)

with col2:
    st.write()
    st.write()
    st.write()
    placeholder1 = st.empty()

    sentence = "Hellos, I am My little Kito meow meow. I am here to assist you. This weird creator is very lazy to assist the viewers so he has hired me to do it for him. It's not like I am free it's just that his intentions and the website he made is just so cool so I aggreed to play along with him. Although I have demanded him cat food and treats worth a year HEHEHE... feel free to curse him if you didn't like his work."
    text = ""

    for char in sentence:
        text += char
        placeholder1.markdown(f"### {text}")
        time.sleep(0.10)



empty_line()
empty_line()
centered_texts("So you must be wondering what in the world is this?", 3, "")
centered_texts("🤔 🤔 🤔", 1, "")
centered_texts("Click Below and Find Out! ", 3, "")
centered_texts("👇", 1,"")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
    
placeHolder2 = st.empty()

# Show button only if it hasn't been clicked
if not st.session_state.button_clicked:
    centered_button("Click Me !!!")
    # time.sleep(2)
    
else:
    placeholder_gif(placeHolder2, "https://media.tenor.com/aZDlttNpGroAAAAi/mind-blowing-cat-mind-blown.gif", 300)
    time.sleep(2)
    placeholder_gif(placeHolder2, "https://media.tenor.com/h_jy2s28rlYAAAAj/spinning-cat.gif", 300)
    
    

    


# Create two columns: left for PNG, right for chat
# col1, col2 = st.columns([1, 1])  # Adjust ratio if needed

# # --- Left column: character image ---
# with col1:
#     st.image("https://media.tenor.com/7UHqqhLP8tgAAAAi/stk.gif", caption="Brr! I'm feeling cold ❄️", width=165)

# # --- Right column: boxy chat ---
# with col2:
#     with st.container(border=True):
#         st.subheader("💬 Chat")

        
        
# centered_and_bigger_button("Click Me!!!")




