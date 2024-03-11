#include "lists.h"
/**
 * check_cycle - func that check if a singly linked list has a cycle in it
 * @list:pointer to struct
 *Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *check, *prove;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	check = list->next;
	prove = list->next->next;

	while (check && prove && prove->next)
	{
		if (check == prove)
		{
			return (1);
		}
		check = check->next;
		prove = prove->next->next;
	}
	return (0);
}
