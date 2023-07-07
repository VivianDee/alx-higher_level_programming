#include "hash_tables.h"

/**
* hash_table_print - A function that prints a hash table.
* @ht: The hash table
*
*/

void hash_table_print(const hash_table_t *ht)
{
	unsigned long int i;
	int check = 0;

	printf("{");
	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i] != NULL)
		{
			if (check)
			{
				printf(", ");
				check = 0;
			}
			printf("'%s': '%s'", ht->array[i]->key, ht->array[i]->value);
			check = 1;
		}
	}
	printf("}\n");
}
