# 🚀 Streamlit Mastery: Interactive Web Components

A clean, modular repository documenting my hands-on journey of mastering **Streamlit** for building interactive UI components and data-driven web applications in Python.

---

## 📌 Project Overview

This repository captures practical implementations of Streamlit widgets, layout controls, and user interactions. Each module demonstrates practical usage, custom styling options, and dynamic event handling.

---

## 🛠️ Tech Stack & Setup

* **Language:** Python 3.9+
* **Framework:** [Streamlit](https://streamlit.io/)

### Installation & Run

1. **Install Streamlit:**
   ```bash
   pip install streamlit

```

2. **Run the Application:**
```bash
streamlit run app.py

```



---

## 🎯 Concepts Covered

### 1. Button Types & Layout Control (`st.columns`)

* **Multi-Column Alignment:** Divided UI elements evenly into 3 columns using `st.columns(3)`.
* **Button Variants:**
* `type='primary'`: High-priority call-to-action button.
* `type='secondary'`: Standard default button style.
* `type='tertiary'`: Low-emphasis borderless button.


* **Responsive Width:** Applied `width='stretch'` to ensure buttons fit their container fluidly.

### 2. Custom Icons & Event Handling

* **Plain Buttons:** Basic click detection and standard text rendering via `st.markdown()`.
* **Emoji Icons:** Custom button branding using native emojis (`icon="🦢"`).
* **Material Design Icons:** Modern iconography leveraging Streamlit's built-in Google Material symbols (`icon=":material/downloading:"`).

---


## 🗺️ Learning Roadmap

* [x] **Phase 1: Layouts & Buttons**
* [x] Header & Subheader structures
* [x] Multi-column grid (`st.columns`)
* [x] Button hierarchy (`primary`, `secondary`, `tertiary`)
* [x] Icon integration (Emoji & Material)


* [ ] **Phase 2: User Inputs**
* [ ] Text inputs, Text areas, & Number inputs
* [ ] Sliders, Selectboxes, & Checkboxes


* [ ] **Phase 3: Data Display & Tables**
* [ ] Interactive DataFrames (`st.dataframe`)
* [ ] Static Tables & Metrics (`st.metric`)


* [ ] **Phase 4: Visualizations & Media**
* [ ] Plotly & Matplotlib integration
* [ ] Audio, Video, and Image assets


* [ ] **Phase 5: State Management**
* [ ] Session State (`st.session_state`) & Callbacks

