chat_id ='5831792569'
src = '/sdcard/Download/HD-wallpaper-tokyo-ghoul-kaneki-kaneki-ken-tokio-tokyo-ghoul-thumbnail.jpg'
def sendPhoto(src,chat_id, caption):
  url = "https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/sendPhoto"
  
  image = open(src,'rb')
  files =  {'photo' : image}
  data ={'chat_id': chat_id,'caption' : caption}
  response = requests.post(url, data = data, files= files)
  
