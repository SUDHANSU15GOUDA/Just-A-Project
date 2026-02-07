import streamlit as st
from base import snow_reset, centered_texts, centered_gif, ocean_divider
import time

st.set_page_config(
    page_title="Stage 1",
    page_icon="https://media.tenor.com/BfwjGMwp30oAAAAj/evil-larry-larry.gif",
    layout="centered")

# placeHolder = st.empty()

snow_reset()
centered_gif("https://media1.tenor.com/m/vrDSZqDOra8AAAAd/oh-no-oop.gif", 300)
centered_texts("Shivering...", 3, "")

if "typed" not in st.session_state:
       st.session_state.typed = False

placeholder1 = st.empty()
# sentence = "I am shivering 🥶 plz enter your name asap and hit enter... Hey you cruel creator I mean Sir I won't demand for cat food... Just don't do this to me 😢 ... Just give me cat treats and I am good 😞."

sentence = "HELLO"

if not st.session_state.typed:

       text = ""
       for char in sentence:
              text += char
              placeholder1.markdown(f"### {text}")
              time.sleep(0.05)
       st.session_state.typed = True
else:
       # Show the full sentence instantly
       placeholder1.markdown(f"### {sentence}")

ocean_divider()

st.write("")
centered_texts("Enter Your Name To Continue... ", 3, "")

name = st.text_input("")

if name:
       
       dashed_name = ""
       for i in name:
              dashed_name = dashed_name + "-" + i
       st.subheader("Wohh... \t" + dashed_name[1::])
       
       if len(name) > 5:
              st.success("Wow you have a long name 😮‍💨... What about your height 😂😂😂")
       st.subheader(f"Hello, {name}! Let's move on to the next step.")

       ocean_divider()

       centered_texts("Let's Verify If You Are A Human Or Let's Just Say Larry", 2, "")
       time.sleep(2)
       centered_gif("https://media.tenor.com/BfwjGMwp30oAAAAj/evil-larry-larry.gif", 300)

       
