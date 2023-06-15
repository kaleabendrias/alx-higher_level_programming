#include "lists.h"

/**
 * get_dnodeint_at_index - returns the nth node of a dlistint_t linked list.
 * @head: pointer to the list.
 * @index: nth node.
 * Return: nth node, if the node doesn't exist, returns NULL.
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *no = head;
	unsigned int con = 0;

	while (no && con != index)
	{
		con++;
		no = no->next;
	}
	if (no && con == index)
		return (no);
	return (NULL);
}
