import pandas as pd
import os

DF = pd.read_csv("course.csv")
try:
    for ind in DF.index :
        os.system("youtube-dl.exe https://fast.wistia.net/embed/iframe/" + str(DF['Code'][ind]))

        for filename in os.listdir():
            if f"mp4-{str(DF['Code'][ind])}.bin" in filename:

                new_filename = str(DF['Name'][ind]) + ".mp4"                
                os.rename(filename,new_filename)
                print("! Change : " + filename + " >>> " + new_filename)
            else:
                pass

finally:
    pass
    
    
        

    





