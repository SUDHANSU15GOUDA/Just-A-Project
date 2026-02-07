import streamlit as st


# balloon reset
def balloon_reset():
  if "balloons_shown" not in st.session_state:
    st.balloons()
    st.session_state.balloons_shown = True

# snow reset
def snow_reset():
  if "snow_shown" not in st.session_state:
    st.snow()
    st.session_state.snow_shown = True
  

# hide the button after clicking
def hide_button():
  st.session_state.button_clicked = True


# markdown for the texts
def centered_texts(text, 
                   level, 
                   color):
  
  style_text = "text-align: center;"
  
  st.markdown(
              f"<h{level} style='{style_text}'>{text}</h{level}>",
              unsafe_allow_html=True
            )


# markdown for the gif
def centered_gif(url, 
                 max_width=None):

  style_url = "display: block; margin-left: auto; margin-right: auto;"
  if max_width:
    style_url += f" max-width: {max_width}px; width: 100%;"
    
  st.markdown(
              f"<img src='{url}' style='{style_url}'>", 
              unsafe_allow_html=True
            )



# placeholder for the texts
def placeholder_texts(placeholder,
                      text, 
                      level, 
                      color):

  style_text = "text-align: center;"

  placeholder.markdown(
              f"<h{level} style='{style_text}'>{text}</h{level}>",
              unsafe_allow_html=True
  )


# placeholder for the gif
def placeholder_gif(placeholder,
                    url, 
                    max_width=None):

  style_url = "display: block; margin-left: auto; margin-right: auto;"
  if max_width:
    style_url += f" max-width: {max_width}px; width: 100%;"
  
    placeholder.markdown(
                f"<img src='{url}' style='{style_url}'>", 
                unsafe_allow_html=True
              )


# add an empty line
def empty_line():
  st.write("")


# button styling
# def centered_button(text):
#   #array
#   col1, col2, col3, col4, col5 = st.columns(5)
#   with col3:
#       st.button(text, 
#                 on_click=hide_button, 
#                 key="centered_button")

def centered_button(placeholder, 
                    text,
                    key,
                    width=300):
  placeholder.markdown(
      f"""
      <style>
      button[kind="secondary"] {{
          display: block;
          margin: 0 auto;
          width: {width}px;
      }}
      </style>
      """,
      unsafe_allow_html=True
  )

  st.markdown('<div id="center-button-container">', unsafe_allow_html=True)
  placeholder.button(
      text,
      on_click=hide_button,
      key="centered_button")
  st.markdown('</div>', unsafe_allow_html=True)



# success styling
def centered_alert(text, 
                   kind):
  #dictionary
    colors = {
        "info":    ("#e8f4fd", "#1f77b4"),
        "success": ("#e6f4ea", "#2e7d32"),
        "warning": ("#fff4e5", "#ed6c02"),
        "error":   ("#fdecea", "#d32f2f"),
    }

    bg, border = colors.get(kind, colors["info"])

    st.markdown(
        f"""
        <div style="
            background-color: {bg};
            border-left: 6px solid {border};
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
            font-weight: 500;
            margin: 1rem auto;
            width: fit-content;
            max-width: 90%;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# soft
st.subheader("Overview", divider=True)
st.markdown(
    "<div style='height:3px;background:linear-gradient(90deg,#6a11cb,#2575fc);border-radius:8px'></div>",
    unsafe_allow_html=True
)


# heat
def heat_divider():
  st.markdown(
      "<div style='height:3px;background:linear-gradient(90deg,#ff512f,#f09819);border-radius:8px'></div>",
      unsafe_allow_html=True
  )


# ocean
def ocean_divider():
  st.markdown(
      "<div style='height:3px;background:linear-gradient(90deg,#2193b0,#6dd5ed);border-radius:8px'></div>",
      unsafe_allow_html=True
  )


# neon
def neon_divider():
  st.markdown(
      "<div style='height:3px;background:linear-gradient(90deg,#00f260,#0575e6);box-shadow:0 0 8px #00f260;border-radius:8px'></div>",
      unsafe_allow_html=True
  )


# pastel rainbow
def pastel_rainbow_divider():
  st.markdown(
      "<div style='height:3px;background:linear-gradient(90deg,#fbc2eb,#a6c1ee,#fddb92);border-radius:8px'></div>",
      unsafe_allow_html=True
  )
