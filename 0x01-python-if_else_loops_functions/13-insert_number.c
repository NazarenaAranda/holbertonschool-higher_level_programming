#include "lists.h"

/**
 *insert_node - insertar un nodo
 *@head: primer nodo
 *@number: numero
 *Return: nuevo
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *temporal = NULL;
	listint_t *prev_node = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	temporal = *head;
	if (!temporal || number <= temporal->n)
	{
		new_node->next = temporal;
		*head = new_node;
	}

	while (temporal && number > temporal->n)
	{
		prev_node = temporal;
		temporal = temporal->next;
	}

	if (prev_node)
		prev_node->next = new_node;
	new_node->next = temporal;
	return (new_node);
}
