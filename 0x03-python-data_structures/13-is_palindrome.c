#include "lists.h"

/**
 * check_len - checks the length of a linked list
 * @head: points to the first node of the list
 *
 * Return: number of nodes in the linked list.
 */

int check_len(listint_t *head)
{
	listint_t *tempPtr = head;
	ssize_t len = 0;

	if (head == NULL)
		return (0);
	while (tempPtr != NULL)
	{
		tempPtr = tempPtr->next;
		len++;
	}
	return (len);
}

/**
 * is_palindrome - checks if a singly linked list is
 * a palindrome
 * @head: points to the first node of the linked list
 *
 * Return: 0 if not a palindrom, otherwise 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tempPtr, *midPtr, *endPtr, *startPtr;
	ssize_t i = 1, j, k, mid, len = 0;

	if (*head == NULL)
		return (1);
	startPtr = *head;
	len = check_len(startPtr);
	tempPtr = midPtr = *head;
	mid = (len / 2) + 1;
	while (i < mid)
	{
		midPtr = midPtr->next;
		i++;
	}
	/* at this point, i == 3 (case "MADAM") */
	j = mid;
	while (j <= len)
	{
		endPtr = midPtr;

		k = j;
		while (k < len)
		{
			endPtr = endPtr->next;
			k++;
		}
		if (tempPtr->n != endPtr->n)
			return (0);
		tempPtr = tempPtr->next;
		j++;
	}
	return (1);
}
