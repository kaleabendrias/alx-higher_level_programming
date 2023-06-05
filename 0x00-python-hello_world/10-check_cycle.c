#include "lists.h"

/**
 * check_cycle - checks if the list has cycle or not
 * @list: list
 * Return: Always
 */

int check_cycle(listint_t *list)
{
	listint_t *one = list;
	listint_t *two = list;

	if (list == NULL)
		return (0);

	while (two && two->next)
	{
		one = one->next;
		two = two->next->next;
		if (two == one)
			return (1);
	}
	return (0);
}
