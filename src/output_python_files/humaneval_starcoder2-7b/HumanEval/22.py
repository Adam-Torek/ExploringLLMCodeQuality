from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
/0x00-python-hello_world/10-check_cycle.c
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
/0x0C-python-almost_a_circle/models/base.py
#!/usr/bin/python3
""" Base class """
import json
import csv
import os
import turtle
import random
import math
from abc import ABCMeta, abstractmethod
from typing import List, Tuple, Union, Optional


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: List[dict]) -> str:
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs: List['Base']) -> None:
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @staticmethod
    def from_json_string(json_string: str) -> List[dict]:
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary: dict) -> 'Base':
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls) -> List['Base']:
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs: List['Base']) -> None:
        """ Writes the CSV string representation of list_objs to a file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("")
            else:
                f.write(cls.to_csv_string([o.to_dictionary() for o in list_objs]))

    @staticmethod
    def to_csv_string(list_