#include "lists.h"
/**
 * print_dlistint - func that print elements of a list
 * @dlistint_t: list
 * @h: pointer to list
 * Return:0
 */
size_t print_dlstint(const dlistint_t *h)
{
	int itr;
	
	itr = 0;
	if (h== NULL)
	{
		return (itr);
	}
	while (h->prev != NULL)
		h= h->prev;
	while (h != NULL)
	{
		printf("%d\n", h->n);
		itr++;
		h = h->next;
	}

	return (itr);
}
