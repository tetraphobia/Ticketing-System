# Ticket System

# What is it?
This is a ticketing system operating using queue style organization. The goal is to create a simple software that customer service and developers can use to recieve complaints/feedbacks from users of some form of software. 

# Requirements
- Python (3.13.3)
- Django (5.2.1) Follow this link in order to install https://docs.djangoproject.com/en/5.2/intro/install/

# Usage
\`\`\`bash
python -m venv venv                     # Create a venv
source venv/bin/activate             # Activate the venv
pip install -r requirements.txt    # Install dependencies
python manage.py runserver      # Run the server
\`\`\`

# How to run it? 
The system will be run behind the scenes and accessed through an admin portion of the website it is built for. This way it's modular and can be accessed by any admin in order for the spread of ticket management. 
