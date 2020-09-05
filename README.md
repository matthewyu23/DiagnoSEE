# Things we have to do: 
- Database to store links / videos.

# Things that our webapp will do:
- Input blurry video files and output clean videos
- Needs to be a video watching thingy
    - Users should be able to download videos
    - ALSO allow them to send a timestamp of a certain place in the video along with their comments in the chat
- Could be a place for physicians to put their notes
    - Could be an instant messaging thing
    - A place where physicians and patients can talk about symptoms, course of treatment, etc.
- Allow users to point out errors in the cleaned up videos BEFORE videos are sent to one another (physician to patient and patient to physician)
    - Can send close-up images of the parts that were GAN-ed incorrectly
    - Can note when (what time out of the video) the user pauses and comments the error
    - Use something like onclick() or a custom button to note down the time
- Needs to be some way that we can actually fix the GAN model
    - Use the close-up image the user has sent and the video time it was commented at

# Visual Layout
- one page where user can choose between uploading videos and viewing chat
- one page where user can input/upload the blurry video file
    - on the same page (although different endpoints), the new clear video will be on the video player and available for download
    - on the same page (but different endpoints), the user can playback the clear video, pause it where it's innaccurate, and take a close-up picture of what the image should be
        - user can then send the timestamped video, correct picture, etc., in a message
- one page for instant messages
    - users should be able to view videos while in the chat
    - users should be able to view a full chat history
    - users should only be able to speak to "friends" like in facebook, ig, etc. otherwise, it's not private

# Frontend endpoints
- Registration and login function (for both the patient and the physician), saved to database
- Allow users to submit video file, save file to cloud, store file path to database, return new and rendered video to client-side
- 

# Database Tables
### Users 
- id (int)
- name (String) - first and last name
- username (String)
- password (String - hash) 
- define the user as a physician/patient (User)
### Video
- id (int)
- user (int) - user id
- filepath_old (String) - for the old (blurry) video. limit video time to (10~15 seconds) to reduce computation time. One user can have multiple rows in the video db if they have submitted multiple videos.
- filepath_new (String) - for the new (clear) video. limit video time to (10~15 seconds) to reduce computation time. One user can have multiple rows in the video db if they have submitted multiple videos.
- comment (String) - physician comment

# Backend workings
- Simply need to run the video into the GAN model
- Incorporate TecoGAN into flask app
- Return video for downloading or viewing in a web player.

# Roles 
- Christina
    - figure out/write video player stuff
    - ALSO allow them to send a timestamp of a certain place in the video along with their comments, to the chat
    - create button that allows users to download video (on the same page as video player)
    
# Flask stuff 
# Learning how to use TecoGan
# Final presentation
# Devpost 
- 5 minute video and written devpost submission.

How this will be written:

# Tentative Schedule
### Friday:
- Figure out how to do project
- Figure out if we’re using Heroku, AWS, etc.
- Assign roles
- Set up heroku stuff
- Learn how to use TecoGan
- Start coding!

### Saturday 
- Record video, retouch video if needed

### Sunday 
- Win the competition.

*Contributors: Matthew Yu, Alan Sun, Christina Wang, Vani Gupta, Jinay Jain*