import os

def binoddetector(filename):
    with open(filename,'r') as f:
        filecontent=f.read()
        if 'binod' in filecontent.lower():
            return True
        else:
            return False


if __name__=="__main__":
   dir_content=os.listdir()
   nbinod=0
   for items in dir_content:
       if items.endswith('.txt'):
        # print(items)
        print("----Detecting Binod----")
        found=binoddetector(items)
        
        if(found):
            print(f"Binod Found In {items}!!!")
            nbinod+=1
        else:
            print(f"Binod not found in {items}")    
                     
print("|||Binod summary|||")
print(f"{nbinod} found into the given directories.")    
    