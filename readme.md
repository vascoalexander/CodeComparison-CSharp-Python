# CodeComparison-CSharp-Python

**Description:**
This project contains a collection of simple coding exercises solved in both C# and Python. The goal is to compare the syntax and programming concepts of both languages. Each task is implemented in both C# and Python to highlight differences in syntax and approach.

[Exercises (ENG)](./Exercises_EN.md)  
[Exercises (DE)](./Exercises_DE.md)

## Usage

### Setting Up the C# Environment

1. **Install .NET SDK**: Ensure that the .NET SDK is installed. You can download it from [dotnet.microsoft.com](https://dotnet.microsoft.com/download).

2. **Create a Project**:
   ```sh
   cd CodeComparison-CSharp-Python/CSharp
   dotnet new console -n <ProjectName>
   ```

3. **Run the Program**:
   ```sh
   dotnet run --project <ProjectName>
   ```

### Setting Up the Python Environment

1. **Install Python**: Ensure that Python is installed. You can download it from [python.org](https://www.python.org/).

2. **Create a Virtual Environment**:
   ```sh
   cd CodeComparison-CSharp-Python/Python
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```sh
     .\venv\Scripts\Activate
     ```
   - **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```

4. **Run the Program**:
   ```sh
   python <FileName>.py
   ```
## General Project Structure

```mathematica
CodeComparison-CSharp-Python/
│
├── CSharp/
│   ├── Basics/
│   │   ├── HelloWorld/
│   │   │   └── HelloWorld.cs
│   │   ├── Variables/
│   │   │   └── Variables.cs
│   │   ├── Conditionals/
│   │   │   └── Conditionals.cs
│   │   └── Loops/
│   │       └── Loops.cs
│   ├── DataStructures/
│   │   ├── Arrays/
│   │   │   └── Arrays.cs
│   │   ├── Lists/
│   │   │   └── Lists.cs
│   │   └── Dictionaries/
│   │       └── Dictionaries.cs
│   ├── Algorithms/
│   │   ├── Sorting/
│   │   │   └── Sorting.cs
│   │   ├── Searching/
│   │   │   └── Searching.cs
│   │   └── Recursion/
│   │       └── Recursion.cs
│   └── AdvancedTopicsMiscellaneous/
│       ├── OOP/
│       │   └── OOP.cs
│       ├── FileIO/
│       │   └── FileIO.cs
│       ├── ExceptionHandling/
│       │   └── ExceptionHandling.cs
│       ├── RegularExpressions/
│       │   └── RegularExpressions.cs
│       ├── DateAndTime/
│       │   └── DateAndTime.cs
│       ├── UnitTesting/
│       │   └── UnitTesting.cs
│       └── WebScraping/
│           └── WebScraping.cs
│   └── README.md
│
├── Python/
│   ├── Basics/
│   │   ├── HelloWorld/
│   │   │   └── HelloWorld.py
│   │   ├── Variables/
│   │   │   └── Variables.py
│   │   ├── Conditionals/
│   │   │   └── Conditionals.py
│   │   └── Loops/
│   │       └── Loops.py
│   ├── DataStructures/
│   │   ├── Arrays/
│   │   │   └── Arrays.py
│   │   ├── Lists/
│   │   │   └── Lists.py
│   │   └── Dictionaries/
│   │       └── Dictionaries.py
│   ├── Algorithms/
│   │   ├── Sorting/
│   │   │   └── Sorting.py
│   │   ├── Searching/
│   │   │   └── Searching.py
│   │   └── Recursion/
│   │       └── Recursion.py
│   └── AdvancedTopicsMiscellaneous/
│       ├── OOP/
│       │   └── OOP.py
│       ├── FileIO/
│       │   └── FileIO.py
│       ├── ExceptionHandling/
│       │   └── ExceptionHandling.py
│       ├── RegularExpressions/
│       │   └── RegularExpressions.py
│       ├── DateAndTime/
│       │   └── DateAndTime.py
│       ├── UnitTesting/
│       │   └── UnitTesting.py
│       └── WebScraping/
│           └── WebScraping.py
│   └── README.md
│
└── README.md
```
## Contributing

You are welcome to contribute to this project! If you want to add a new exercise or suggest improvements, please create a pull request.
