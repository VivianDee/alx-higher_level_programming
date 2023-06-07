#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: A pointer to the head of the list
 *
 * Return:
 *-(0) if there is no cycle
 *-(1) if there i a cycle
 */

int check_cycle(listint_t *list)
{
	int i;
	listint_t *temp = NULL;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	temp = list;
	for (i = 0; temp != NULL; i++)
	{
		if (temp < temp->next && temp->next != NULL)
			return (1);
		temp = temp->next;
	}
	return (0);
}
