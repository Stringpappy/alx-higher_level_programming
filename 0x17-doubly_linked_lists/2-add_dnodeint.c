#include "lists.h"
/**
 * add_dnodeint - func that a add a new node to beginning of list
 * @head:pointer
 * @n: data
 * Return
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n){
	dlistint_t *real;
	dlistint_t *j;

	real= malloc(sizeof(dlistint_t));
	if (real == NULL)
		return (NULL);

	real->n = n;
	real->prev = NULL;
	j = *head;

	if (j != NULL)
	{
		while (j->prev != NULL)
			j = j->prev;
	}
	real->next = j;
	if (j != NULL)
		j->prev = real;
	*head = real;

	return (real);
}
