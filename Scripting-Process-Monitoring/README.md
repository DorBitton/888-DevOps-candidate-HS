## Scripting - Process Monitoring

 -	Top is the most important process on our system, and it must be running the whole time, unless we are under maintenance.
-	When we want to start a maintenance, we need to create a file under /tmp/maintenance.txt
-	When maintenance is done, file can be removed.

First Part

- Please write a script to monitor the Top process. 
- The script will create a CSV file with 2 headers, "Date" & "Message"
- Checks if the process for Top is running 
  - Process is running - Write the current hour, minute & second into the csv file.
     and the message "Top is running"
  - Process is not running - Start the Top process (only if we are not under maintenance mode), write the current hour, minute & second into the csv file and the message "Top was started".

- Checks if a file maintenance exists.
  - Fie Exists - write the current hour, minute & second into the csv file.
  - Write "We are under maintenance mode!" in the message.

- The script should run for 5 minutes and it should sample the process every 5 seconds.

Second Part:
-	Extract from the csv only the lines which have "We are under maintenance mode!" in them.
-	Count & output the amount of lines extracted

Bonus:
-	Extract from the CSV all the lines where Top wasn't running and had to be opened.
-	Show via some GUI all the relevant lines from the CSV.
-	Give the user an option to choose some lines and save them into a separate file.
