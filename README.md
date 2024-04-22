<h1 align="center">472 Final Project -Pathways of Hope: Navigating Addiction</h1>
<h1 align="center">Mahima Abraham and Nohamed Chikani</h1>

Discussion and Conclusions: Address project issues, limitations, and how your course learnings were applied.
# ***Project Goals***
+ The goal of this project was to create a web application that users can use for five different features that is displayed on a menu after they login to their account. They can already have an exisiting account or can create a new one.:
  + Survey - Answer a questionaire about how often they drink, use subtances, how they are feeling, etc.
  + Journaling - They can use this option to journal about anything they want to just write down which they can access again by just signing into their account.
  + Stories - There are four categories of articles - Recovery Stories, Impact of Addiction, and Statistics - that users can choose from. Once they choose a category, they can randomly generate an article for them to read. For the sake of this project we have 5 articles each.
  +  Resources - This option contains different resources within Pennsylvania people can use to reach out for help.
  +  Statistics - This options shows important statistics when it comes substance/drug usage.

# ***Significance of the Project (10%)***
+ Drug addiction or any substance abuse of that matter is a serious issue that is taking over our country and other parts of the world. It is a serious topic that a lot of individuals have a hard time to talk about or to find resources that could help them with their recovery. We wanted to create a simple web application that has different types of resources that the user can use. They have a simple survey they can take that asks they about different questions about their addiction, mental state, etc. Once they answer it they can get back results which contains some simple advice and where they have been rated. Second, they have a journaling option. When recovering from addiction or just struggling with having to break it the individual might not have anybody to talk to. Or they can be afraid to reach out. Having a place where they can write down their thoughts on how they are feelings for the day and not having to show it to anyone can be an important step towards recovering. So we wanted to include this option so the user can use it to get out whatever they are feeling without having to talk to someone directly. The third option is called Stories. It has three different categories like mentioned in the introduction. We wanted to include this option to bring awareness to the issue that is drug addiction. Sometimes people do not know how bad something is without reading or seeing something for themselves. Our fourth option is called Resources. We think it is vital to have resources that the user can use to reach out for help. Sometimes a person might get overwhelmed with having to find resources to reach out for help. So we thought it was vital to include that so we can give someone the push to reach out for help. For the sake of this project we just included resources within Pennsylvania. Last but not least we included statisitcs so we can really put into perspective how bad this epidemic is. 

# ***Installation and Instruction to Use***
## Installation
+ Open up our repository on github.
  + link: https://github.com/mabraham2o24/CMPSC472FinalProject.git
+ Once you are in our repository, click the 'period' key on your keyboard which will open up github codespaces. It will look something like this:
![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/d8352f1e-e91c-4352-b941-42053c9ea8e8)

+ Once codespace is opened, click on the 3 lines at the top left corner above the little file sign. It looks like this:
+ ![Screenshot 2024-04-22 102456](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/3f2abe03-70db-40bf-8dc3-2aa72b9b6994)


+ You will see an option called 'Terminal'. Hover over it and you will see an option called 'New Terminal'. Click on that to open a new terminal.
![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/d43df8bd-96ae-4d35-9bf2-f089d65e973b)


+ Once you click on 'New Terminal', a terminal will pop up and you will be prompted to choose where you want to continue working, Github Codespaces or a New Local Clone. Choose Github Codespaces.
![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/db292e30-d3b3-4b47-8331-94a9e9118503)

+ Once you choose github codespaces, you will be prompted to choose the instance type for your code space - 2 Cores, 8GB RAM, 32 GB storage or 4 Cores, 16 GB RAMS, 32 GB storage. You can choose either one depending on your preference and how much space you want it to use.
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/871a3ee7-5591-4254-bc4d-1ad58fbdf281)
  
+ Once you choose either 2 Cores or 4 Cores, a new tab will open up and this will be your codespace.
+ Once the codespace loads, the terminal you are going to run the application is will open up.
![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/32c13a3f-f41b-4fe7-8521-8107e63a8163)


+ Now that you have a terminal open, run the command 'pip install flask'. We need this to run our website.
![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/92b6e262-b10f-4964-a751-bdf7e1c18b4e)


+ Once flask has been installed, the command line prompt will pop up again where you are going to run the command to launch the application.
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/655615ff-e121-483c-ab8b-753cad2cb934)


+ Now you will run the command 'python app2.py'which will run our application.
![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/e614ff4b-e561-4093-9324-a84e94208531)

----------------------------------------------------------------------------------------------------------------------------------
## Instruction to Use
+ There are two ways to open up the website:
  + First way:
    + You can hover your mouse over the url link given in the command prompt. When you hover over it, a little screen will pop up saying 'Follow Link'. Click on that and the website will opened in a new tab of your web browser.
    ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/704bc463-0383-4d6c-af3f-d4b57925ce1d)
    ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/c10d8663-cfc5-4d36-a12f-f02fded9c403)
  + Second Way:
    + Once you run the command, a little window will pop up in the bottom right corner that says 'Open Web Browser'. Click on that and that will launch the website on a new tab of your web browser.
      ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/955f38d2-7a1f-4fd0-9b92-04296514d2b1)
+ Once you have launched the website, you will see a login page. If you already have an account, login with your username and password. If this is your first time using the website, click on 'Don't have an account, Register here.'
+ ![Screenshot 2024-04-22 103055](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/97bb122a-b370-4c6f-87d1-a75f3a6aad7a)

+ You will then go to a 'Register' screen. Choose a username and password and hit 'Register'.
![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/e00e436d-6efe-463c-b945-c3632f14956e)

+ Once you have created an account, you will see a little message that says "Account Created For..." and will end up back on the login page.
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/00c15b30-9012-49b0-b251-4450498d6dea)

+ Log into your new account and you will see a menu.
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/488b8f43-340f-4bb4-b5cd-fbdb883634ec)

+ You can choose any three options. The instructions for each menu option is as follows:
  + Option 1: Survey
    + Click the first option called 'Survey'. Once you open up this option, you will be prompted to fill out a questionaire.
    + There are 9 questions and you rate your answer from a scale 1 to 5. For instance, the first question asks about how often do you consume alcohol or drugs. Your answer will be somewhere on a scale from 1 to 5. Each question has a drop down menu where you choose your rating.
      ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/ca72f6c5-23ba-4afe-98af-2384871cd42d)

    + Answer each question and when you are done click 'Submit'.
    + ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/1d71f832-f488-4ab1-a1cb-37d381072a4d)

    + Once you hit submit, you will get your results based on your ratings. You will also get some advice based on whatever your results is.
      ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/0189f78f-8ce1-429d-90d3-045bbd808ab3)

    ---------------------------------------------------------------------------------------------------------------------------------------
      
  + Option 2: Journaling
    + Click on the option 2 for journaling. This is where you can write down thoughts or whatever you want.
    ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/e852e71f-a60f-48e0-ba44-5a6998d89dcb)
    + Type in whatever you want and click save.
    + ![Screenshot 2024-04-22 104022](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/0c3958c6-29e5-4965-80ea-06f4cf1ed23a)

    + Once you hit 'Save', you entry will appear at the bottom. So, whenever you login you will be able to see all of your past entires.
    ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/0782b40a-0050-4c1d-ab4b-fccc1ee6a099)
--------------------------------------------------------------------------------------------------------------------------------------

  + Option 3: Good News
    + Click on the option 3 for Good News.
    + This will take you to a page labeled 'Good News" where you can pick a category and generate a random good news article.
      ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/bcf78fdf-becc-45f8-803a-d688f4cb12fe)
    + Choose an article type by clicking on the drop down menu and choosing one of the categories.
      ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/b4f983b9-b40f-4196-bcfe-f770169fb1f2)
    + Once you choose a category, click Generate Article.
    +  ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/f23764b0-384a-4928-b4f0-35c2e8658659)

    + This will generate a random article that you can read. Once an article is generated, you will be provided with the article title, source, and a read more option. Click the 'read more' option to go to the article.
      ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/07a751f5-a540-42d2-83eb-78a62d51ea02)
    + This will open up the article in a new tab of the web browser you are in and you can read the article. 

-----------------------------------------------------------------------------------------------------------
# ***Structure of the Code***
This diagram is for our app2.py:
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/cc92d98d-aa93-4a30-a2d0-0d6faa258581)

This diagram is for our migrate_passwords.py:
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/89db9746-68ce-4275-8c3e-6f198d623ff7)

-------------------------------------------------------------------------------------------------------------------------

# ***Functionalities and Test Results***
+ Function 1 - Create an Account
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/ca90db2b-692d-4170-b144-1077d09548ef)
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/3f4cebb6-ab33-412b-a017-206648b56bd2)

+ Function 2 - Choosing a menu option
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/404cb9fc-372b-49a4-b35a-ed62e6fc0125)

+ Function 3 - Fill Out a Questionare and Get Back Mood Results and Advice
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/451510af-1975-4b7e-97ac-85a7868c0743)
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/43657ddd-d3f6-415e-9c35-1d8097ed6695)

+ Function 4 - Can journal using our option 2 in the menu and can save your writings to visit back later.
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/32c603c1-e036-48ac-b76a-b89602df5c2b)
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/ae1cdc93-c3b7-4f99-a5bd-7edec9f08b2d)

+ Function 5 - Generate Good News article choosing one of the catagories provided. Once you choose a category, hit generate article and then click read more which will open up a new tab with the article of your choosing.
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/16b0905d-a5a9-42d3-814d-fe1f1e2be7e6)
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/edfe44aa-386a-41d6-bc32-1b53062fd4be)
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/d0d13638-5e11-4fff-9eee-3378f0aa9155)

## If you want to see a video demo of the application in use(test results) click play below: 
https://github.com/mabraham2o24/463-Final-Project/assets/143213640/1da470a1-08df-4ede-ab38-1558cede60a5

# ***Discussion and Conclusions***
+ Our main project issue was coming together and combining all of our code. For the sake of time and not being to meet all the time we split up this project into parts. Treasure handled the journaling and saving all the information to the database for each user. While I, Mahima, dealt with the login system and good new generator. So, after we finished our individual parts when it came time to combining the codes we had some trouble due to compatibility issues and code errors. We had to spend a bit time on that to get it working together. We both worked together on the Stressometer which did not cause many issues.
+ Our biggest and really only limitation was time. We both had a lot of other work to do for other classes and was busy with personal stuff. Due to that we were not able to spend a lot of time on this project over break like we wanted to. If we had more time we would have added more features to improve our user interface and overall application. We wanted to add more menu options like a sleep tracker. We also wanted to make the good news generator use an API and randomly generate articles rather than hard coding them. Due to our time limit we were not able to implement some of the features we had in mind, but was able to execute the idea on a simple basis.
+ Our goal for this project was to implement one of the algorithms we learned in class. The algorithm that we chose and fit best into our application was quick sort algorithm. We used this for our stressometer option. The user has to fill out a questionaire ranking their emotions and other factors. Once the user submits it, the quick sort algorithm sorts the scores which are used to give the user their results and advice.
+ ![image](https://github.com/mabraham2o24/463-Final-Project/assets/143213640/87e7f1e0-ba51-4b05-87a2-33020ccd9efa)

