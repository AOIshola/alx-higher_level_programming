#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle in it
 * @list: points to the first node in list
 *
 * Return: 0 if there is no cycle, otherwise, 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slowPtr, *fastPtr = NULL;

	slowPtr = fastPtr = list;

	while (slowPtr != NULL)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;

		if (slowPtr = fastPtr)
		{
			return (1);
		}
	}

	return (0);
}
