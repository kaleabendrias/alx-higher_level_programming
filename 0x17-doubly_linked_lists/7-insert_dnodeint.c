#include "lists.h"

/**
 * insert_dnodeint_at_index - inserts a node node at a given position
 * in a dlistint_t list.
 * @h: pointer to the list.
 * @idx: position to add the node.
 * @n: data for the new node.
 * Return: the address of the new node, or NULL if it failed
 **/
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *aux_n = *h, *new_n;
	unsigned int index, con = 0;

	/* create node */
	new_n = malloc(sizeof(dlistint_t));
	if (new_n == NULL)
		return (NULL);
	new_n->n = n;

	/* border case for insert at the beginning */
	if (idx == 0)
	{
		new_n->prev = NULL;
		new_n->next = *h;
		if (*h)
			(*h)->prev = new_n;
		*h = new_n;
		return (*h);
	}

	/* search of position to insert */
	index = idx - 1;
	while (aux_n && con != index)
	{
		con++;
		aux_n = aux_n->next;
	}

	/* general case */
	if (con == index && aux_n)
	{
		new_n->prev = aux_n;
		new_n->next = aux_n->next;
		if (aux_n->next)
			aux_n->next->prev = new_n;
		aux_n->next = new_n;
		return (new_n);
	}
	free(new_n);
	return (NULL);
}
