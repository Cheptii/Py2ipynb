from IPython.nbformat import v3, v4

# Add file Path without the '.py' at the end.
file_path = ""

with open(file_path+".py") as f:
    text = f.read()
    text += """"""
nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)
    
jsonform = v4.writes(nbook) + "\n"
with open (file_path + ".ipynb", "w") as f:
    f.write(jsonform) 
