# Saving code in editor to AWS S3
A user may wish to save the attempt and come back to it at a later time.

In CodeBrat, this is handled by saving the code written in the editor to an Amazon S3 bucket.

This function takes in the following:\
	`username`: the user's CodeBrat username (can be different from the username on Kattis)\
	`problem_id`: the id of the problem on Kattis that the user is writing code to solve\
	`language`: the programming language that the code is written in\
	`code`: the source code