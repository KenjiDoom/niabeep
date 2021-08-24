# Niabeep
Niabeep is a GUI program designed for sending google emails, using googles SMTP servers. It was coded using python's built in tkinter and smtplib library. Note: In order to use this UI program the user must enable Less secure app access in there [google account security settings.](https://myaccount.google.com/lesssecureapps)  
![](prototype/LESSAPP.png)
## Installation
1. Clone repo
```
git clone https://github.com/KenjiDoom/niabeep.git
```
2. Install Tkinter (arch linux) 
```
pacman -S tk
```
3. Run program
```
python niabeep.py
```

Login prompt             |  Sending email prompt
:-------------------------:|:-------------------------:
![](prototype/login_prompt.png)|![](prototype/sending_prompt.png)

Overall we get an approval rating of 7/10 this GUI needs more work, but overall it's a good start.

### TO-DO
- [] - Sending Attachments
- [] - Cancel Button
- [] - HTML Formatting
- [] - Custom Fonts? 
