import tkinter
import customtkinter
import requests
from bs4 import BeautifulSoup

def getHtmlFile(url):
    req = requests.get(url)
    return req.text # this will return entire HTML document

def getArticleData():
    url = link.get()
    print(url)
    new_url = "https://"+url.replace("https://","").replace("http://","")
    soup = BeautifulSoup(getHtmlFile(new_url),'html.parser')
    articleText.configure(state="normal")
    articleText.delete("0.0","end")
    title = soup.find('title')
    app.title(f"Artix - {title.get_text()}")
    for headers in soup.find_all(['h1','h2','h3','h4']):
        articleText.insert("end",text=f"\n# {headers.get_text()} \n\n")
        for element in headers.next_elements:
            if element.name and element.name.startswith('h'):
                break
            if element.name == 'footer' or element.name == 'nav' or element.name == 'form':
                break
            if element.name == 'p':
                articleText.insert("end",text=f"{element.get_text()} \n\n")
            if element.name == 'ol':
                nested_lists = element.find_all('li')
                count = 0;
                while(count < len(nested_lists)):
                  articleText.insert("end",text=f"{count+1}. {nested_lists[count].get_text()}\n")
                  count+=1
    articleText.configure(state="disabled")


# setting up the system
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# Create tkinter screen
app = customtkinter.CTk()
app.geometry("700x500")
# Bitmap is currently disabled as it causes errors on some platforms
# app.iconbitmap("📄")
app.title("Artix")


# Creating a frame
frame = customtkinter.CTkFrame(app,height=35,width=750)
frame.grid_rowconfigure(0,weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.pack(padx=5,pady=5)

# Take an entry
link = customtkinter.CTkEntry(master=frame,width=600,height=25,state="normal",placeholder_text="Enter an article's url to load")
link.grid(row=0,column=0,padx=10,pady=5,sticky="")

#Button
go_button = customtkinter.CTkButton(master=frame,text="GO",command=getArticleData)
go_button.grid(row=0,column=1,padx=5,pady=5,sticky="")

# Print Text
articleText = customtkinter.CTkTextbox(app)
articleText.configure(wrap="word",state="normal")
articleText.pack(fill="both",padx=15,pady=10,expand=True)
articleText.insert("0.0","Enter an article link in the above bar and press on go button to load the article. This does't work as a search!")

# run the app
app.mainloop()