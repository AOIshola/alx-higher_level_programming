#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 * @head: points to the first element of the list
 * @number: numbe to insert in list
 *
 * Return: address of the newly added node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prevPtr = NULL, *currentPtr = *head;
	listint_t *newPtr = malloc(sizeof(listint_t));

	if (newPtr == NULL)
		return (NULL);
	newPtr->n = number;
	newPtr->next = NULL;

	if (*head == NULL)
		*head = newPtr;
	while (currentPtr->next != NULL && newPtr->n > currentPtr->n)
	{
		prevPtr = currentPtr;
		currentPtr = currentPtr->next;
	}
	if (currentPtr->next == NULL)
		currentPtr->next = newPtr;
	else if (prevPtr == NULL)
	{
		newPtr->next = *head;
		*head = newPtr;
	}
	else
	{
		newPtr->next = currentPtr;
		prevPtr->next = newPtr;
	}

	return (newPtr);
}
