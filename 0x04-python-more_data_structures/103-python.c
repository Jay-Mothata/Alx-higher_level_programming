#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", string[i] & 0xff);
	printf("\n");
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python list object
 */

void print_python_list(PyObject *p)
{
	ssize_t size, allocated, i;
	PyObject *element;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	allocated = ((PyVarObject *)p)->ob_size;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, PyBytes_Check(element) ? "bytes" :
									  PyList_Check(element) ? "list" :
									  PyLong_Check(element) ? "int" :
									  PyFloat_Check(element) ? "float" :
									  PyTuple_Check(element) ? "tuple" :
									  PyUnicode_Check(element) ? "str" :
									  "<unprintable type>");
		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
