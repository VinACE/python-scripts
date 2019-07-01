# https://www.geeksforgeeks.org/rename-multiple-files-using-python/
# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    import pdb; pdb.set_trace()
    for filename in os.listdir("/home/superadmin/mrcnn/IDRBT Cheque Image Dataset/300"): 
        dst = str(i) + ".jpg"
        src = "/home/superadmin/mrcnn/IDRBT Cheque Image Dataset/300/" + filename 
        dst = "/home/superadmin/mrcnn/IDRBT Cheque Image Dataset/300/" + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 