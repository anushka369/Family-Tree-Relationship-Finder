from pyDatalog import pyDatalog
import graphviz

# Initialize PyDatalog
pyDatalog.create_terms('parent, child, sibling, grandparent, ancestor, common_ancestor, cousin, degree_of_relationship, X, Y, Z')

# Define sibling relationships based on shared parents
sibling(X, Y) <= (parent(Z, X)) & (parent(Z, Y)) & (X != Y)

# Define grandparent relationships based on parent-child relationships
grandparent(X, Y) <= (parent(X, Z)) & (parent(Z, Y))

# Define the degree of relationship between two people
degree_of_relationship(X, Y, 1) <= parent(X, Y)
degree_of_relationship(X, Y, D) <= (parent(X, Z)) & (degree_of_relationship(Z, Y, D1)) & (D == D1 + 1)

# Define ancestor relationships recursively
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= (parent(X, Z)) & (ancestor(Z, Y))

# Define common ancestor for two people
common_ancestor(X, Y, Z) <= ancestor(Z, X) & ancestor(Z, Y)

# Define cousins
cousin(X, Y) <= (parent(Z, X)) & (sibling(Z, W)) & (parent(W, Y))

# Helper function to add a parent-child relationship to the family tree
def add_parent_child(parent_name, child_name):
    +parent(parent_name, child_name)

# Function to find the earliest common ancestor of two people
def find_common_ancestor(person1, person2):
    result = common_ancestor(person1, person2, Z)
    if result:
        return Z.data[0]
    else:
        return "No common ancestor found"

# Function to visualise the family tree using Graphviz
def visualize_family_tree():
    dot = graphviz.Digraph(comment="Family Tree")

    # Add parent-child relationships to the tree
    for rel in parent.data:
        dot.edge(rel[0], rel[1])

    # Render the tree as an image
    dot.render('family_tree', format='png')
    print("Family tree diagram generated as 'family_tree.png'.")

    # User inputs for building the family tree
    while True:
        print("\nChoose an operation:")
        print("1. Add a parent-child relationship")
        print("2. Find siblings")
        print("3. Find grandparents")
        print("4. Find degree of relationship")
        print("5. Find common ancestor")
        print("6. Find cousins")
        print("7. Generate family tree diagram")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            parent_name = input("Enter the parent's name: ")
            child_name = input("Enter the child's name: ")
            add_parent_child(parent_name, child_name)
            print(f"Parent-child relationship added: {parent_name} -> {child_name}")

        elif choice == 2:
            person = input("Enter the person's name to find their siblings: ")
            siblings = sibling(person, Y)

            if siblings:
                print(f"Siblings of {person}: {[Y for Y in siblings.data]}")
            else:
                print(f"No siblings found for {person}.")

        elif choice == 3:
            person = input("Enter the person's name to find their grandparents: ")
            grandparents = grandparent(X, person)

            if grandparents:
                print(f"Grandparents of {person}: {[X for X in grandparents.data]}")

            else:
                print(f"No grandparents found for {person}.")

        elif choice == 4:
            person1 = input("Enter the first person's name: ")
            person2 = input("Enter the second person's name: ")
            degree = degree_of_relationship(person1, person2, D)

            if degree:
                print(f"Degree of relationship between {person1} and {person2}: {degree.data[0][2]}")
            else:
                print(f"No relationship found between {person1} and {person2}.")

        elif choice == 5:
            person1 = input("Enter the first person's name: ")
            person2 = input("Enter the second person's name: ")
            ancestor = find_common_ancestor(person1, person2)
            print(f"Earliest common ancestor of {person1} and {person2}: {ancestor}")

        elif choice == 6:
            person = input("Enter the person's name to find their cousins: ")
            cousins = cousin(person, Y)

            if cousins:
                print(f"Cousins of {person}: {[Y for Y in cousins.data]}")
            else:
                print(f"No cousins found for {person}.")

        elif choice == 7:
            visualize_family_tree()
            
        elif choice == 8:
            break
            
        else:
            print("Invalid choice. Try again.")
