# Info-ChatBot
This is a simple Rasa bot that uses a form to get information from the user.

## Running the assistant
1. Install Rasa Open Source: https://rasa.com/docs/rasa/user-guide/installation/ <br />
https://rasa.com/docs/rasa-x/0.42.x/installation-and-setup/install/local-mode/

2. Train the model:

    ``rasa train``

3. Open a second terminal window and start the action server:

    ``rasa run actions``

4. Return to the first terminal window and start the assistant on the command line:

    ``rasa x``
