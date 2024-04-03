#include "lists.h"
/**
 * dlistint_len - func that returns num of element in double
 * @h:pointer
 * Return:0
 */
size_t dlistint_len(const dlistint_t *h)
{
	int itr;

	itr = 0;

	if (h == NULL)
		return (itr);
	while (h->prev != NULL)
		h = h->prev;
	while (h != NULL)
	{
		itr++;
		h = h->next;
	}
	return (itr);
}
