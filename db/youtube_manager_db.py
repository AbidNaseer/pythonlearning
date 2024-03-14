import sqlite3

conn = sqlite3.connect('youtube.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time NOT NULL
        )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_videos(name , time):
    cursor.execute("INSERT INTO videos (name ,  time) VALUES (? ,?)", (name, time))
    conn.commit()


def update_videos(video_id , name , time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube manger  app with DB") 
        print("1 . List videos ")
        print("2 . add videos ")
        print("3 . update videos ")
        print("4 . delete videos ")
        print("5 . exit app")
        choice = input("enter your choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name =input("enter the video name")
            time = input("enter the video time")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("enter the video ID to update")
            name =input("enter the video name")
            time = input("enter the video time")
            update_videos(video_id,name, time)
        elif choice == '4':
            video_id = input("enter the video ID to update")
            delete_videos(video_id)
        elif choice == '5':
            break
        else :
            print("invalid choice")
            
conn.close()


if __name__ == "__main__":
    main()

