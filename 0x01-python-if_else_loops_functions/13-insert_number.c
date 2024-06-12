#include "lists.h"
/**
 * insert_node - func hat inserts number into sorted singly linked list
 * @head: pointer to the firstnoode
 * @number: number to be inserted
 * Return: 0
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *in_node, *nodee;

	if (head == NULL)
		return (NULL);

	in_node = malloc(sizeof(listint_t));
	if (in_node == NULL)
		return (NULL);

	in_node->n = number;
	in_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		in_node->next = *head;
		*head = in_node;
		return (in_node);
	}

	nodee = *head;
	while (nodee->next != NULL && nodee->next->n < number)
	{
		nodee = nodee->next;
	}

	in_node->next = nodee->next;
	nodee->next = in_node;

	return (in_node);
}
