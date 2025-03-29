import gradio as gr
from password_generator import PasswordGenerator

def generate_password_gradio(length):
    password_generator = PasswordGenerator(length)
    return password_generator.generate_random_password()

def create_interface():
    iface = gr.Interface(fn=generate_password_gradio,
                         inputs=gr.Slider(minimum=8, maximum=64, step=1, label="Şifre Uzunluğu"),
                         outputs="text",
                         live=True)
    return iface

if __name__ == "__main__":
    create_interface().launch()