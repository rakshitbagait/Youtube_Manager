import pymongo

client = pymongo.MongoClient("mongodb+srv://youtubepy:rakshit9205@cluster0.tolmitj.mongodb.net/?appName=Cluster0")

db = client["Youtube_Manager"]

video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
        print(f"Id:{video['_id']},Name:{video['name']}and Time:{video['time']}")
def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one({'_id':video_id},
                                {"$set":{"name":new_name,"time":new_time}}
                                )
def delete_video(video_id):
    video_collection.delete_one(
        {"_id":video_id}
    )
def main():
    while True:
        print("\n Youtube Manager App")
        print("1.List All videos \n 2.Add a new video\n 3.Update videos\n 4.Delete a video\n 5.Exit the app")
        choice = input("Enter your choice")
        if choice =='1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name")
            time = input("Enter video Time")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter the video id ")
            name = input("Enter updated video name")
            time = input("Enter updated video Time")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter the video id ")
            delete_video(video_id)
        elif choice=='4':
            break
        else:
            print("Invalid choice")



if  __name__=="__main__":
    main()
