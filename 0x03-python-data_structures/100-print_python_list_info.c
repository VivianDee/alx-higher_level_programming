#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - A function that prints some basic
 *info about Python lists
 * @p: A pointer
 */
void print_python_list_info(PyObject *p)
{
	PyObject *element = NULL
	const char *type = NULL
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
