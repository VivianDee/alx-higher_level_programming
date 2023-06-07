#include "lists.h"

int check_cycle(listint_t *list)
{
	int i;
	listint_t *temp = NULL;

	temp = list;
	for (i = 0; temp != NULL; i++)
	{
		if (temp < temp->next)
			return (1);
		else
			temp = temp->next;
	}
	return (0);
}
