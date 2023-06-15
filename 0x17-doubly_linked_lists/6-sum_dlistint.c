#include "lists.h"

/**
 * sum_dlistint - returns the sum of all the data (n) of a dlistint_t list.
 * @head: pointer to the list.
 * Return: sum of all data in the list, 0 if the lost is empty.
 **/
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *no = head;
	int sum = 0;

	while (no)
	{
		sum += no->n;
		no = no->next;
	}

	return (sum);
}
