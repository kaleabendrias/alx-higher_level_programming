#include "lists.h"

/**
 * check_cycle - checks if the list has cycle or not
 * @list: list
 * Return: Always
 */

int check_cycle(listint_t *list)
{
	listint_t *one = list;
	listint_t *two = list->next;

	if (list == NULL)
		return (0);

	while (two && one && two->next)
	{
		if (one == two)
			return (1);
		one = one->next;
		two = two->next->next;
	}
	return (0);
}
