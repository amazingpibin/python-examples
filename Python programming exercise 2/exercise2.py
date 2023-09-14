import sqlite3

# Function to create the SQLite database and table
def create_database_and_table():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
            movieID INTEGER PRIMARY KEY AUTOINCREMENT,
            movieName TEXT,
            movieYear INTEGER,
            imdbRating REAL
        )
    ''')
    conn.commit()
    conn.close()

# Function to read the file and populate the database
def populate_database_from_file():
    with open('stephen_king_adaptations.txt', 'r') as file:
        lines = file.readlines()
    
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 4:
            movie_id, movie_name, movie_year, imdb_rating = parts
            cursor.execute('''
                INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating)
                VALUES (?, ?, ?)
            ''', (movie_name, int(movie_year), float(imdb_rating)))
    
    conn.commit()
    conn.close()

# Function to search for movies based on user's choice
def search_movies():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    while True:
        print("\nOptions:")
        print("1. Movie name")
        print("2. Movie year")
        print("3. Movie rating")
        print("4. STOP")
        choice = input("Enter your choice: ")

        if choice == '1':
            movie_name = input("Enter the name of the movie: ")
            cursor.execute('''
                SELECT movieName, movieYear, imdbRating
                FROM stephen_king_adaptations_table
                WHERE movieName = ?
            ''', (movie_name,))
            result = cursor.fetchone()
            if result:
                print("Movie Found:")
                print(f"Name: {result[0]}")
                print(f"Year: {result[1]}")
                print(f"Rating: {result[2]}")
            else:
                print("No such movie exists in our database")

        elif choice == '2':
            movie_year = input("Enter the year: ")
            cursor.execute('''
                SELECT movieName, movieYear, imdbRating
                FROM stephen_king_adaptations_table
                WHERE movieYear = ?
            ''', (int(movie_year),))
            results = cursor.fetchall()
            if results:
                print("Movies Found:")
                for result in results:
                    print(f"Name: {result[0]}")
                    print(f"Year: {result[1]}")
                    print(f"Rating: {result[2]}")
            else:
                print("No movies were found for that year in our database.")

        elif choice == '3':
            rating = input("Enter the minimum rating: ")
            cursor.execute('''
                SELECT movieName, movieYear, imdbRating
                FROM stephen_king_adaptations_table
                WHERE imdbRating >= ?
            ''', (float(rating),))
            results = cursor.fetchall()
            if results:
                print("Movies Found:")
                for result in results:
                    print(f"Name: {result[0]}")
                    print(f"Year: {result[1]}")
                    print(f"Rating: {result[2]}")
            else:
                print("No movies at or above that rating were found in the database.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.")

    conn.close()

# Main function
def main():
    create_database_and_table()
    populate_database_from_file()
    search_movies()

if __name__ == "__main__":
    main()
