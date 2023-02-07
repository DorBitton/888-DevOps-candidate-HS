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


## Solution
As an example I've changed the process to gedit ubuntu process:

before running the code, gedit process is closed
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Scripting-Process-Monitoring/images/Screenshot%20from%202023-02-07%2002-39-11.png?raw=true" alt="Terminal">

Script opened gedit process, and counting if maintanance file exists:
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Scripting-Process-Monitoring/images/Screenshot%20from%202023-02-07%2002-39-31.png?raw=true" alt="Terminal">
 
 Creating the csv file:
 
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Scripting-Process-Monitoring/images/Screenshot%20from%202023-02-07%2002-47-41.png?raw=true" alt="terminal">

GUI opened with 2 buttons:
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Scripting-Process-Monitoring/images/Screenshot%20from%202023-02-07%2002-39-48.png?raw=true" alt="Terminal">

Clicking on show entries will show us when process started:
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Scripting-Process-Monitoring/images/Screenshot%20from%202023-02-07%2002-40-40.png?raw=true" alt="Terminal">

We can save the number of times in a different file:
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Scripting-Process-Monitoring/images/Screenshot%20from%202023-02-07%2002-40-51.png?raw=true" alt="Terminal">
