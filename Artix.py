import tkinter
import customtkinter
import requests
from bs4 import BeautifulSoup

def getHtmlFile(url):
    req = requests.get(url)
    return req.text # this will return entire HTML document

def getArticleData():
    url = link.get()
    new_url = "https://"+url.replace("https://","").replace("http://","")
    soup = BeautifulSoup(getHtmlFile(new_url),'html.parser')
    articleText.delete("0.0","end")
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



# setting up the system
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create tkinter screen

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Artix")
app.iconbitmap("📄")


# Take an entry
url_link = tkinter.StringVar()
link = customtkinter.CTkEntry(master=app,width=700,height=30,textvariable=url_link,placeholder_text="Enter a URL")
link.pack(padx=5,pady=5,fill="both")

#Button

go_button = customtkinter.CTkButton(master=app,text="GO",command=getArticleData,width=200)
go_button.pack(padx=5,pady=5)

# Print Text
articleText = customtkinter.CTkTextbox(app)
articleText.configure(wrap="word",text_color="lightgreen")
articleText.pack(fill="both",padx=15,pady=10,expand=True)

# run the app

app.mainloop()