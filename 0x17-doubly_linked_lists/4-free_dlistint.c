#include "lists.h"
/**
 * free_dlistint - func that free a list
 * @head:pointer
 * Return: void
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *point;

	if (head != NULL)
	{
		while (head->prev != NULL)
			head = head->prev;
	}
	while ((point =  head) != NULL)
	{
		head = head->next;
		free(point);
	}
}
