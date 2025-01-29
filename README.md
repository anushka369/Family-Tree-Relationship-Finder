# Family Tree Relationship Finder 🌳

## Introduction
The **Family Tree Relationship Finder** is a Python-based program that utilizes **PyDatalog** to model and query family relationships. It allows users to add parent-child relationships, find siblings, grandparents, common ancestors, cousins, and determine the degree of relationship between individuals. The program also includes a **Graphviz** visualization feature to generate a graphical representation of the family tree.

---

## Features 💡
- **Add Parent-Child Relationship**: Users can input family connections dynamically.
- **Find Siblings**: Identify individuals who share a common parent.
- **Find Grandparents**: Discover grandparents based on parent-child connections.
- **Determine Degree of Relationship**: Calculate the number of generations separating two individuals.
- **Find Common Ancestors**: Locate the earliest common ancestor of two individuals.
- **Find Cousins**: Identify cousin relationships based on family lineage.
- **Generate Family Tree Diagram**: Visual representation using Graphviz.

---

## Technologies Used 🌐
- **Python 3**
- **PyDatalog** for logic programming
- **Graphviz** for visualizing family trees
  
---

## Installation & Setup ⚙
1. Ensure **Python 3** is installed on your system.
2. Install required dependencies using pip:
   ```sh
   pip install pyDatalog graphviz
   ```
3. Ensure Graphviz is installed and added to the system path (if not installed, download from [Graphviz](https://graphviz.gitlab.io/download/)).

## How to Run 💻

1. Save the script as `family_tree.py`.
2. Run the program:
   ```sh
   python family_tree.py
   ```
3. Follow the on-screen prompts to add relationships and query the family tree.

--- 

## User Guide 📝

### Adding a Parent-Child Relationship
1. Select option **1** in the menu.
2. Enter the parent's name and child's name.
3. The relationship will be stored in the system.

### Finding Siblings
1. Select option **2**.
2. Enter the person's name.
3. The program will list their siblings if available.

### Finding Grandparents
1. Select option **3**.
2. Enter the person’s name.
3. The program will display their grandparents.

### Determining Degree of Relationship
1. Select option **4**.
2. Enter the names of two individuals.
3. The program will compute their degree of relationship.

### Finding a Common Ancestor
1. Select option **5**.
2. Enter two individuals' names.
3. The program will return their earliest common ancestor.

### Finding Cousins
1. Select option **6**.
2. Enter a person's name.
3. The program will list their cousins if found.

### Generating a Family Tree Diagram
1. Select option **7**.
2. The program will generate a `family_tree.png` image.

---

## Known Issues & Limitations 📜
- The system does not store data persistently; all relationships are lost when the program exits.
- User input is case-sensitive.
- The visualization only represents direct parent-child relationships.

## Future Improvements 🎯
- Implement a database (SQLite or MongoDB) for persistent storage.
- Add GUI support for a more interactive experience.
- Enhance visualization to include additional relationships.

---

## Author 📎
_Anushka Banerjee_
