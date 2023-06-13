#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - A function that checks if a singly linked list is a
 *palindrome
 * @head: A pointer to the head of a linked list
 *
 * Return:
 * - (0) if it is not a palindrome
 * - (1) if the linked list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;


	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next;
		if (fast != NULL)
			fast = fast->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
		slow = slow->next;
	while (slow != NULL)
	{
		if (prev == NULL)
			return(0);
		if (prev->n != slow->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
