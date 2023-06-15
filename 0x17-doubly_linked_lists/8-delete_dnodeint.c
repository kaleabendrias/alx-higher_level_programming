#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t list.
 * @head: pointer to the list.
 * @index: position of the node to delete.
 * Return: 1 if it succeeded, -1 if it failed.
 **/
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *aux_n = *head;
	dlistint_t *node_to_del = *head;
	unsigned int idx;
	unsigned int con = 0;

	/* border case for empty list */
	if (!(*head))
		return (-1);

	/* border case for delete at the beginning */
	if (index == 0)
	{
		*head = node_to_del->next;
		free(node_to_del);
		if (*head)
			(*head)->prev = NULL;
		return (1);
	}

	/* search of position to delete */
	idx = index - 1;
	while (aux_n && con != idx)
	{
		con++;
		aux_n = aux_n->next;
	}

	/* general case */
	if (con == idx && aux_n)
	{
		node_to_del = aux_n->next;
		if (node_to_del->next)
		node_to_del->next->prev = aux_n;
		aux_n->next = node_to_del->next;
		free(node_to_del);
		return (1);
	}

	return (-1);
}
