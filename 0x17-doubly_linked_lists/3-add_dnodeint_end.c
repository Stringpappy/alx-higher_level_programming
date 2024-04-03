#include "lists.h"
/**
 * add_dnodeint_end - func that add a new node to the end of a list
 * @head: pointer
 * @n:data
 * Return:0
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *j;
	dlistint_t *fresh;

	fresh = malloc(sizeof(dlistint_t));
	if (fresh == NULL)
	fresh->n = n;
	fresh->next = NULL;

	j = *head;

	if (j != NULL)
	{
		while (j->next != NULL)
			j = j->next;
		j->next = fresh;
	}
	else
	{
		*head = j;
	}
	fresh->prev = j;

	return (fresh);
}
