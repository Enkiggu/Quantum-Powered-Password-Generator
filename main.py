from api import app
import threading

def run_flask():
    app.run(debug=True, use_reloader=False)

def run_gradio():
    from interface import create_interface
    create_interface().launch()

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    run_gradio()
