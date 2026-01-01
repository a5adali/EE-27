from VideoHistoryHashTable import *
import csv

#Takes in list of Dictionaries in format[{},{}] 
# Returns HashTable in the Format [{'ID':..,"DATA":{}}]
def create_VideoHistory(VideoRecords):
    size=7
    htable=create_hashtable(size)
    for i in range(len(VideoRecords)):
        # print(VideoRecords[i])
        # print(htable)
        data=VideoRecords[i]
        # print(data)
        video_id = data.pop('Video_ID')
        htable, size = put(htable, video_id, data, size)
    return htable
    pass
    
        
    
    
#Takes as input the Hashtable and Name of Operation file 
# Returns a Tuple with two items 
#   1. collision Path in the format {1:[],2:[]} where the keys are the Operation number
#   2. Final HashTable After All Operations performed.
def perform_Operations(H,operationFile):
    collision_path = {}
    with open(operationFile) as f:
        lines = f.readlines()
    count=0
    for line in lines:
        count+=1
        line = line.strip().split(' ')
        x=line[0]
        # video_id = line[1]
        # print(line[1])
        if x== 'Watch':
            full=line[1].split(';')
            video_id = full[0]
            video_url= full[1]
            views=int(full[2])
            likes=int(full[3])
            dislikes=int(full[4])

            y = get(H, video_id, len(H), collision_path, count)
            # print(count,y)
            data=y[0]
            
            if data is not None and data !='#':
                # print(data,'hhhhhh')
                data['Views'] += 1  # Increment the view count
                
            else:
                print(video_id,'THIS COULD')
                y = get(H, video_id, len(H), collision_path, count)
                # print(loadFactor(H,len(H)))
                H,size=put(H,video_id, {'Video_URL':video_url,'Views': views+1, 'Likes': likes, 'Dislikes': dislikes},len(H))
                # print(H)
                # print(loadFactor(H,len(H)))
                # print('PUT HAPPENED')
                
        elif x=='Like':
            video_id = line[1]
            y = get(H, video_id, len(H), collision_path, count)
            data=y[0]
            if data is not None:
                data['Likes'] += 1
        elif x=='Dislike':
            video_id = line[1]
            y = get(H, video_id, len(H), collision_path, count)
            data=y[0]
            if data is not None:
                data['Dislikes'] += 1

        elif x=='Delete':
            video_id = line[1]
            print(loadFactor(H,len(H)))
            H=delete(H, video_id, len(H), collision_path, count)
            
    # print(collision_path)
    return collision_path, H

                

        # print(line[0])

    pass

            

            
#Takes the File name is input 
# Returns the list of Dictionaries to be converted to a hashtable in format [{},{}...]
def main(filename):
    videorecs = []
    
    # Open the CSV file for reading
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';') #; is the seperator
        
        # looping through the file and creating a list of dictionaries
        for row in reader:
            # converting to int
            row['Views'] = int(row['Views'])
            row['Likes'] = int(row['Likes'])
            row['Dislikes'] = int(row['Dislikes'])
            
            
            videorecs.append(row)
    
    return videorecs
    pass
    

# Driver Code
VideoRecords=main('watchedVideos.csv')
print(VideoRecords)
H=create_VideoHistory(VideoRecords)
perform_Operations(H,'Operations1.csv')