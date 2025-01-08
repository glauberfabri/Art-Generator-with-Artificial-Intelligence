# AI Art Generator

This project is a simple AI-powered application that generates images based on user-provided prompts. It uses the OpenAI API to create artistic images and provides an interactive interface for users.

---

## Features

- **Image Generation**: Enter a text prompt, and the application generates an image based on the input.
- **Interactive Interface**: Simple and user-friendly interface built with Streamlit.
- **Local Storage**: Images generated can be stored locally for future use.

---

## Project Structure

```plaintext
ai-art-generator-python/
├── models/
│   └── art_generator_model.py    # Handles the AI image generation logic.
├── controllers/
│   └── art_controller.py         # Business logic for handling user prompts and model calls.
├── views/
│   └── art_view.py               # Streamlit interface for user interaction.
├── config/
│   └── secrets.toml              # Stores API keys and other sensitive data.
├── main.py                       # Entry point for running the application.
├── requirements.txt              # Project dependencies.
