import os
for root, dirs, files in os.walk("/Users/purnimasurya/imgtest"):  
    for filename in files:
        name,ext = os.path.splitext(filename)
        if(ext=='.png' or ext=='.jpg'):
            print(filename)