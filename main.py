from pytube import YouTube

#user input
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)


print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
print("Author: ",yt.author)
print("Channel URL: ", yt.channel_url)
print("Date When Video Was Published: ", yt.publish_date)
print("Keywords: ",yt.keywords)
print("Thumbnail URL: ",yt.thumbnail_url)
print("Video URL: ",yt.watch_url)
print("Channel ID: ",yt.channel_id)
print("The Videos Javascript URL: ",yt.js_url)
print("Embed URL: ",yt.embed_url)
print("Video ID: ",yt.video_id)
print("Description: ",yt.description)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download()
print("Download completed!!")
