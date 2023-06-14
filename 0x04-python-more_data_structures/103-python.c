#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(list);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = item->ob_type->tp_name;

		printf("Element %zd: %s\n", i, item_type);
	}
}
/**
 * print_python_bytes - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_GET_SIZE(p);
	data = PyBytes_AS_STRING(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", data);
	printf("  first %zd bytes: ", (size + 1 < 10) ? size + 1 : 10);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02hhx%c", data[i], (i + 1 < size + 1 && i + 1 < 10) ? ' ' : '\n');
}
