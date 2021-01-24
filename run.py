from reportapp import app
import psycopg2
from reportapp.models import db


def main():
    db.create_all()
    app.run(debug=True)


if __name__ == '__main__':
    with app.app_context():
        main()
