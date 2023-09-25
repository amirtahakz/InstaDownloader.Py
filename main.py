from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image, ImageTk
import io






# window configs
window = Tk()
window.title('Home')
window.geometry('600x600')
window.minsize(400,400)
window.maxsize(800,800)

# labels
homeLabel = Label(window, text='Home')
homeLabel.pack()


# buttons
def download():
    downloadBtn.config(text=f'Received {userNameInput.get()}')
    # insta loader
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context,username= f'{userNameInput.get()}')
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    lableImg.config(image=pic)
    lableImg.image = pic
    lableImg.pack()


downloadBtn = Button(window, text='Show', bg='blue', fg='white')
downloadBtn.pack()
downloadBtn.config(command=download)

# inputs
userNameInput = Entry(window, width=50)
userNameInput.pack()





# images
lableImg = Label(window)





window.mainloop()











