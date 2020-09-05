# foodapp


Things we have to do: 
Database to store links / videos.
Things that our webapp will do:
Input blurry video files and output clean videos
Needs to be a video watching thingy
Could be a place for physicians to put their notes
Could be an instant messaging thing
A place where physicians and patients can talk about symptoms, course of treatment, etc.
Allow users to point out errors in the cleaned up videos BEFORE videos are sent to one another (physician to patient and patient to physician)
Can send close-up images of the parts that were GAN-ed incorrectly
Can note when (what time out of the video) the user pauses and comments the error
Use something like onclick() or a custom button to note down the time
Needs to be some way that we can actually fix the GAN model
Use the close-up image the user has sent and the video time it was commented at
Frontend endpoints
Registration and login function
Have accounts for patients and physicians
Allow users to submit video file, save file to cloud, store file path to database
Etc., etc., FILL OUT LATER
Limit video time to (10~15 seconds) to reduce computation time.
Page to either download or preview the video (maybe with a section for clinician’s notes)=
Backend workings
Simply need to run the video into the GAN model
GAN is already pre-trained for us (yay!!)
Return video for downloading or viewing in a web player.
Fake login page.
Incorporate TecoGAN into flask app

Roles: 
Flask stuff: 
Learning how to use TecoGan
Final presentation
Devpost -- 5 minute video and written devpost submission.

How this will be written:

Tentative Schedule:
Friday:
Figure out how to do project
Figure out if we’re using Heroku, AWS, etc.
Assign roles
Set up heroku stuff
Learn how to use TecoGan
Start coding!


Saturday: 



Sunday: 


