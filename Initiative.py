import pandas as pd
import numpy as np
import tkinter as tk

'''
This is the start to the GUI for the app.  The current plan is to use a two part approach.
The back end is going to be a dataframe (for now) the front end is going to be text entries with deleting and updating
the dataframe and entries back and forth.
'''
#GUI Starts Here

root = tk.Tk()

#type variable
types = tk.IntVar()
types.set(0)

tk.Label(root, text = "Welcome to Blood Cobra's Initiative Tracker").grid(row = 0, columnspan = 6)


# Clears output
def clear():
  for label in root.grid_slaves():
    if int(label.grid_info()["row"]) >  5:
      label.grid_forget()
      label.grid_forget()

# Headers
tk.Label(root, text = 'Order').grid(row=1)
tk.Label(root, text = 'Name').grid(row=1,column=1)
tk.Label(root, text = 'Armor Class').grid(row=1, column=2)
tk.Label(root, text = 'Initiative').grid(row=1, column=3)
tk.Label(root, text = 'Max HP').grid(row=1, column=4)
tk.Label(root, text = 'Current HP').grid(row=1, column=5)
tk.Label(root, text = 'Damage/Heal').grid(row=1, column=6)

# Order
for n in range(5):
  tk.Label(root, text = n+1).grid(row=n+2)

# Fields
datas = {}

for n in range(5):
  datas.update({'name ' + str(n):tk.Entry(root, width = 10)})
  datas['name ' + str(n)].grid(row = n+2, column = 1)
  datas.update({'ac ' + str(n):tk.Entry(root, width = 5)})
  datas['ac ' + str(n)].grid(row = n+2, column = 2)
  datas.update({'init ' + str(n):tk.Entry(root, width = 5)})
  datas['init ' + str(n)].grid(row = n+2, column = 3)
  datas.update({'maxhp ' + str(n):tk.Entry(root, width = 5)})
  datas['maxhp ' + str(n)].grid(row = n+2, column = 4)
  datas.update({'currhp ' + str(n):tk.Entry(root, width = 5)})
  datas['currhp ' + str(n)].grid(row = n+2, column = 5)
  datas.update({'damage ' + str(n):tk.Entry(root, width = 6)})
  datas['damage ' + str(n)].grid(row = n+2, column = 6)

cols = ["Name", 'AC', 'Initiative', 'Max HP', 'Current HP']
df = pd.DataFrame(columns = cols)

def sort(df, cols, datas):
  df = pd.DataFrame(columns = cols)
  for n in range(5):
    try:
      data = [
        datas['name ' + str(n)].get(), 
        datas['ac ' + str(n)].get(),
        int(datas['init ' + str(n)].get()),
        datas['maxhp ' + str(n)].get(),
        datas['currhp ' + str(n)].get()
        ]
      dfapp = pd.DataFrame([data], columns = cols)
      df = df.append(dfapp)
    except ValueError:
     pass
  df.sort_values(by = 'Initiative', ascending = False, inplace=True)
  for n in range(df['Name'].count()):
    datas['name ' + str(n)].delete(0, tk.END)
    datas['name ' + str(n)].insert(tk.END, df.iloc[n]['Name'])
    datas['ac ' + str(n)].delete(0, tk.END)
    datas['ac ' + str(n)].insert(tk.END, df.iloc[n]['AC'])
    datas['init ' + str(n)].delete(0, tk.END)
    datas['init ' + str(n)].insert(tk.END, df.iloc[n]['Initiative'])
    datas['maxhp ' + str(n)].delete(0, tk.END)
    datas['maxhp ' + str(n)].insert(tk.END, df.iloc[n]['Max HP'])
    datas['currhp ' + str(n)].delete(0, tk.END)
    datas['currhp ' + str(n)].insert(tk.END, df.iloc[n]['Current HP'])
  if df['Name'].count() < 5 and df['Name'].count() > 0:
    for n in range(5 - df['Name'].count()):
      datas['name ' + str(n+4)].delete(0, tk.END)
      datas['ac ' + str(n+4)].delete(0, tk.END)
      datas['init ' + str(n+4)].delete(0, tk.END)
      datas['maxhp ' + str(n+4)].delete(0, tk.END)
      datas['currhp ' + str(n+4)].delete(0, tk.END) 
def damage(datas):
  for n in range(5):
    if len(datas['currhp ' + str(n)].get()) > 0 and len(datas['damage ' + str(n)].get()) > 0:
      new = int(datas['currhp ' + str(n)].get()) - int(datas['damage ' + str(n)].get())
      datas['currhp ' + str(n)].delete(0, tk.END)
      datas['currhp ' + str(n)].insert(tk.END, str(new))
      datas['damage ' + str(n)].delete(0, tk.END)

def quit(event=None):
  root.destroy()


tk.Button(root, text = "Sort", command = lambda: sort(df, cols, datas)).grid(row = 12)
tk.Button(root, text = 'Damage/Heal', command = lambda: damage(datas)).grid(row = 12, column = 2)
tk.Button(root, text = "Quit", command = root.quit).grid(row = 12, column = 5)
root.bind('<Escape>', lambda e: quit(root))

root.mainloop()
