import pandas as pd
import os


try:
    for code in pd.read_csv("course.csv").Code.tolist():
        os.system("youtube-dl.exe https://fast.wistia.net/embed/iframe/" + code)
        for filename in os.listdir():
            #print(f"mp4-{code}.bin")
            if f"mp4-{code}.bin" in filename:
                #print("True")
                new_name = filename.replace(f"mp4-{code}.bin", "mp4")
                os.rename(filename,new_name)
                print("! Change : " + filename + " >>> " + new_name)
            else:
                #print("False")
                pass
finally:
    pass
    
    
        

    




