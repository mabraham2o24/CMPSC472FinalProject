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
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/450acd57-e223-4195-b844-ca2d8ab8865f)


+ You can choose any three options. The instructions for each menu option is as follows:
  + Option 1: Survey
    + Click the first option called 'Survey'. Once you open up this option, you will be prompted to fill out a questionaire.
    + There are 9 questions and you rate your answer from a scale 1 to 5. For instance, the first question asks about how often do you consume alcohol or drugs. Your answer will be somewhere on a scale from 1 to 5. Each question has a drop down menu where you choose your rating.
      + ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/ca72f6c5-23ba-4afe-98af-2384871cd42d)

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

--------------------------------------------------------------------------------------------------------------------------------------

  + Option 3: Stories
    + Click on the option 3 for Good News.
    + This will take you to a page labeled 'Stories To Bring Awareness" where you can pick a category and generate a random news article.
      ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/7b07618d-6875-4f3e-bd85-870a77440c56)

    + Choose an article type by clicking on the drop down menu and choosing one of the categories.
      ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/8b05f0df-5329-4fc6-b0e5-a344d5b86432)

    + Once you choose a category, click Generate Article.
    +  ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/5d974af7-f196-4d48-ba75-c88a581117b1)


    + This will generate a random article that you can read. Once an article is generated, you will be provided with the article title, source, and a read more option. Click the 'read more' option to go to the article.
      ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/a3a49fda-8648-43c4-89d3-e99e3eb1c3bd)

    + This will open up the article in a new tab of the web browser you are in and you can read the article.
------------------------------------------------------
  + Option 4: Resources
    + Click on the option 4 called Resources. When you go this page you will see four different tables contained 3 resources for different categories such as support groups and online resources.
      ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/223e1ff2-4f0e-49b0-b0f1-0d5c61efcbad)
------------------------------------------------------
  + Option 5: Statistics
    + Click on option 5 called Statistics and you will be taken to a page that lists out different stats that shows how bad the drug epidemic is. It has tables listing out numbers, percentages, etc along with some diagrams for visualizing these statistics for different substances. 
     ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/a90c0f9b-1f0a-4863-b4ca-78506de9b37c)



-----------------------------------------------------------------------------------------------------------
# ***Structure of the Code***
This diagram is for our app2.py:
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/a8f5c01f-1e5f-4fa3-a203-fea84e9dbb96)


This diagram is for our migrate_passwords.py:
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/4bde0f31-1dbb-4b03-861e-2242ded54e04)


-------------------------------------------------------------------------------------------------------------------------

# ***Functionalities and Test Results***
+ Function 1 - Create an Account
+ ![Screenshot 2024-04-22 103055](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/eea213de-6035-435f-b2b0-db8cb493f353)
+ ![Screenshot 2024-04-22 103235](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/af6dc321-a04e-43fb-95ca-7ac5e93d9a3e)


+ Function 2 - Choosing a menu option
+ ![Screenshot 2024-04-22 103350](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/ba89512a-4b45-4656-b83e-427a93b7bb6d)


+ Function 3 - Fill Out a Survey and Get Back the Results
+ ![Screenshot 2024-04-22 103508](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/f625a989-a6ce-4d6e-9121-9590f5b8c50e)
+ ![Screenshot 2024-04-22 103612](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/33205a3b-994f-4e09-b199-b554d7852574)


+ Function 4 - Can journal using our option 2 in the menu and write down your thoughts.
+ ![Screenshot 2024-04-22 103707](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/2bf9f567-bd3c-4914-ace8-bcdf91c04508)


+ Function 5 - Generate News article choosing one of the catagories provided. Once you choose a category, hit generate article and then click read more which will open up a new tab with the article of your choosing.
+ ![Screenshot 2024-04-22 112609](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/a90d1bf5-f5cd-49ef-9071-08e9f2ab8f8b)
+ ![Screenshot 2024-04-22 112625](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/fe94a37a-e7a8-4ac0-ac9b-39b896019f04)
+ ![image](https://github.com/mabraham2o24/CMPSC472FinalProject/assets/143213640/e9343e77-49b8-4100-a3f6-322d4db112fd)
# ***Demo***
+ The video of a brief demo is uploaded onto this repository and can be found on the homepage. 

----------------------------------------------------------

# ***What we Included from the Lectures***
+ Database Interactions:
  + Every time we interact with our SQLite database, whether creating it, inserting data, or querying it, system calls are invoked to access the file system and manage data on the disk.
+ Processing User Input:
  + When a user submits their survey, Flask handles the incoming network data (a system call), processes it, and stores the results, which again invokes system calls for writing to the database.
+ Rendering and Sending Responses:
  + Rendering HTML templates and sending them back to the user involves system calls that read template files and send the resultant HTML over the network back to the user's browser.
+ Logging In and Session Management:
  + As users log in, their credentials are verified against the database, requiring file system access, and sessions are managed, necessitating memory management—both are system call dependent.

+ Survey Results:
  + When you fetch survey results from a data structure in your web application, system calls are at work behind the scenes. As your program retrieves the data from memory to calculate scores, system calls for memory access are implicitly issued by the operating system. Finally, system calls also handle sending the calculated results back to the user through the network, completing the process from data retrieval to response delivery.


# ***Discussion and Conclusions***
+ Our main project issue was coming together and combining all of our code. Neither Mohamed or I had mucg time to meet up and work together. So for the sake of the project we split up the features being implemented and then came together at the end to put everything together. I did the first 3 options and he did the last two. Combining the code caused quite a few issues because our app2.py files were different so having to go in and fix all the errors was just a bit time consuming. Another issue I, Mahima, personally had was trying to save the journal entries. I wanted the user to be able to go back and visit their old posts but for some reason I was not able to get that to work. It was causing a lot of errors and crashing the website so we had to just scratch the idea of saving previous entries. Github codespaces was also causing some issues when it came to launching the website. 
+ Our biggest and really only limitation was time. We both had a lot of other work to do for other classes and was busy with personal stuff. Time was just very limited due to our schedules never meeting up and constantly having work for other classes. If we had more time we would have fixed the journaling issue and would have added more features such as an active page where the user can click on a link and it will directly lead them to a hotline. Or just any feature that can help with this topic. We feel like this web application has so much more potential but due to tome constraints we just cannot do anything about it. 
+ Our goal for this project was to build a user interface that is easy to access and navigate for any user. We also wanted this web application to have some features that can actually be useful for recovering addicts or for those who are looking to go on a recovery journey. In the beginning of the semester one of the first things we learning about was UI/UX and we wanted to use what we learned and develop a simple yet useful interface.
