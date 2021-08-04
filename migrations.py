from db import DB

migrations = [
    ("CREATE TABLE IF NOT EXISTS item ("
        "id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
        "description VARCHAR(255) NOT NULL,"
        "available_amount INT NOT NULL"
     ") ENGINE=INNODB;")
]


def run():
    db = DB()
    cursor = db.get_connection()

    for migration in migrations:
        cursor.execute(migration)
