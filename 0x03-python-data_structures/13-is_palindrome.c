#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

void reverse_list(listint_t **head);

/**
 * is_palindrome - checks
 * @head: double pointer to head
 * Return: Always
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev;
	listint_t *second_h, *mid_n;
	int palindrome;

	palindrome = 1;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = *head;
	fast = *head;
		prev = *head;
	mid_n = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid_n = slow;
		slow = slow->next;
	}
	second_h = slow;
	prev->next = NULL;
	reverse_list(&second_h);
	palindrome = compare_lists(*head, second_h);
	reverse_list(&second_h);
	if (mid_n != NULL)
	{
		prev->next = mid_n;
		mid_n->next = second_h;
	}
	else
		prev->next = second_h;
	return (palindrome);
}

/**
 * reverse_list - reverse linkned list
 * @head: double pointer
 * Return: none
 */
void reverse_list(listint_t **head)
{
	listint_t *prev, *current, *next;
	prev = NULL;
	current = *head;
	next = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * compare_lists - compare
 * @list1: pointer to first
 * @list2: pointer to second
 * Return: ALways
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1 != NULL && list2 != NULL)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (list1 == NULL && list2 == NULL);
}
