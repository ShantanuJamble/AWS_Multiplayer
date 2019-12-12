#Project Motivation:

This is a research project where I am building the multiplayer game on top of AWS infrastructure.

# Project OutComes:

	1. Hosted FPS game built on Unreal on AWS GameLift
	2. Built microservice for the Temelmetry about Gamelift's performance. The tool is hosted on AWS Lambda which is triggered as a cron job. 
	3. Research different AWS services and choose best suited for the use case.
	4. Testing for scaling support design plan. 

### Unreal Documention for hosting game on AWS GameLift
- [Tutorial on integrating Unreal with Amazon GameLift](https://answers.unrealengine.com/questions/884106/view.html) \
	This covers how to add GameLift Server SDK to the Unreal engine as a module and get it build and packaged with the Unreal engine's package.
- [Using Client SDK by Yeti Tech](https://www.youtube.com/watch?v=2I8JDeMGkgc)\
	This tutorial covers the part of using Yeti Tech's AWS client via UE to use Game lift sessions.

### GameLift monitor tool Details:
[AWSTools/Readme.md](AWSTools/Readme.md)

# Future plans:
	1. Adding login mechanism like Steam login to the game
	2. Automating session creation and basic setup for Unreal to work with AWS currently most of stuff is manual.
	3. Adding team based gameplay.Current target was just POC, so focus was more on getting it to AWS than adding maore gameplay feratures.
	
# Testing plan:
The basic test plan is under document **"Test plan for AWS Independent Study.pdf"**.

# Resources:
- GDC talks and Tutorials being used for the project can be found at *[link](https://docs.google.com/spreadsheets/d/1rYbCugIDJeewsHSxHRQ65mhBmB13Ui00EbTWOu1p5P4/edit?usp=sharing)*

- Resource links in the repo are under folder Research_docs

# Credits:
The starting FPS code for the project is taken from [Tom Looman's FPS Template](https://www.tomlooman.com/fps-template/)

[UE4 Client SDK by Yeti Tech](https://github.com/YetiTech-Studios/UE4GameLiftClientSDK/tree/688cc418cc3b7fe8e0eaae5aefbb3758ddc89120)

### AWS CLI to push the build to lift
`aws gamelift upload-build --name FPSGame --build-version 1.0 --build-root "D:\AWS_Multiplayer\package\WindowsNoEditor" --operating-system WINDOWS_2012 --region us-east-1`

### AWS CLI to create game session on gamelift
`aws gamelift create-game-session --maximum-player-session-count 10 --fleet-id <fleet_id>`
