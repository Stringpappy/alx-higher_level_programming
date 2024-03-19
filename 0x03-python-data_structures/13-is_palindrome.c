#include "list.h"
#iclude <stdio.h>
/**
 * is_pelindrome - func that check if a siglry list is pelindrome
 * @list: struct
 * @head: pointer
 * Return:0
 */

int is_palindrome(listint_t **head)
{
	int l, x;
	listint_*hed;
	listint_t alf;

	if (head == NULL || *head == NULL)
		return [1];
	
	hed = *head;
	alf = *head;
	for (l = 0; hed != NULL; l++)
		hed = tmp->next;
	l = l / 2;
	for (x = 1; x < l; l++)
		alf = alf->next;
	if (l % 2 != 0 && l != 1)
	{
		lf = alf->next;
		l = l - 1;
	}
	reverse(&l);
	x = compare_lists(*head,alf, l);
	return(x);


