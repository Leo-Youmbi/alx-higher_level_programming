# Python - Classes and Objects
In this project, I began practicing object-oriented programming using classes and objects in Python. I learned about attributes, methods, and properties as well as data abstraction, data encapsulation, and information hiding.


## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                           | Prototype                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `0-square.py`    | `class Square:`                                                                    |
| `1-square.py`          | `class Square:`                                                           |
| `2-square.py`                | `class Square:`                                                                               |
| `3-square.py`         | `class Square:`                                                                      |
| `4-square.py`      | `class Square:`                                                                   |
| `5-square.py`             | `class Square:`                                                                          |
| `6-square.py` | `class Square:`                                                              |
| `100-singly_linked_list.py`        | <ul><li>`class Node:`</li><li>`class SinglyLinkedList:`</li></ul>                                                                         |
| `101-square.py`     | `class Square:`                                                                       |
| `102-square.py`        | `class Square:`                                                                |

## Tasks :page_with_curl:

* **0. My first square**
  * [0-square.py](./0-square.py): An empty python class that defines a square.
  * You are not allowed to import any module

* **1. Square with size**
  * [1-square.py](./1-square.py): Python class that pdefines a square by: (based on [0-square.py](./0-square.py))
  * Private instance attribute: `size`
  * Instantiation with `size` (no type/value verification)
  * You are not allowed to import any module

* **2. Size validation**
  * [2-square.py](./2-square.py): Python class that defines a square by: (based on [1-square.py](./1-square.py)).
  * Private instance attribute: `size`
  * Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
  * You are not allowed to import any module



* **3. Area of a square**
  * [3-square.py](./3-square.py): Python class that defines a square by: (based on [2-square.py](./2-square.py))
  * Private instance attribute: `size`
  * Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
  * Public instance method: `def area(self):` that returns the current square area
  * You are not allowed to import any module

* **4. Access and update private attribute**
  * [4-square.py](./4-square.py): Python class that defines a square by: (based on [3-square.py](./3-square.py))
  * Private instance attribute: `size`
    * property `def size(self):` to retrieve it.
    * property setter `def size(self, value):` to set.
      * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
  * Instantiation with optional `size`: `def __init__(self, size=0):`
  * Public instance method: `def area(self):` that returns the current square area
  * You are not allowed to import any module.

* **5. Printing a square**
  * [5-square.py](./5-square.py): Python class that that defines a square by: (based on [4-square.py](./4-square.py))
  * Private instance attribute: `size`
    * property `def size(self):` to retrieve it.
    * property setter `def size(self, value):` to set.
      * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
  * Instantiation with optional `size`: `def __init__(self, size=0):`
  * Public instance method: `def area(self):` that returns the current square area.
  * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line
  * You are not allowed to import any module.

* **6. Coordinates of a square**
  * [6-square.py](./6-square.py): Python class that
  defines a square by: (based on [5-square.py](./5-square.py))
  * Private instance attribute: `size`
    * property `def size(self):` to retrieve it.
    * property setter `def size(self, value):` to set.
      * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
      * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`.
  * Private instance attribute: `position`:
    * property `def position(self):` to retrieve it
    * property setter `def position(self, value):` to set it:
      * `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`.
  * Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
  * Public instance method: `def area(self):` that returns the current square area.
  * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line.
    * `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
  * You are not allowed to import any module.

* **7. Singly linked list**  
  [100-singly_linked_list.py](./100-singly_linked_list.py):  
  Python class `Node` that defines a node of a singly linked list by:
  * Private instance attribute: `data`:
    * property `def data(self):` to retrieve it
    * property setter `def data(self, value):` to set it:
      * `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`
  * Private instance attribute: `next_node`:
      * property `def next_node(self):` to retrieve it
      * property setter `def next_node(self, value):` to set it:
        * `next_node` can be None or must be a Node, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`
    * Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`

   And, a Python class `SinglyLinkedList` that defines a singly linked list by:  
  * Private instance attribute: `head` (no setter or getter)
  * Simple instantiation: `def __init__(self):`
  * Should be printable:
    * print the entire list in stdout
    * one node number by line
  * Public instance method: `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order)
  * You are not allowed to import any module

* **8. Print Square instance**
  * [101-square.py](./101-square.py): Python function that defines a square by: (based on [6-square.py](./6-square.py))
  * Private instance attribute: `size`
    * property `def size(self):` to retrieve it.
    * property setter `def size(self, value):` to set.
      * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`.
      * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`.
  * Private instance attribute: `position`:
    * property `def position(self):` to retrieve it
    * property setter `def position(self, value):` to set it:
      * `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`.
  * Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
  * Public instance method: `def area(self):` that returns the current square area.
  * Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line.
    * `position` should be use by using space.
  * Printing a `Square` instance should have the same behavior as `my_print()` 
  * You are not allowed to import any module.

* **9. Compare 2 squares**
  * [102-square.py](./102-square.py): Python function that defines a square by: (based on [4-square.py](./4-square.py))
  * Private instance attribute: `size`
    * property `def size(self):` to retrieve it.
    * property setter `def size(self, value):` to set.
      * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
  * Instantiation with optional `size`: `def __init__(self, size=0):`
  * Public instance method: `def area(self):` that returns the current square area.
  * `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area.
  * You are not allowed to import any module.
