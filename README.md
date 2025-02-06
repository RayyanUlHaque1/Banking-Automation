### Project Description: Banking Automation System with Validation

This *Banking Automation System* is a fully functional application designed to manage user accounts, facilitate secure money transfers, and send email notifications for significant activities. The system incorporates strong validation checks to ensure data integrity, security, and a seamless user experience. It is equipped with a *user-friendly UI/UX* for easy navigation and robust security measures to protect transactions and personal data.

*Key Features of the System:*

- *User Access via Account Number (ACN) and Password*:
  - *Users: Each user can log in using their unique **Account Number (ACN)* and *personalized password* (as Default **USER=1* and *password=user*).
  - *Admin: Admin uses fixed login credentials with **ACN = 0* and *password = admin*.
  
- *Validation*: All user inputs are validated to ensure proper formatting, prevent errors, and protect against malicious data:
  - *ACN & Password*: Validation checks to ensure the entered ACN is in the correct numeric format and the password is not empty.
  - *Deposit and Withdrawal*: Ensures the amount entered is numeric, greater than zero, and that users have enough balance for withdrawals.
  - *Transfer Amount*: Ensures the transfer amount is valid, numeric, and users have sufficient funds to complete the transfer.
  - *Transaction History*: The system checks that the history table is properly populated before displaying it.

- *Money Transfer*: Users can securely transfer funds between accounts, with real-time balance updates. Validation ensures the transfer amount is valid and there is enough balance in the user's account.
  
- *Check Balance*: Users can easily view their account balance. 
  - Validation ensures that the account is active and the balance retrieval is successful.

- *Update Balance*: Admin can adjust the balance of user accounts (e.g., deposit, withdrawal, or adjustments). 
  - The system ensures the admin updates are within valid limits and follow security protocols.

- *Deposit Amount*: Users can deposit funds, and the system ensures the input amount is valid (positive numeric values).

- *Withdraw Amount*: Users can withdraw funds from their account, with validation ensuring:
  - The withdrawal amount is numeric and greater than zero.
  - The user has sufficient funds in their account.

- *Transaction History*: Users can view their transaction history. The system ensures the data is properly populated and valid before displaying it.

- *OTP and CAPTCHA: Implements **One-Time Passwords (OTP)* and *CAPTCHA* to verify user identity and prevent unauthorized access.
  
- *Email Notifications*: Sends automatic email updates to users for every significant action (deposit, withdrawal, transfer, balance update).

- *Account Creation Email: When an admin creates a new user, a **welcome email* is sent to the user with the account details.

- *Two User Roles*:
  - *Admin Role*: Admin has full access to create, delete, view, and manage users, as well as update account balances and monitor activity.
  - *User Role*: Users can check balances, update balances (via deposit or withdrawal), transfer money, and view transaction history.

---

*Technologies Used:*
Here is the description of the additional libraries and classes you mentioned:

- **Tkinter**: Core library for creating the graphical user interface (GUI). It provides essential components like **Tk**, **Label**, **Frame**, **Entry**, **Button**, **Messagebox**, and **FileDialog** for handling user interactions and displaying data.
  
- **Combobox**: Part of **tkinter.ttk**, it provides a dropdown menu for users to select predefined options, enhancing the user interface with a more compact and convenient selection tool.

- **Time**: This module is used for working with time-related functions, such as generating timestamps for transactions or delays in the application.

- **Gmail**: Used to interact with Gmail API for sending automatic email notifications, such as for account creation, transaction alerts, and other important user activities.

- **Random**: This library is used for generating random numbers or strings, such as creating One-Time Passwords (OTPs) for additional security.

- **SQLite3**: Provides a lightweight, disk-based database to store and manage user information, balances, and transaction records. It supports executing SQL queries to ensure data integrity.

- **PIL (Pillow)**: A library for opening, manipulating, and displaying images. It’s used for adding user photos or logos within the software interface.

- **Database_table**: A custom module for handling interactions with the SQLite database. It contains predefined functions for executing queries related to user and transaction data, ensuring proper validation during database operations.

- **TkinterTable**: Provides functionality for displaying data in a table format within the GUI. **TableCanvas** and **TableModel** are used to create and manage interactive tables, such as showing transaction history with data validation.

- **Re**: The **regular expression** module is used for pattern matching and validating string inputs, such as ensuring that email addresses, account numbers, and other text-based data conform to expected formats.

- **Shutil**: Provides high-level file operations, such as copying, moving, or deleting files and directories. It’s used in scenarios where file handling is required, such as managing user files or backups.

- **Os**: The **os** module provides functions to interact with the operating system, including file and directory manipulation, checking system paths, or creating temporary files for data storage

### User Access & Authentication:
- *Admin Access: Admin can log in using **ACN = 0* and *password = admin*.
  - Validation ensures that the entered credentials match these values for admin login.
- *User Access: Users must enter their **unique Account Number (ACN)* and *password*.
  - Validation ensures that the ACN is numeric, and the password is non-empty and matches the stored data for the given ACN.

---

### Validation Details for All Key Actions:

1. *Login*: 
   - *User ACN*: Checks if the ACN entered is numeric and valid (e.g., no special characters).
   - *Password*: Ensures the password is not empty and matches the stored password for the given ACN.

2. *Deposit/Withdrawal/Transfer*:
   - *Amount*: Ensures the amount entered is a positive numeric value. If the user is withdrawing or transferring, it checks if the account balance is sufficient.
   - *Minimum/Maximum Limits*: Ensures that users cannot deposit, withdraw, or transfer more than allowed limits.

3. *Transaction History*: 
   - *Empty Check*: Before showing the transaction history, the system verifies that there are actual transactions to display.

4. *Admin Operations*: 
   - *User Management*: Admin can create or delete users, but the system checks that no invalid data (e.g., empty account numbers or passwords) is provided.
   - *Balance Update*: Ensures balance changes (deposits or withdrawals) are within valid ranges and do not exceed user limits.

5. *Email Validation*: 
   - *Email Format*: Ensures the user’s email (if applicable) is valid before sending any email notifications (e.g., account creation, transaction updates).

6. *OTP and CAPTCHA*: 
   - *Security Check*: Ensures the correct OTP and CAPTCHA are entered for sensitive actions like transactions and logins.

---

### Flow of Operations:

1. *Login Screen*: The user or admin enters their ACN and password. Validation ensures credentials are correct, and if valid, the user or admin is granted access.
2. *Main Dashboard*: After login, the user can check their balance, update balance, view transaction history, make deposits/withdrawals, or initiate transfers. Each action is validated to prevent errors.
3. *Admin Panel*: Admin has additional options, such as Create Accounts , View Account Holders , Delete Account. The admin’s access is validated through the fixed credentials.

---

This system ensures that *all inputs are validated* for data integrity and security, preventing errors, unauthorized access, and malicious inputs. The user experience is streamlined with clear prompts and validations, making the software both reliable and user-friendly.

