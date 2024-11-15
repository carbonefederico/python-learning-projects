import sqlite3

class DatabaseHandler:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS urls (
                    primary_key INTEGER PRIMARY KEY AUTOINCREMENT,
                    url_id TEXT NOT NULL UNIQUE,
                    full_url TEXT NOT NULL,
                    user TEXT
                )
            """)
            # Add an index on `url_id` for faster searches
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_url_id ON urls (url_id)
            """)

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def add_record(self, url_id, full_url, user):
        """
        Adds a new record to the database.
        :param url_id: Unique identifier for the URL.
        :param full_url: The full URL string.
        :param user: The user associated with the URL.
        :return: The primary key of the inserted record.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO urls (url_id, full_url, user) VALUES (?, ?, ?)",
                    (url_id, full_url, user)
                )
                conn.commit()
                return cursor.lastrowid
            except sqlite3.IntegrityError:
                raise ValueError(f"url_id '{url_id}' already exists")

    def get_record_by_url_id(self, url_id):
        """
        Retrieves a record by its `url_id`.
        :param url_id: The `url_id` to search for.
        :return: A dictionary representing the record or None if not found.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM urls WHERE url_id = ?", (url_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "primary_key": row[0],
                    "url_id": row[1],
                    "full_url": row[2],
                    "user": row[3],
                }
            return None

    def get_all_urls(self):
        """
        Retrieves all urls from the database.
        :return: A list of dictionaries representing the urls.
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM urls")
            rows = cursor.fetchall()
            return [
                {
                    "primary_key": row[0],
                    "url_id": row[1],
                    "full_url": row[2],
                    "user": row[3],
                }
                for row in rows
            ]

    def delete_record(self, primary_key):
        """
        Deletes a record by its primary key.
        :param primary_key: The primary key of the record to delete.
        :return: Number of rows deleted (1 if successful, 0 if not found).
        """
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM urls WHERE primary_key = ?", (primary_key,))
            conn.commit()
            return cursor.rowcount
