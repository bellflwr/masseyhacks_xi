from dotenv import load_dotenv

load_dotenv()

from masseyhacks_xi import create_app

app = create_app()


def main():
    app.run("localhost", debug=True)


if __name__ == "__main__":
    main()
