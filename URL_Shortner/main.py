import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("URL Shortner")
root.geometry("300x150")

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))


longurl_label = tkinter.Label(root, text="Enter Long URL")
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text="Output shortened URL")
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root, text="Shorten URL", command=shorten)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()



root.mainloop()