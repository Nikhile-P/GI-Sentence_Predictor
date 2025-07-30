# 🤖 Next Sentence Predictor

\[Hugging Face LLM]  [Static Badge](https://img.shields.io/badge/!%5BProject%20Badge%5D(https%3A%2F%2Fimg.shields.io%2Fbadge%2FProject-Sentence_Predictor-blue))


A web application for real-time, controllable text generation using a pre-trained GPT-2 model. This project demonstrates the implementation of a generative AI system in an interactive and user-friendly front end.

-----

## ✨ Features

  * **Dynamic Text Generation**: Produces multiple, unique sentence completions from a user-provided prompt.
  * **User-Controlled Parameters**: Allows for real-time adjustment of key generation parameters, including maximum length and creativity.
  * **Optimized Model Caching**: Utilizes Streamlit's `@st.cache_resource` to load the model into memory once, ensuring minimal latency.
  * **Modern UI/UX**: A polished, two-column interface designed for intuitive interaction and clear presentation of results.

-----

## 🛠️ Tech Stack

  * **Python** 3.9+
  * **Streamlit** for the web interface
  * **HuggingFace Transformers LLM Model**
  * **GPT-2** as the base model
  * **PyTorch** as the backend tensor library

-----

## 📦 Usage & Output

The application provides a direct, interactive experience. The user enters a starting sentence into the input panel, adjusts the optional settings, and clicks the "Predict" button.

The output is rendered directly in the UI, with each of the three generated sentence predictions displayed in its own distinct container for clarity.

-----

## 🚀 Setup and Usage

To get this project running locally, follow these steps.



https://github.com/user-attachments/assets/1fcf43d1-6d66-4679-b9f3-7d1cb7be1484

### 1\. Clone the Repository

```bash
git clone https://github.com/edwin14631/GenAI-Proj.git
cd GenAI-Proj
```

### 2\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3\. Run the Application

Execute the main script to launch the Streamlit web server.

```bash
streamlit run app.py
```

The application will be accessible at `http://localhost:8501`.

-----

📄 License
This project is licensed under the MIT License.
