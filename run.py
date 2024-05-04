from flask_app import create_app
import PIL
print('VERSION:', PIL.__version__)

app = create_app()

if __name__ == "__main__":
    app.run()