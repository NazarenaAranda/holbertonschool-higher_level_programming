#include "lists.h"

/**
 * check_cycle - chequea el ciclo de la linked list
 * @list: linkedn list
 * Return: 0 o 1, depende si existe el ciclo
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuguita;
	listint_t *liebre;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	while (tortuguita && liebre && liebre->next)
	{
		if (tortuguita == liebre)
			return (1);
		tortuguita = tortuguita->next;
		liebre = liebre->next->next;
	}
	return (0);
}
