#include "lists.h"

/**
 * free_dlistint - frees a dlistint_t list.
 * @head: pointer to the list.
 **/
void free_dlistint(dlistint_t *head)
{
	dlistint_t *actual_n;
	dlistint_t *next_n;

	if (head)
	{
		actual_n = head;
		next_n = head->next;
		while (next_n)
		{
			free(actual_n);
			actual_n = next_n;
			next_n = next_n->next;
		}
		free(actual_n);
	}
}
