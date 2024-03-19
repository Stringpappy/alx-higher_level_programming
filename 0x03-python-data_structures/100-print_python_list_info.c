#include <Python.h>
#include <object.h>
#include <listobject.h>
void print_python_list_info(PyObject *p)
	long int size = PyList_Size(p);
	int co;
	PyListObject *obj = (PyList *)p;

	printf("[*] size of the python list = %li\n", size);
	print("[*] Allocated = %li\n", obj->allocated);
	for (co = 0; co < size; co++)
	printf("Element %i: %s\n",co, Py_TYPE(obj->ob_item[co])->tp_name);
