# from pytube import YouTube

# yt = YouTube ("YOUTUBE_URL")
# audio = yt.streams.filter(only_audio=True).first()
# audio.download()



import os
import requests

# dump_directory = os.path.join(os.getcwd(), 'mp3')
# os.makedirs(dump_directory, exist_ok=True)


# def dump_mp3_for(resource):
#     payload = {
#         'api': 'advanced',
#         'format': 'JSON',
#         'video': resource
#     }
#     initial_request = requests.get('http://youtubeinmp3.com/fetch/', params=payload)
#     if initial_request.status_code == 200:  # good to go
#         download_mp3_at(initial_request)


# def download_mp3_at(initial_request):
#     j = initial_request.json()
#     filename = '{0}.mp3'.format(j['title'])
#     r = requests.get(j['link'], stream=True)
#     with open(os.path.join(dump_directory, filename), 'wb') as f:
#         print('Dumping "{0}"...'.format(filename))
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:
#                 f.write(chunk)
#                 f.flush()






# import urllib.request
# import json

# r = urllib.request.urlopen('https://www.hotstar.com/in/shows/devon-ke-dev-mahadev/12/shiva-is-angry/1000000234/watch?filters=content_type%3Depisode')
# content = r.read()
# # extract download link
# download_url = json.loads(content)['link']
# download_content = urllib.urlopen(download_url).read()
# # save downloaded content to file
# f = open('test.mp4', 'wb')
# f.write(download_content)
# f.close()








import requests  
from bs4 import BeautifulSoup  
  
'''  
URL of the archive web-page which provides link to  
all video lectures. It would have been tiring to  
download each video manually.  
In this example, we first crawl the webpage to extract  
all the links and then download videos.  
'''
  
# specify the URL of the archive here  
archive_url = "https://www.hotstar.com/in/shows/devon-ke-dev-mahadev/12/shiva-is-angry/1000000234/watch?filters=content_type%3Depisode"
  
def get_video_links():  
      
    # create response object  
    r = requests.get(archive_url)  
      
    # create beautiful-soup object  
    soup = BeautifulSoup(r.content,'html5lib')  
      
    # find all links on web-page  
    links = soup.findAll('a')  
  
    # filter the link sending with .mp4  
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]  
  
    return video_links  
  
  
def download_video_series(video_links):  
  
    for link in video_links:  
  
        '''iterate through all links in video_links  
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string  
        file_name = link.split('/')[-1]  
  
        print( "Downloading file:%s"%file_name)  
          
        # create response object  
        r = requests.get(link, stream = True)  
          
        # download started  
        with open(file_name, 'wb') as f:  
            for chunk in r.iter_content(chunk_size = 1024*1024):  
                if chunk:  
                    f.write(chunk)  
          
        print( "%s downloaded!\n"%file_name ) 
  
    print ("All videos downloaded!") 
    return
  
  
if __name__ == "__main__":  
  
    # getting all video links  
    video_links = get_video_links()  
  
    # download all videos  
    download_video_series(video_links)  
      
  
     