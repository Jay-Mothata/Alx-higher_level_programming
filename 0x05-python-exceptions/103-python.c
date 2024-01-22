#include <Python.h>

/**
 * print_python_list - prints information about Python lists
 * @p: a PyObject pointer to a Python list
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints information about Python bytes
 * @p: a PyObject pointer to a Python bytes object
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - prints information about Python float objects
 * @p: a PyObject pointer to a Python float object
 *
 * Return: void
 */

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AsDouble(p));
}

