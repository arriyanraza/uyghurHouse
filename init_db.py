import sqlite3

def init_db():
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('guestbook.db')
    c = conn.cursor()

    # Create table
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            website TEXT,
            location TEXT
        )
    ''')

    # Add some sample entries
    sample_entries = [
        ('CyberNinja', 'First post in the guestbook! Love the retro vibes!', 'https://github.com/cyberninja', 'San Francisco'),
        ('HackerX', 'Cool hacker house! Keep up the great work!', '', 'New York'),
        ('ByteWarrior', 'Awesome ASCII art!', 'https://twitter.com/bytewarrior', 'Tokyo')
    ]

    c.executemany('''
        INSERT INTO entries (name, message, website, location)
        VALUES (?, ?, ?, ?)
    ''', sample_entries)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("Initializing database...")
    init_db()
    print("Database initialized successfully!")
