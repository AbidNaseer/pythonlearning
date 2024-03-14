import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)



def list_all_videos(videos):
    for index , video in enumerate(videos, start=1):
        print("\n")
        print("*" * 70)
        print(f"{index}. {video['name']},Duration: {video['time']} ")
        print("\n")
        print("*" * 70)
def add_videos(videos):
    name = input('enter video name')
    time = input('enter video time')
    videos.append({'name': name , 'time': time})
    save_data_helper(videos)


def update_videos(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to update"))
    if 1<= index <=len(videos):
        name =input("enter the new video name")
        time =input("enter the new video time")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("there's nothing")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to be deete"))
    if 1<= index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid ")

def main():
    videos = load_data()
    while True:
        print("\n Youtube manager")
        print("1 . List a favorite videos")
        print("2 . add a youtube video")
        print("3 . update a youtube details")
        print("4 . delete a youtube video")
        print("5 . exit the app")
        choice = input("enter your choice")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main() 
