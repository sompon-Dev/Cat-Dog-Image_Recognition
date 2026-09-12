# Cat-Dog-Image_Recognition
This Project is the personal side project to learning the new tools like Pytorch and how Deeplearning work and how to use 

Start Idea : I Got an Dataset is Dog Image and Cata Image each one like 1000 Picture I'll Seperate to 80% Train Data 10% Train Data And 10% to Evaluate

Step 1 : Seperate Data : Calculate Part Cat have 1000 Picture and Dog have 1000 too that mean 10% or 100 picture have to go for test_data and Evaluate_data it's mean it's have to get 100 cat&dog to test and evaluate

Step 1.1 : now I got 800 image Dog&Cat for Train_data and 200 Picture Dog&Cat in Test data I have to seperate 100 picture from Test data to Evaluate data

Step 1.2 : Now complete About Seperate and now I have to go to next step is EDA

Step 2 : I got an Image that from KAGGLE That specific to this Project it's mean their dataset is almost cleaned but after I re-check I see that Name in image each file.jpg is have name that dulpicate like "cat1000.jpg " and the next one is "cat1000.jpg(1)" This problem I solve by manual with hand the process is I Scroll to watch their name of file to see which Image in their name have "(number)" and I just check the next Image that have number that sort or Order to previous one and now I Complete it tooo

Dataset Structure 
 Image:
    Cats: #Train data for cat picture
            Image Cat001.jpg --> Cat800.jpg
    Dogs: #Train data for dog picture
            Image Dog001.jpg --> Dog800.jpg
    Test_data:  #to Test that If Accuracy is low Back to tune Hyperparameter
            Test_Cat:
                        Image Cat801.jpg --> Cat900.jpg
            Test_Dog:
                        Image Dog801.jpg --> Dog900.jpg
    Evaluate_data: #for Evaluate specific value like Recall,Precision,F1-Score
            Cats:
                    Image Cat901.jpg --> Cat1000.jpg
            Dogs:
                    Image Dog901.jpg --> Dog1000.jpg

-------------------------------------------------------------------------------------------------------------

** Data Preparation Is Complete



