import tkinter

window = tkinter.Tk()
window.title("My badass app")
window.minsize(width=500, height=300)
window.config(padx=60, pady=60)

label= tkinter.Label(text="Converter", font=("Arial", 16, "bold"))
label.pack()

t_input = tkinter.Entry()
t_input.pack()

# km_label = tkinter.Label(text="Km", font=("Arial", 12))
# km_label.pack()

miles_label = tkinter.Label(text="miles", font=("Arial", 12, "bold"))
miles_label.pack()

def convert():
    miles = int(t_input.get()) * .62
    miles_label.config(text=f"{round(miles)} miles")

button = tkinter.Button(text="Convert", command=convert)
button.pack()

window.mainloop()