# School Management System

## Overview

This repository contains a simple School Management System implemented in Python using MySQL as the database. The main program file is `main.py`, and a demo MySQL database file (`student.idb`) is provided for initial testing.

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/school-management-system.git
   cd school-management-system
   ```

2. **Database Setup:**
   Place the `student.idb` file in the following directory:
   ```
   C:\ProgramData\MySQL\MySQL Server 8.0\Data\school
   ```
   Make sure to create a database named `school` in MySQL.

3. **Configure Main Program:**
   Open the `main.py` file and update the following variables with your MySQL credentials:
   ```python
   # main.py

   DB_CONFIG = {
       'host': 'your_mysql_host',
       'user': 'your_mysql_user',
       'password': 'your_mysql_password',
       'database': 'school',
   }
   ```

4. **Run the Program:**
   Execute the main program:
   ```
   python main.py
   ```

## Database Information

The `student.idb` file serves as a demo MySQL database for the School Management System. It contains sample data to get you started.

## Dependencies

Make sure you have the required dependencies installed. You can install them using:
```
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
