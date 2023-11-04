import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import urllib.parse

def validate_url():
    user_input = entry_url.get()
    try:
        parsed_url = urllib.parse.urlparse(user_input)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            messagebox.showerror("Invalid URL","invalid url")
            return False
    except ValueError:
        messagebox.showerror("Invalid URL","enter the correct url" )
        return False

def scrape_and_display():
    if not validate_url():
        return
    url = entry_url.get()
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    

    class_for_1 = entry_class_1.get()
    
    tag_1 = entry_tag_1.get()
   
    if class_for_1=="" and  tag_1=="" :
         messagebox.showerror("notice","minimum one class or tag should be filled")
    else:
      class1 = soup.find_all(tag_1, class_=class_for_1)
      

      names_text.delete(1.0, tk.END)
      price_text.delete(1.0, tk.END)


   
      for i in class1:
        names_text.insert(tk.END, i.text + '\n')
     
    # Rest of your scraping code goes here...

root = tk.Tk()
root.title("Web Scraping Tool using Python")
root.configure(bg="gray")
 # Set window size

style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels
ttk.Label(frame, text=" ENTER THE URL:").grid(row=0, column=0, sticky=tk.W, pady=(10, 0))
ttk.Label(frame, text=" ENTER THE Class 1:").grid(row=1, column=0, sticky=tk.W)
ttk.Label(frame, text=" ENTER THE Tag 1:").grid(row=2, column=0, sticky=tk.W)

# Entry fields
entry_url = ttk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, columnspan=2, pady=(10, 0), sticky=(tk.W, tk.E))

entry_class_1 = ttk.Entry(frame, width=30)
entry_class_1.grid(row=1, column=1, pady=(5, 0), sticky=(tk.W, tk.E))

entry_tag_1 = ttk.Entry(frame, width=10)
entry_tag_1.grid(row=2, column=1, pady=(5, 0), sticky=(tk.W, tk.E))


# Scrape button
scrape_button = ttk.Button(frame, text="Scrape", command=scrape_and_display)
scrape_button.grid(row=5, column=0)

# Text boxes
names_text = tk.Text(root, wrap=tk.WORD)
names_text.grid()
price_text =tk.Text(root, wrap=tk.WORD)
price_text.grid()

root.mainloop()

