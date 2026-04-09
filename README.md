# Python Programs Collection

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  <img src="https://img.shields.io/badge/VS_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="VS Code"/>
</div>

## 📋 Overview

A comprehensive collection of Python programs covering various topics from my programming curriculum. This repository contains programs ranging from basic concepts to advanced applications including a full Django web application.

## 🗂️ Repository Structure

### 📁 IInd_unit/
Unit 2 programming exercises and academic programs
- `academic.py` - CGPA calculation system
- `matrix.py` - Matrix operations
- `u2_p1.py` to `u2_p15.py` - Various programming problems

### 📁 OOP/
Object-Oriented Programming examples
- `p1.py` - Shape classes (Circle, etc.) with inheritance
- `p2.py` - OOP concepts demonstration
- `p3.py` - Advanced OOP examples

### 📁 pro/
Programming problems and utilities
- `fibonacci(p9).py` - Fibonacci sequence generator
- `birthday(p12).py` - Birthday calculator
- `blood_group(p5).py` - Blood group analyzer
- `cards(p1).py` - Card game simulations
- `collatz_sequence(p10).py` - Collatz conjecture implementation
- `Exact_change(p13).py` - Change calculation algorithm
- `student_marks(p8).py` - Student grade management
- `stringmanipulation(p4).py` - String processing utilities
- And many more programming exercises...

### 📁 python_program_list/
Comprehensive list of Python programs (p1.py through p20.py)
- Basic to advanced Python programming concepts
- Algorithm implementations
- Data structure examples

### 📁 taskmanager/
**Django Web Application** - Task Management System
- Full-stack Django project with SQLite database
- Features: Add, update, delete, and view tasks
- Templates for user interface
- RESTful API endpoints

### 📁 python unit 2/
Additional Unit 2 programming exercises
- Numbered programs (1.py through 15.py)
- File operations and data processing

### 📁 unit 1 & 2 extra/
Extended collection of programs from Units 1 and 2
- 24 comprehensive programs
- Advanced concepts and algorithms

## 🚀 Tech Stack

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
</div>

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Clone the Repository
```bash
git clone https://github.com/GayatriParimiDev/Python-Programs.git
cd Python-Programs
```

### Django Task Manager Setup
```bash
cd taskmanager

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install Django
pip install django

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the task manager application.

## 🎯 Program Categories

### 🔢 Mathematical Programs
- Fibonacci sequences
- Matrix operations
- CGPA calculations
- Collatz conjecture
- Exact change algorithms

### 🎮 Game & Simulation
- Card games
- Number guessing games
- Text-based adventures

### 📊 Data Processing
- Student marks management
- File I/O operations
- JSON data handling
- Text processing utilities

### 🏗️ Object-Oriented Programming
- Shape hierarchies
- Inheritance examples
- Polymorphism demonstrations
- Class design patterns

### 🌐 Web Development
- Django task management system
- CRUD operations
- Template rendering
- Database interactions

## 📖 Usage Examples

### Running Individual Programs
```bash
# Navigate to specific folder
cd pro

# Run a program (example: Fibonacci)
python fibonacci(p9).py
```

### Academic CGPA Calculator
```python
from IInd_unit.academic import add_course, calculate_cgpa

# Add courses with credits and grade points
add_course("Mathematics", 4, 9.5)
add_course("Physics", 3, 8.0)
add_course("Computer Science", 4, 9.0)

# Calculate CGPA
cgpa = calculate_cgpa()
print(f"Your CGPA is: {cgpa:.2f}")
```

### Shape Area Calculator (OOP)
```python
from OOP.p1 import Circle

# Create a circle object
circle = Circle(5)
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Program Documentation

Each program includes comments explaining:
- Purpose and functionality
- Input requirements
- Output format
- Algorithm used (where applicable)

## 🏆 Learning Outcomes

This collection demonstrates:
- ✅ Basic Python syntax and data types
- ✅ Control structures (loops, conditionals)
- ✅ Functions and modules
- ✅ File I/O operations
- ✅ Object-oriented programming
- ✅ Data structures and algorithms
- ✅ Web development with Django
- ✅ Database interactions
- ✅ Error handling and validation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Gayatri Parimi**
- GitHub: [@GayatriParimiDev](https://github.com/GayatriParimiDev)
- Repository: [Python-Programs](https://github.com/GayatriParimiDev/Python-Programs)

---

<div align="center">
  <p><strong>⭐ Star this repository if you found it helpful!</strong></p>
  <p>Built with ❤️ using Python</p>
</div>