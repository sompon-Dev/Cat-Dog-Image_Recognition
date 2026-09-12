import pandas as pd
import os

    

def main():
    train_cats = pd.DataFrame()
    train_cats["Path"] = []
    train_cats["Label"] = []

    train_dogs = pd.DataFrame()
    train_dogs["Path"] = []
    train_dogs["Label"] = []

    current_Path = os.getcwd()
    Oringin_Path_Cat = current_Path+"src\Image\Cats"
    Oringin_Path_Dog = current_Path+"src\Image\Dogs"
    
    Catlist = os.listdir("src\Image\Cats")
    Doglist = os.listdir("src\Image\Dogs")
        
    Catlist_Length = len(Catlist)
    Dogist_Length = len(Doglist)

    #Path_Cat = Oringin_Path+Catlist[0]
    
    print('CatList Length = ',Catlist_Length)
    print(Oringin_Path_Cat)


    print(train_cats)
    for i in range(Catlist_Length):
        Target = Oringin_Path_Cat+Catlist[i]
        print(Target)
        train_cats.loc[len(train_cats)] = [Target, 'Cat']

    print('DogList Length = ',Dogist_Length)
    print(Oringin_Path_Dog)
    for i in range(Dogist_Length):
            Target = Oringin_Path_Dog+Doglist[i]
            print(Target)
            train_dogs.loc[len(train_dogs)] = [Target, 'Dog']

    
    print(train_dogs)
    
    
main()
