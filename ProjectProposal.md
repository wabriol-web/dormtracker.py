**The DormTracker**  
   
**II.  Problem Description:** When living in a dorm room with others, it can be difficult to keep track of chore assignments, room group supply fund debts, and neat little facts about each roommate. If room chores are not tracked, certain roommates will do more than others. If nothing is written down, shared debts will be lost in the shuffle. DormTracker allows users to create a room profile which automatically rotates chores and saves personal descriptions about each roommate in a digital almanac.

**III.  Goals:**   
Create Room & User Profile: When DormTracker first runs it will ask for the users dorm room number, their name, and each of their roommates names and a quick description.  
Chore Rotator: Assign each person a cleaning chore everyday with no repetitions.  
Almanac Look-up: Access any of your roommate's profile and description in less than 2 seconds.

**IV.  Features:**   
Startup Questions: When Dorm Tracker first opens, ask users for their room number, their name, how many roommates they have, each of their roommates names, and a quick description to save about each of them.  
Roommate Almanac: Allows users to look up any of their roommate's profile information and description that they saved.  
Automatic Chore Scheduler: Assign each roommate a different cleaning chore in an equal rotation.  
Supply Debt Tracker: Keep track of any collective supply purchases the room makes and calculate who is owes whom and how much.

**V. Inputs and Outputs:**   
Inputs: Room number, user name, number of roommates, roommate names, description of roommates, list of cleaning chores, cost of bought item, name of person who paid for item.  
Outputs: Welcome message with room number, formatted view of roommate's profile and description, board member with a cleaning chore, message stating who owes whom and how much, main menu option. 

**VI. Pseudocode:**

**START**  
  **PROMPT user for room\_number**  
  **PROMPT user for user\_name**  
  **PROMPT user for total\_roommates**  
    
  **FOR i FROM 1 TO total\_roommates DO**  
    **PROMPT for roommate\_name**  
    **PROMPT for roommate\_description**  
    **STORE roommate\_name and roommate\_description in almanac\_dictionary**  
  **ENDFOR**

  **SET running \= TRUE**  
    
  **WHILE running IS TRUE DO**  
    **DISPLAY "=== DORMTRACKER: ROOM " \+ room\_number \+ " \==="**  
    **DISPLAY "User: " \+ user\_name**  
    **DISPLAY "\[1\] Roommate Almanac"**  
    **DISPLAY "\[2\] Manage Cleaning Chores"**  
    **DISPLAY "\[3\] Log Shared Expense"**  
    **DISPLAY "\[4\] View Summary & Balances"**  
    **DISPLAY "\[5\] Exit Program"**  
    **PROMPT user for choice**

    **IF choice \== 1 THEN**  
      **DISPLAY list of registered roommates**  
      **PROMPT user to select a roommate name**  
      **IF selected name EXISTS in almanac\_dictionary THEN**  
        **DISPLAY roommate\_name \+ ": " \+ stored roommate\_description**  
      **ELSE**  
        **DISPLAY "Error: Roommate not found."**  
      **ENDIF**

    **ELSE IF choice \== 2 THEN**  
      **PROMPT user for list of chores**  
      **FOR each chore DO**  
        **ASSIGN chore to roommate using round-robin index**  
      **ENDFOR**  
      **DISPLAY generated cleaning schedule**

    **ELSE IF choice \== 3 THEN**  
      **GET expense item name, total cost, AND payer name**  
      **IF cost \<= 0 THEN**  
        **DISPLAY "Error: Cost must be a positive number."**  
      **ELSE**  
        **CALCULATE split\_amount \= total cost / total\_roommates**  
        **UPDATE balances for each roommate**  
        **DISPLAY "Expense logged successfully."**  
      **ENDIF**

    **ELSE IF choice \== 4 THEN**  
      **DISPLAY overall room summary, chore schedule, and balances**

    **ELSE IF choice \== 5 THEN**  
      **DISPLAY "Exiting DormTracker. Goodbye\!"**  
      **SET running \= FALSE**

    **ELSE**  
      **DISPLAY "Invalid choice. Please select 1 to 5."**  
    **ENDIF**

  **ENDWHILE**  
**END**  
