# **Collections in Python**

They are data structures, which make it possible to store one or more values.

## **1 - Tuples**

Tuples are collections in Python responsible for storing homogeneous or heterogeneous values. It is an immutable collection, that is, it is not possible to add values, or even modify them. In this way, it ends up being used for data that will not be changed in the context of executing the code. That is, a classic example of usefulness for such a structure would be the abbreviations of the states of Brazil:

* ### **Creating a Tuple**

```python
states = ('MG', 'SP', 'RJ', 'AM', 'PR', 'GO')
```

## **2 - Lists**

Lists are data structures, that is, collections in Python responsible for storing multiple data, homogeneous or heterogeneous. Unlike tuples, it allows changing, adding and even deleting elements from the created List. That said, it is possible to perform a full CRUD on this collection.

* ### **Creating a List**

```python
names = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
```

* ### **Inserting an element to the List**

```python
names.append('Pan')
```

* ### **Updating an element from List**

```python
names[0] = 'Piccolo'
```

* ### **Deleting an element from List**

In this case, it is possible to remove an element by its own value or by its index.

* #### **By value**

```python
names.remove('Trunks')
```

* #### **By index**

```python
names.pop(2)
```

## **3 - Sets**

The sets are data structures, which make it possible to store homogeneous or heterogeneous information. Unlike lists, it does not allow you to have repeated elements and these can be arranged in an unordered way. Still, it is not possible to perform a full CRUD. In this way, it is only possible to create, add and remove elements.

* ### **Creating a Set**

```python
names = {'Goku', 'Trunks', 'Vegeta', 'Trunks', 'Gohan'}`
```

* ### **Inserting element to the Set**

```python
names.add('Piccolo')
```

* ### **Deleting an element from the Set**

```python
names.remove('Trunks')
```

## **4 - Dictionaries**

Finishing off Python's collections, we have dictionaries. Its structure is of the key-value type (having several keys inside the dictionary) and resembles the JSON (JavaScript Object Notation) format. Just like the set, its storage is done in a disorderly way. On a dictionary, you can perform full CRUD, just like on lists. In this way, we can create a dictionary, add the elements, update the elements and remove the elements present in it.

* ### **Creating a Dictionary**

```python
person = {'name': 'Goku','age': 42}
```

* ### **Inserting an element to the Dictionary**

```python
person['sex'] = 'M'
```

* ### **Updating an element from the Dictionary**

```python
person['idade'] = 40
```

* ### **Deleting an element from the Dictionary**

In this case, it is possible to remove an element by its own key in two different ways.

* #### **Deleting without knowing the value**

```python
del person['name']
```

* #### **Deleting with return value, the pop method returns the value related to that key**

```python
x = person.pop('sex')
```
