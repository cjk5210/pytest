import pyperclip

def copyToSYSPaste(str):
    if str!=None and str.strip()!='':
        pyperclip.copy(str)
        pyperclip.paste()
copyToSYSPaste('Hello World!')