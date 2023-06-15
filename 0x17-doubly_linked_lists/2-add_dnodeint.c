#include "lists.h"

/**
 * add_dnodeint - adds a new node at the beginning of a dlistint_t list.
 * @head: pointer to the first element of the list.
 * @n: int to set in the new node.
 * Return: address of the new element, or NULL if it failed
 **/
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *ne;

	ne = malloc(sizeof(dlistint_t));
	if (ne == NULL)
		return (NULL);

	ne->n = n;
	ne->prev = NULL;
	ne->next = *head;
	if (*head)
		(*head)->prev = ne;
	*head = ne;

	return (new);
}
